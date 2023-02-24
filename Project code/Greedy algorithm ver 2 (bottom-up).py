# Python3 program to find minimum
# number of denominations

def findMin(V):
    # All denominations of Turkish Currency
    deno = [1, 5, 10, 25, 50,
            100, 500, 1000, 2000, 5000, 10000, 20000]
    n = len(deno)

    # Initialize Result
    ans = []

    # Traverse through all denomination
    i = 0
    while (i < n):

        # Find denominations
        while (V >= deno[i]):
            V -= deno[i]
            ans.append(deno[i])

        i += 1

    # Print result
    for i in range(len(ans)):
        print(ans[i]/100, end=" ")


# Driver Code
if __name__ == '__main__':
    n = 9387
    print("Following is minimal number",
          "of change for", n/100, ": ", end="")
    findMin(n)

# This code is contributed by
# Nurbek-Juraev