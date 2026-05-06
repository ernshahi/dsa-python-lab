# Amazon Locker Low Level Design

## Step 0: The Approach
Hello Interview LLD Delivery Framework
1. Requirements
- Cover the core functionality and features of the system. Spend some time to understand the problems, talk with interviewer if needed and come up with a list of requirements.

2. Entities
- list out all possible entities in the system. Nouns of the system, what are the things that need to modeled as classes, enums, interfaces, etc.

3. Class Desing
- State and behavior of each one of the entities. 
- State: What are the attributes of the entity?
- Behavior: What are the methods/actions/functions of the entity?

4. Implementation
- Implement the class design in the code. Mostly prefer pseudocode or simple code with comments(language agnostic).

5. Extensibility
- Follow up questions, how system evolves to handle new use cases, new features, new requirements, new constraints, new scale, etc.


# Design a locker system like Amazon locker where delivery drivers can deposit packages and customers can pick them up using a code.

- Always clarify the requirements with the interviewer, and ask questions to understand the problem better. As interviewer looking for your ability to think thorough the problems and how to ask/approach the problem.

Blow are key categories to cover in the design, so ask questions which are related to these categories.
1. primary capabilities
2. error hanling
3. scope boundaries

Primary Capabilities:
- Are there different sized compartments?
- How does the customer get their code? Do we need to send a SMS or email?

Error Handling:
- Can  one customer have multiple packages in the system at once? Are access tokens unique per package?
- How long do the codes last? What happens if it's never picked up?
- What if all compartments are full when a driver tries to deposit a package?

Scope Boundaries:
- What's in scope for this system? Are we modeling the whole deliver flow, or just the piece from when driver arrives at the locker until the customer picks up?


## Step 1: Requirements
1. Carrier deposits a package by specifying size(small, medium, large).
- System assigns an available compartment to matching size.
- Opens compartment and provides a access token or error if no space available.
2. Upon successful deposit, an access token is generated and sent to the customer.
- One access token per package.
3. user retrives package by using the access token.
- System validates token and opens compartment.
- Throws error if token is invalid or expired.
4. Access tokens expire after 7 days
- Expired codes are rejected if used for pickup.
- Package remains in the locker until staff removes it.
5. Staff can open all compartments to manually handle packages.
- System opens all compartments with expired tokens.
- Staff physically removes packages and returns them to sender.

Out ot Scope:
- How the packages gets to the locker(delivery logistics)
- How the access token reaches the customer(SMS/email)


## Step 2: Entities
- Locker
- Compartment
- AccessToken

- Package(External Entity)
- Carrier/Driver(External Entity)
- User(External Entity)

## Step 3: Class Design
- Always start with TopDown approach, start with the main class/orchestrator and then move down to the classes which depends on it.

```python
class Locker:
    - compartments: Compartment[]
    - accessTokensMapping: Map<String, AccessToken>

    + depositPackage(size: Size): AccessToken | Error
    + pickUpPackage(accessToken: String): void | Error
    + openExpiredCompartments(): void

class AccessToken:
    - code: String
    - expiresAt: timestamp
    - compartmentId: Compartment

    + isExpired(): boolean
    + getCompartment(): Compartment
    + getCode(): String

class Compartment:
    - size: Size (small, medium, large)
    - isAvailable: boolean

    + open(): void
    # + close(): void # auto close after certain time
    + getSize(): Size (small, medium, large)
    + isAvailable(): boolean
    + markAsAvailable(): void
    + markAsUnavailable(): void
```

## Step 4: Implementation
- Define the core logic
- Consider the edge cases
```python
class Locker:
    depositPackage(size):
    """
    Core logic:
    1. Find compartment of the right size
    2. Open the compartment
    3. Mark the compartment as unavailable
    4. Generate an access token
    5. Store the access token in the mapping
    6. Return the access token code

    Edge cases:
    1. No compartment of the right size -> throw error
    """
    compartment = _getAvailableCompartment(size)
    if compartment is None:
        raise Exception("No available compartment of right size!")
    compartment.open()
    compartment.markAsUnavailable()
    accessToken = _generateAccessToken(compartment)
    code = accessToken.getCode()
    accessTokensMapping[code] = accessToken
    return code

    _getAvailableCompartment(size):
    """
    Core logic:
    1. Find the first available compartment of the right size
    2. Return the compartment
    Edge cases:
    1. No available compartment of the right size -> return None
    """
    for c in compartments:
        if c.getSize() == size and c.isAvailable():
            return c
    return None

    _generateAccessToken(compartment):
    """
    Core logic:
    1. Generate a random code
    2. Set the expiration date
    3. Return the access token
    """
    code = _generateUniqueCode()
    expiresAt = _generateExpirationTimestamp(7 days)
    return AccessToken(code, expiresAt, compartment)

    pickUpPackage(code):
    """
    Core logic:
    1. Look up the code to get the access token
    2. get the compartment
    3. Open the compartment
    4. Mark the compartment as available
    5. Remove the access token from the mapping

    Edge cases:
    1. Invalid code(empty, null, not found) -> throw error
    2. Expired code(expired time is in the past) -> throw error
    3. Compartment not found -> throw error
    """
    if code is None or code == "":
        raise Exception("Invalid code!")
    accessToken = accessTokensMapping[code]
    if accessToken is None:
        raise Exception("Invalid code!")
    if accessToken.isExpired():
        raise Exception("Expired code!")
        
    compartment = accessToken.getCompartment()
    if compartment is None:
        raise Exception("Compartment not found!")
    compartment.open()
    compartment.markAsAvailable()
    accessTokensMapping.remove(code)

    openExpiredCompartments():
    """
    Core logic:
    1. Open all compartments with expired tokens
    --- remove the package from the compartment
    2. Mark the compartments as available
    3. Remove the access tokens from the mapping? No, as we are showing them as expired. Remove it after 3months+ as per policy.
    """
    for code, accessToken in accessTokensMapping.items():
        if accessToken.isExpired():
            compartment = accessToken.getCompartment()
            compartment.open()
            # assume the empty package is removed from the compartment and auto closed
            compartment.markAsAvailable()
            # accessTokensMapping.remove(code)
    return True

    _generateUniqueCode():
    """
    Core logic:
    1. Generate a random code
    2. Return the code
    """
    return str(uuid.uuid4())
```

## Step 5: Extensibility
"""
1. What if we want to allow a smaller package to use a larger compartment as a fallback when all exact-size compartments are full?
```python
_getAvailableCompartment(size):
    """
    Core logic:
    1. Find the first available compartment of the right size
    2. Return the compartment
    Edge cases:
    3. No available compartment of the right size -> return None
    """
    sizes = [small, medium, large]
    startIndex = sizes.index(size)
    for i in range(startIndex, len(sizes)):
        size = sizes[i]
        for c in compartments:
            if c.getSize() == size and c.isAvailable():
                return c
    return None
```

1. How would you hanlde compartment that are broken or under mentainance? 
```python
enum CompartmentStatus:
    AVAILABLE
    UNAVAILABLE
    BROKEN
    UNDER_MAINTENANCE

class Compartment:
    - size: Size (small, medium, large)
    - status: CompartmentStatus

    + open(): void
    # + close(): void # auto close after certain time
    + getSize(): Size (small, medium, large)
    + isAvailable(): boolean
    + markAsAvailable(): void
    + markAsUnavailable(): void

_getAvailableCompartment(size):
    """
    Core logic:
    1. Find the first available compartment of the right size
    2. Return the compartment
    Edge cases:
    3. No available compartment of the right size -> return None
    """
    for c in compartments:
        if c.getSize() == size and c.isAvailable():
            return c
    return None
```

2. How would you ensure packages are actuallly deposited before generating the access token?
```python
# Two phase commit approach
1. Reserve the compartment & confirm deposit

class Locker:
    - compartments: Compartment[]
    - accessTokensMapping: Map<String, AccessToken>

    # + depositPackage(size: Size): AccessToken | Error
    + reserveCompartment(size: Size): reservationId | Error
    + confirmDeposit(reservationId: String): tokenCode | Error
    + cancelReservation(reservationId: String): void | Error

    + pickUpPackage(accessToken: String): void | Error
    + openExpiredCompartments(): void

class Compartment:
    - size: Size (small, medium, large)
    - status: CompartmentStatus

enum CompartmentStatus:
    AVAILABLE
    UNAVAILABLE
    BROKEN
    RESERVED
    UNDER_MAINTENANCE

reserveCompartment(size):
    """
    Core logic:
    1. Find the first available compartment of the right size
    2. Mark the compartment as reserved
    3. Store the reservation in the mapping
    4. Return the reservation id
    """
    compartment = _getAvailableCompartment(size)
    if compartment is None:
        raise Exception("No available compartment of right size!")
    compartment.markAsReserved()
    compartment.open()
    reservationId = _generateReservationId()
    reservationsMapping[reservationId] = compartment
    return reservationId

confirmDeposit(reservationId):
    """
    Core logic:
    1. Find the reservation by the reservation id
    2. Mark the compartment as unavailable
    3. Generate an access token
    """
    compartment = reservationsMapping[reservationId]
    if compartment is None:
        raise Exception("Invalid reservation id!")
    if compartment.getStatus() != CompartmentStatus.RESERVED:
        raise Exception("Invalid reservation id!")
    
    compartment.markAsUnavailable()
    accessToken = _generateAccessToken(compartment)
    code = accessToken.getCode()
    accessTokensMapping[code] = accessToken
    reservationsMapping.remove(reservationId)
    return code

cancelReservation(reservationId):
    """
    Core logic:
    1. Find the reservation by the reservation id
    2. Mark the compartment as available
    3. Remove the reservation from the mapping
    """
    reservation = reservationsMapping[reservationId]
    if reservation is None:
        raise Exception("Invalid reservation id!")
    if reservation.getStatus() != CompartmentStatus.RESERVED:
        raise Exception("Invalid reservation id!")
    compartment = reservation.getCompartment()
    compartment.markAsAvailable()
    reservationsMapping.remove(reservationId)
    return True
```

