## Big O

1. Omega is best, theta is avg, and omicron is worst case
2. We always look at worst case. There is only worst case big o. 
3. Drop the constants. So, `O(2n)` is actually `O(n)`
4. Drop non-dominant terms. So, `O(n^2 + n)` is actually `O(n^2)`
5. Wherever the number of elements in your array get halved during search then it will take **`"log of n to the base 2" aka LogN`** steps to search our target element
6. Order: **`O(1) << O(log N) << O(N) << O(N^2)`**
7. Space complexity states how much memory in the worst case is needed at any point in the algorithm.
8. Recursive algos consume high memory as we have to remember numbers in each recursive iteration.
9. Add vs multiply for time complexities. If you have two input parameters like a,b. Then you can have O(a+b) or O(a*b) as the time complexities.