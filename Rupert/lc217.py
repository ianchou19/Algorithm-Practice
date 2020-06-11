class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Set
        # Time: O(n)
        # Space: O(n)
        s= set()
        for n in nums:
            if n in s:
                return True
            else:
                s.add(n)
        return False
        
        # Sorting
        # Time: O(nlogn)
        # Space: O(1)