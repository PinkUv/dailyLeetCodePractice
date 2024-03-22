# 234. Palindrome Linked List
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

# Thought Process
Through intuition, if a palindrome is present then half the list must be a reflection of the other half. So, if we reverse the list and compare both halves they should be equal, if not, a palindrome is not present.

Additionally, this process can be completed faster by starting from the halfway point of the list, for this check we don’t need to reverse the whole list.

# Method
In order to achieve this I define a function *reverse* that reverses the list at the halfway point after iterating through it. Then a while loop compares the values of the reversed list to the original. If they don’t match, there is no palindrome, if they do we continue to iterate through the list until either we end the loop or the values don’t match.

