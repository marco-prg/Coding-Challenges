# Jesse loves cookies and wants the sweetness of some cookies to be greater than value k.
# To do this, two cookies with the least sweetness are repeatedly mixed. This creates a special combined cookie with:
#
# sweetness = (1 * Least sweet cookie + 2 * 2nd least sweet cookie).
#
# This occurs until all the cookies have a sweetness >= k.
# Given the sweetness of a number of cookies, determine the minimum number of operations required. If it is not possible, return -1.

from heapq import heappop, heappush

def cookies(k, A):
    A.sort()
    minimum = A[0]
    count = 0
    
    while len(A) > 1 and minimum < k:
        x = heappop(A)
        y = heappop(A)
        z = x + 2*y
        heappush(A, z)
        minimum = A[0]
        count += 1
    
    return count if minimum >= k else -1


# Sorting - Heap (Priority Queue)