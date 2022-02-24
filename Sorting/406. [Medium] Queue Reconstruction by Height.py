# You are given an array of people, people, which are the attributes of some people in a queue (not necessarily in order).
# Each people[i] = [hi, ki] represents the ith person of height hi with exactly ki other people in front who have a height greater than or equal to hi.
# Reconstruct and return the queue that is represented by the input array people. The returned queue should be formatted as an array queue, 
# where queue[j] = [hj, kj] is the attributes of the jth person in the queue (queue[0] is the person at the front of the queue).

class Solution:
    # Time complexity = O(n^2)
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort()
        output = [(-1, -1)] * len(people)
        
        for p in people:
            # i is the pointer, s is the current number of taller people encountered
            i = s = 0
            
            # not enough taller people met or current position already filled
            while s < p[1] or output[i][0] != -1:
                # empty position or position filled by person with same height (greater than or equal to hi)
                if output[i][0] == -1 or output[i][0] == p[0]:
                    s += 1          # increment taller people counter
                i += 1              # increment pointer
            
            # fill position
            output[i] = p
        
        return output
    

    # Time complexity = O(n^2) (faster)
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # sorting people by height in descending order, then by taller counter in ascending order for people with the same height
        # so that we can build res by using the taller counter as insertion index
        # -> for every person p, you will have exactly p[1] people with a height greater or equal to p[0]
        people = sorted(people, key = lambda x: (-x[0], x[1]))
        res = []
        for p in people:
            res.insert(p[1], p)
        return res


# Array - Greedy - Sorting