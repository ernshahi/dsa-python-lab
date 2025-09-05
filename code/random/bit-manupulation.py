"""
Bit Manipulation

https://www.youtube.com/watch?v=6HGKvFLAPNc
2749. Minimum Operations to Make the Integer Zero
"""
num = 10

print(num)
print(num.bit_count())
print(num.bit_length())

print(bin(num))
print(hex(num))
print(oct(num))

print(int('0b1010', 2))
print(int('0o12', 8))
print(int('0xa', 16))