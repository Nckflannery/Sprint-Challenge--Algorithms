#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The while loop will run n times, so *O(n)*


b) The for loop will run n times and the while loop is n/2, so *O(n log(n))*


c) *O(n)*

## Exercise II

I would implement a "binary search" method by dropping an egg on the middle floor. Then, if it breaks only look at the floors below and drop one on the middle floor of those floors. If it doesn't break, use the upper floors and drop an egg on the middle floor of those floors. Repeat until we find f.  
The runtime complexity of this would be *O(log(n))*
