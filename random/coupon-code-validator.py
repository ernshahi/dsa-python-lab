"""
3606. Coupon Code Validator
You are given three arrays of length n that describe the properties of n coupons: code, businessLine, and isActive. The ith coupon has:

code[i]: a string representing the coupon identifier.
businessLine[i]: a string denoting the business category of the coupon.
isActive[i]: a boolean indicating whether the coupon is currently active.
A coupon is considered valid if all of the following conditions hold:

code[i] is non-empty and consists only of alphanumeric characters (a-z, A-Z, 0-9) and underscores (_).
businessLine[i] is one of the following four categories: "electronics", "grocery", "pharmacy", "restaurant".
isActive[i] is true.
Return an array of the codes of all valid coupons, sorted first by their businessLine in the order: "electronics", "grocery", "pharmacy", "restaurant", and then by code in lexicographical (ascending) order within each category.©leetcode


Example 1:
Input: code = ["SAVE20","","PHARMA5","SAVE@20"], businessLine = ["restaurant","grocery","pharmacy","restaurant"], isActive = [true,true,true,true]
Output: ["PHARMA5","SAVE20"]

Explanation:
First coupon is valid.
Second coupon has empty code (invalid).
Third coupon is valid.
Fourth coupon has special character @ (invalid).

Example 2:
Input: code = ["GROCERY15","ELECTRONICS_50","DISCOUNT10"], businessLine = ["grocery","electronics","invalid"], isActive = [false,true,true]
Output: ["ELECTRONICS_50"]

Explanation:
First coupon is inactive (invalid).
Second coupon is valid.
Third coupon has invalid business line (invalid).
©leetcode
"""

import string
from typing import List

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        result = []
        categories = ["electronics", "grocery", "pharmacy", "restaurant"]
        chars = string.ascii_letters + string.digits + '_'
        for cod, bs, status in zip(code, businessLine, isActive):
            is_made_by_chars = all(char in chars for char in cod)
            if status and bs in categories and  len(cod) > 0 and is_made_by_chars:
                result.append((bs, cod))

        result.sort(key=lambda x: (categories.index(x[0]), x[1]))
        return [cod for _, cod in result]
    
    """
    result = []
    categories = ["electronics", "grocery", "pharmacy", "restaurant"]
    valid_chars = set(string.ascii_letters + string.digits + '_')
    
    for c, b, a in zip(code, businessLine, isActive):
        if a and b in categories and len(c) > 0 and all(char in valid_chars for char in c):
            result.append((b, c))  # store both businessLine and code for sorting
    
    # Sort based on category order and then lexicographically by code
    result.sort(key=lambda x: (categories.index(x[0]), x[1]))
    
    # Return only the codes
    return [code for _, code in result]
    """
    
if __name__ == "__main__":
    code = ["SAVE20","","PHARMA5","SAVE@20"]
    businessLine = ["restaurant","grocery","pharmacy","restaurant"]
    isActive = [True, True, True, True]
    print(Solution().validateCoupons(code, businessLine, isActive))  # Output: ["PHARMA5","SAVE20"]

    code = ["GROCERY15","ELECTRONICS_50","DISCOUNT10"]
    businessLine = ["grocery","electronics","invalid"]
    isActive = [False, True, True]
    print(Solution().validateCoupons(code, businessLine, isActive))  # Output: ["ELECTRONICS_50"]
