# Monotone Stack

A **Monotone Stack** is a data structure used to solve problems involving arrays and sequences by maintaining a stack with elements that are either strictly increasing or strictly decreasing. This structure is efficient for finding the next greater or smaller element in a sequence, optimizing over brute-force methods.

## Key Concepts of Monotone Stack

1. **Monotonicity**: 
   - The stack maintains a strictly increasing or strictly decreasing order of elements:
     - **Increasing Stack**: Elements are in ascending order.
     - **Decreasing Stack**: Elements are in descending order.

2. **Efficient Lookups for Next Greater or Smaller Element**:
   - Monotone stacks allow efficient lookup for the next greater (or smaller) element by popping elements from the stack until the top of the stack meets the required condition.
   - This eliminates the need to re-evaluate previously checked elements, making the approach more efficient than brute-force.

3. **Usage Pattern**:
   - Traverse the array.
   - For each element, compare it with the top of the stack.
   - If the current element meets the condition (greater or smaller), pop elements from the stack and perform operations based on index differences (e.g., recording distances).
   - Push the current element and its index onto the stack.

4. **Time Complexity**:
   - Each element is pushed and popped from the stack at most once, resulting in **O(N)** time complexity.

5. **Space Complexity**:
   - The stack uses **O(N)** space in the worst case, where all elements might end up in the stack.

## Practical Applications

- **Next Greater Element Problems**: Efficiently finding the next greater or smaller element for each position in an array (e.g., stock span problems, daily temperatures).
- **Histogram Problems**: Calculating the largest rectangle in a histogram.
- **Sliding Window Problems**: When combined with other techniques, monotone stacks can optimize certain sliding window problems.

---

## Example: Daily Temperatures Problem

In the **Daily Temperatures** problem, a **Descending Stack** is used to efficiently calculate the days until a warmer temperature for each day.

1. **Stack Initialization**: Create a descending stack to store temperatures in decreasing order.

2. **Processing Each Temperature**:
   - For each temperature, check if it’s warmer than the temperature at the top of the stack.
   - If so, pop from the stack and calculate the distance between indices to find how many days until a warmer temperature.

3. **Result Array**:
   - This approach fills an array with the days until a warmer temperature appears, achieving an **O(N)** solution.

This method allows for efficient lookup and updates without redundant checks, making it optimal for this type of problem.