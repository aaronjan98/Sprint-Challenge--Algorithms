#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) time complexity because there’s a while loop that iterates through all the input values (in the worst case) and performs an operation per value. O(c) space complexity because there’s only one variable that stores one value regardless of how many inputs there are and regardless if the variable gets reassigned with every element of the iteration.

b) O(n*log(n)) time complexity. O(n) part because each input item will be iterated at least once with the for loop; and, log(n) because the number of times that each item fits the while loop condition decreases in half as the variable j increase by double every iteration. O(c) space complexity because no matter the input size, there is always going to be just two variables taking up the same amount of memory.

c) O(n) time complexity because each item of the input will be iterated through with the recursion calls. O(c) space complexity because no matter the input size, one value will be returned.

## Exercise II

The input, n-stories will be sorted from the ground floor to the building’s highest floor. We can take advantage of this ordering by implementing a binary search algorithm. First we’ll drop the egg at the midway point: n/2 and depending if the egg breaks or not we’ll drop it from a higher or lower point. If the egg didn’t break we would through the next egg from (n-n/2)/2, the next half way point to the top from the last floor position. We’ll keep going until we find the value of f. The runtime complexity is O(log(n)).
