#Given a string s, return the longest palindromic substring in s.
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        Finds the longest palindromic substring in s.
        """

        # Edge case: if the string has only one character, return it directly
        if len(s) == 1:
            return s

        # Initialize the longest palindrome found so far
        longestPalindrome = ""

        # Helper function to check if a string is a palindrome
        def isPalindrome(sub):
            # Check if string is equal to its reverse
            return sub == sub[::-1]

        # Helper function to find the longest palindrome starting from index 0
        def palindromeLength(sub):
            l = len(sub)
            currentPalindrome = ""  # initialize current palindrome
            for count in range(l + 1):  # check all prefixes of sub
                if isPalindrome(sub[:count]):
                    currentPalindrome = sub[:count]  # update if palindrome found
            return currentPalindrome

        # Main loop: check all substrings starting at each index
        for count in range(len(s)):
            temp = palindromeLength(s[count:])  # longest palindrome starting at s[count:]
            
            # Update longestPalindrome if a longer one is found
            if len(temp) > len(longestPalindrome):
                longestPalindrome = temp    
            
            # Optimization: if remaining string cannot produce longer palindrome, return early
            if len(longestPalindrome) >= (len(s) - count):
                return longestPalindrome  

        return longestPalindrome


# I completed the challenge all by myself! The time complexity isn't the greatest however as it's my first leetcode challenge I am happy to do it with no assistance.
