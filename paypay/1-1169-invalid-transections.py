"""
1169. Invalid Transactions

A transaction is possibly invalid if:

the amount exceeds $1000, or;
if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
You are given an array of strings transaction where transactions[i] consists of comma-separated values representing the name, time (in minutes), amount, and city of the transaction.

Return a list of transactions that are possibly invalid. You may return the answer in any order.

 
Example 1:
Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
Output: ["alice,20,800,mtv","alice,50,100,beijing"]
Explanation: The first transaction is invalid because the second transaction occurs within a difference of 60 minutes, have the same name and is in a different city. Similarly the second one is invalid too.

Example 2:
Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
Output: ["alice,50,1200,mtv"]

Example 3:
Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
Output: ["bob,50,1200,mtv"]
 

Constraints:
transactions.length <= 1000
Each transactions[i] takes the form "{name},{time},{amount},{city}"
Each {name} and {city} consist of lowercase English letters, and have lengths between 1 and 10.
Each {time} consist of digits, and represent an integer between 0 and 1000.
Each {amount} consist of digits, and represent an integer between 0 and 2000.
"""
from collections import defaultdict
from typing import List

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        mapping = defaultdict(list) # name: name, time, amt, city
        invalid = [False] * len(transactions)
        for idx, tx in enumerate(transactions):
            name, time, amt, city = tx.split(",")
            mapping[name].append([idx, name, int(time), amt, city, tx])

        for name, details in mapping.items():
            for i in range(len(details)):
                idx1, name1, time1, amt1, city1, tx1 = details[i]
                if int(amt1) > 1000:
                    invalid[idx1] = True

                for j in range(len(details)):
                    if i == j:
                        continue
                    idx2, name2, time2, amt2, city2, tx2= details[j]
                    if city1 != city2 and abs(time2 - time1) <= 60:
                        invalid[idx1] = True
                        break
        return [ transactions[i] for i in range(len(transactions)) if invalid[i]]