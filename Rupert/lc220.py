import bisect

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        '''
        # Naive linear search => TLE
        # Time: O(n * min(n, k))
        # Space: O(1)
        n = len(nums)
        for i in range(n):
            for j in range(max(0, i-k), i):
                if abs(nums[i] - nums[j]) <= t:
                    return True
        return False
        '''
        
        # Binary search tree - search in log time
        # Time: O(n * log(min(n, k)))
        # Space: O(min(n, k))
        # Use bisect() to maintain a sorted list and faciliate O(logn) lookup
        if t < 0 or k <= 0:
            return False
        
        a = []
        n = len(nums)
        for i in range(n):
            p = bisect.bisect_left(a, nums[i])
            # Check exact duplicate or predecessor
            if p < len(a) and a[p] == nums[i] or p > 0 and abs(nums[i] - a[p-1]) <= t:
                return True
            
            q = bisect.bisect_right(a, nums[i])
            # Check successor
            if q < len(a) and abs(nums[i] - a[q]) <= t:
                return True
            
            # Maintain a window size of k
            if i >= k:
                del a[bisect.bisect_left(a, nums[i-k])]
                
            # Add the current element into list
            bisect.insort(a, nums[i])
          
        return False
            
        '''
        # Bucket - search in linear time
        # Time: O(n)
        # Space: O(min(n, k))
        if t < 0 or k <= 0:
            return False
        
        d = {}
        n = len(nums)
        w = t + 1 # bucket size
        for i in range(n):
            bucket = nums[i] // w
            # Check the bucket that nums[i] belongs to and two neighboring buckets
            if bucket in d or bucket - 1 in d and abs(nums[i] - d[bucket-1]) <= t or bucket + 1 in d and abs(nums[i] - d[bucket+1]) <= t:
                return True
            # Keep a sliding windonw of size k
            if i >= k:
                d.pop(nums[i-k] // w)
            # Add the current element into its bucket
            d[bucket] = nums[i]
        return False
        '''
            
            
        