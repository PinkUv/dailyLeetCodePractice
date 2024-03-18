# 136. Single Number (March 17th, 2024)
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

# Sort-While
For my first, and most ineffective approach, I opted for a while loop sort brute force.
I iterated through the list and sorted it using standard python's built-in sorting function. Then, I checked each pair of elements to see if they equalled one.

There are a few issues I had with this solution
- Complexity (solved in o(nlongn))
- Sort, sorting isn't nessecary as there are sort-free solutions
- Clarity

For a better, but still not ideal solution i opted for,

# collections.Counter 
Using the counter function from Collections I pass the list of nums into the function and then iteratre the list to find the single case.

While this is a faster and more readable solution, it's still very *pythonic* and may not be accepted in interviews

So for my last approach,

# XOR Bit Manipulation
Using XOR, if both numbers are the same the values will cancel themselves out leaving only the single number.

This solution is both fast and low-space without an external library making this my best solution.