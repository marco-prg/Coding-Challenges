# Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.
# You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement.
# You could assume there always exists an answer.

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d = { v : k for k,v in enumerate(list1) }
        d = { v : k + d[v] for k,v in enumerate(list2) if v in d.keys() }
                
        return [ v for v in d.keys() if d[v] == min(d.values()) ]


# Array - Hash Table - String