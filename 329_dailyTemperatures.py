from typing import *

class Solution:
    """
    Approaches:
        * Brutal Force: For each num in temperatures, just iterate through each of its following
        nums in the list and find the number that is large than it and record the distance.
        
        Time Complexity: O(N^2)
        Space Complexity: O(1)

        * Descending Stack: Create a stack that will add (num[i], i) to the stack. While iterating
        thought the list, we pop out item(s) the top of stack while num[i] is greater than stack.peek()
        and record distance of between the popped num and the num[i] with the poped index and i. After 
        the iteration any remaining items in the stack means that they can't find a larger num in such list

        Time Complexity: O(N)
        Space complexity: O(N)
    """
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        desc_stack: List[Tuple[int, int]] = []
        result_arr: List[int] = [0] * len(temperatures)
        for index, num in enumerate(temperatures):
            while len(desc_stack) > 0 and desc_stack[len(desc_stack) - 1][0] < num:
                _, old_index = desc_stack.pop()
                result_arr[old_index] = index - old_index
            desc_stack.append((num, index))
        return result_arr
        