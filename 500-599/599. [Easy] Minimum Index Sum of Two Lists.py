# Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.
# You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement.
# You could assume there always exists an answer.

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict1 = { v : k for k,v in enumerate(list1) }
        dict2 = { v : k + dict1[v] for k,v in enumerate(list2) if v in dict1.keys() }
                
        return [ v for v in dict2.keys() if dict2[v] == min(dict2.values()) ]