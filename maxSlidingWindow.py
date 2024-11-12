from collections import deque
from typing import *

class Solution:
    """
    Monotone Queue:
        Create a descending queue that for a new element intended to be added it will pop out
        any elements in the queue that is smaller than it and push_back this item. Whatever is 
        at the bottom will be the max of the sliding window. Also the index of the element will
        be saved as well.

        If sliding window moves and the larges element is index is not within it, this element 
        will be removed.

        Such algorithem ensures that the maximum and potential following ones are always prepared 
        and if current maximum is shifted out, the following ones will take its place. Any newly 
        element will invalidate any element in the queue that is smaller than it.

        Time Complexity: O(N)
        Space Complexity: O(k) --- The queue will never be larger than the size of the sliding window
    """
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Assume all inputs are valid and validation logic will be skipped here.
        
        # The decending queue will keep tuple of (index, num).
        descending_queue: List[Tuple[int, int]] = deque([])
        def queue_add(index, num):
            while len(descending_queue) > 0 and num > descending_queue[len(descending_queue) - 1][1]:
                descending_queue.pop()
            descending_queue.append((index, num))
        
        # Remove the larges item if its index is less than the new left window
        def queue_remove(left_window_index: int):
            if descending_queue[0][0] < left_window_index:
                descending_queue.popleft()

        # We will shift right window from 0 to k - 1 inclusive
        for right_window in range(k):
            queue_add(right_window, nums[right_window])

        result_arr: List[int] = [descending_queue[0][1]]
        # Then lets shift the entire window from k to len(descending_queue) - 1 inclusive
        for right_window in range(k, len(nums)):
            left_window = right_window - k + 1
            queue_add(right_window, nums[right_window])
            queue_remove(left_window)
            result_arr.append(descending_queue[0][1])
        
        return result_arr
        
nums = [1,3,-1,-3,-4,3,6,7]
k = 3
print(Solution().maxSlidingWindow(nums, k))