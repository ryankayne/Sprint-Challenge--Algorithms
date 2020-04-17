# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```
Time: O(n)
Space: O(1)

As n increases, the amount of time to do operations also increase, but by a steady amount. For every 1 integer you increase, the steps involved increase by 2. That's linear.

And space is constant because there is no increase in space depending on how big the number is, it just uses one slot of memory.

```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```
Time: O(n^2)
Space: O(1)

As n increases, the time for operations also increases, but not in a consistent fashion. Regardless, time is increasing the time needed to process in an exponential fashion in relation to n, not to the previous time which I was at first thinking. The space is constant though, since every iteration takes up the same amount of space for variables i, sum, j, and n.


```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```
Time: O(n)
Space: O(n)

As n increases, the time increase in a linear fashion. As n increases by an integer, an additional 4 steps are added to the process. In terms of space, the stack grows at a consistent rate during calculations as n increases so that relationship is also linear.

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.
