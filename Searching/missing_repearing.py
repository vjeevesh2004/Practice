'''
Given an unsorted array of size n.
Array elements are in the range of 1 to n.
One number from set {1, 2, …n} is missing
and one number occurs twice in the array. 
Find these two numbers.
'''
def findmissingrepeating(arr):
    n = len(arr)
    S = (n * (n + 1)) // 2  # Sum of first n natural numbers
    S_sq = (n * (n + 1) * (2 * n + 1)) // 6  # Sum of squares of first n natural numbers

    actual_sum = sum(arr)
    actual_sq_sum = sum(x * x for x in arr)

    # Compute the differences
    sum_diff = S - actual_sum  # x - y
    sq_sum_diff = S_sq - actual_sq_sum  # x^2 - y^2

    # Solving for x (missing) and y (repeating)
    missing = (sum_diff + sq_sum_diff // sum_diff) // 2
    repeating = missing - sum_diff

    print(f"The missing number is {missing} and the repeating number is {repeating}")

# Test the function
arr = [4, 3, 6, 2, 1, 6, 7]
findmissingrepeating(arr)
