"""
Leetcode 359. Logger Rate Limiter

Design a logger system that enforces a 10-second rate limit per unique message. The shouldPrintMessage(timestamp, message) method should return true if the message hasn't been printed in the last 10 seconds, otherwise false. For example, if "foo" is logged at timestamp 1, it can't be logged again until timestamp 11 or later.

Input:

shouldPrintMessage(1, "foo") → true
shouldPrintMessage(2, "bar") → true
shouldPrintMessage(3, "foo") → false
shouldPrintMessage(8, "bar") → false
shouldPrintMessage(10, "foo") → false
shouldPrintMessage(11, "foo") → true
Output:

true, true, false, false, false, true

Explanation: "foo" at timestamp 1 blocks until 11. "bar" at timestamp 2 blocks until 12. Requests within the 10-second window return false.

Constraints:

Timestamps are in seconds and arrive in chronological order
Multiple unique messages can be tracked simultaneously
Each message has an independent 10-second window

"""

class Logger:
    def __init__(self):
        self.message_timestamps = {}
        
    # shouldPrintMessage(1, "foo") → true
    def shouldPrintMessage(self, timestamp, log):
        if log in self.message_timestamps:
            last_time = self.message_timestamps[log]
            if timestamp - last_time < 10:
                return False
        self.message_timestamps[log] = timestamp
        return True
    

from collections import deque
import time

class Logger:

    def __init__(self):
        self.queue = deque()  # (timestamp, message)
        self.messages = set()

    def shouldPrintMessage(self, timestamp, message):
        # Remove old messages
        while self.queue and timestamp - self.queue[0][0] >= 10:
            old_time, old_msg = self.queue.popleft()
            self.messages.remove(old_msg)

        # Check if message exists
        if message in self.messages:
            return False

        # Add new message
        self.queue.append((timestamp, message))
        self.messages.add(message)
        return True