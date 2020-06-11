class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Linear search
        # Time: O(n * min(n, k))
        # Space: O(1)
        
        # Dictionary
        # Time: O(n)
        # Space: O(n)
        d = {}
        n = len(nums)
        for i in range(n):
            if nums[i] not in d:
                d[nums[i]] = i
            else:
                if i - d[nums[i]]  <= k:
                    return True
                else:
                    d[nums[i]] = i
        return False
            