# Python3 program to find minimum
# number of denominations

def findMin(V, limits):
    # All denominations of Turkish Currency
    deno = [1, 5, 10, 25, 50,
            100, 500, 1000, 2000, 5000, 10000, 20000]
    n = len(deno)

    # Initialize Result
    ans = []

    # Traverse through all denomination
    i = n - 1
    while (i >= 0):

        # Find denominations
        while (V >= deno[i] and limits[i] > 0):
            V -= deno[i]
            limits[i] -= 1
            ans.append(deno[i])

        i -= 1

    # Print result
    for i in range(len(ans)):
        print(ans[i]/100, end=" ")


# Driver Code
if __name__ == '__main__':
    n = 150.52*100
    limits = [10, 5, 10, 5, 10, 5, 10, 5, 1, 1, 5, 5]
    print("Following is minimal number",
          "of change for", n/100, ": ", end="")
    findMin(n, limits)

# This code is contributed by
# Nurbek-Juraev