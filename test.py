"""
Write a function which takes 2 parameters: an array of whole numbers and an integer X.

The function should look for pairs of numbers in the array which sum to X. Each array element can only be used in one pair. The function should return the count of how many such pairs it finds.

You may assume that the array passed to the function has already been sorted in ascending order.

State any assumptions or design choices you have made
"""

def count_pair(arr, x):
    # take distinct values from the list
    arr = list(set(arr))
    n = len(arr)

    # initilise a counter to count pairs
    count = 0

    for i in range(0, n):
        for j in range(i + 1, n):
            if (arr[i] + arr[j] == x):
                # increment counter for each pair found to be equal to number provided
                count += 1
    
    print(f"Output: {count}")
 
 
if __name__ == "__main__":
    X = 10
    Array = [2, 6, 7, 1, 8, 3]
    count_pair(Array, X)
