# Python3 program to find minimum
# number of denominations

def findMin(V, limits):
    # All denominations of Turkish Currency
    deno = [1, 5, 10, 25, 50,
            100, 500, 1000, 2000, 5000, 10000, 20000]
    n = len(deno)

    # Initialize Result
    ans = []

    # Create a table to store results of subproblems
    dp = [float('inf') for _ in range(V+1)]
    dp[0] = 0

    # Traverse through all denominations
    for i in range(n):
        for j in range(V+1):
            if j >= deno[i]:
                # Find the minimum number of denominations needed
                dp[j] = min(dp[j], dp[j-deno[i]]+1)

    # Traverse through all denominations in reverse order
    i = n - 1
    while i >= 0 and V > 0:
        # Find denominations
        while (V >= deno[i] and limits[i] > 0):
            V -= deno[i]
            limits[i] -= 1
            ans.append(deno[i])

        i -= 1

    # Print result
    for i in range(len(ans)):
        print(ans[i]/100, end=" ")

"""# Driver Code
if __name__ == '__main__':
    n = 60100
    limits = [10, 5, 10, 5, 10, 5, 10, 5, 1, 1, 1, 5]
    print("Following is minimal number",
          "of change for", n/100, ": ", end="")
    findMin(n, limits)"""

# This code is contributed by
# Nurbek-Juraev

import time
import matplotlib.pyplot as plt

# All denominations of Turkish Currency
deno = [1, 5, 10, 25, 50, 100, 500, 1000, 2000, 5000, 10000, 20000]
n = len(deno)

# Array to store running times
running_times = []

# Array to store input sizes
input_sizes = []

# Measure running time for different input sizes
for i in range(10, 1910, 10,):
    V = i * 100
    limits = [10, 5, 10, 5, 10, 534, 10, 5, 1, 1, 0, 5]

    start_time = time.time()
    findMin(V, limits)
    end_time = time.time()

    running_times.append(end_time - start_time)
    input_sizes.append(i)

# Plot the running times
plt.plot(input_sizes, running_times)
plt.xlabel('Input size (V)')
plt.ylabel('Running time (seconds)')
plt.show()
