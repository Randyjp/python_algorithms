# given a sorted array, find the range of a given number.

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        a_len = len(A)
        if a_len < 1:
            return [-1, -1]
        elif a_len == 1 and A[0] == B:
            return [0, 0]
        elif a_len == 1 and A[0] != B:
            return [-1, -1]
        if self.find(A, B, 0, a_len-1) > -1:
            low = self.find_lower(A, B, 0, a_len-1)
            high = self.find_higher(A, B, 0, a_len-1)

            return [low, high-1]
        return [-1, -1]

    def find_lower(self, arr, key, low, high):
        if low > high:
            return low
        mid = low + ((high - low) >> 1)
        mid_val = arr[mid]

        if mid_val >= key:
            return self.find_lower(arr, key, low, mid - 1)
        else:
            return self.find_lower(arr, key, mid + 1, high)

    def find_higher(self, arr, key, low, high):
        if low > high:
            return low
        mid = low + ((high - low) >> 1)
        mid_val = arr[mid]

        if mid_val > key:
            return self.find_higher(arr, key, low, mid - 1)
        else:
            return self.find_higher(arr, key, mid + 1, high)


    def find(self, arr, key, low, high):
        if low > high:
            return -1

        mid = low + ((high - low) >> 1)
        mid_val = arr[mid]

        if mid_val == key:
            return mid

        if mid_val < key:
            return self.find(arr, key, mid+1, high)
        else:
            return self.find(arr, key, low, mid-1)



# testing code
A  = [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10 ]

sol = Solution()
print(sol.searchRange(A, 10))