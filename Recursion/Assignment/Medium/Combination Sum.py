# https://leetcode.com/problems/combination-sum/

# Time O() | Space O()
def CombinationSum(candidates, target):
    comb = []
    getallCombination(target, candidates, [], 0, comb)
    return comb

def getallCombination(self, target, candidates, cur, idx, comb):
    if target == 0:
        comb.append(cur)
        return 
    
    if target < 0:
        return
    
    for i in range(idx, len(candidates)):
        val = candidates[i]
        getallCombination(target - val, candidates, cur + [val], i, comb)



# Here we are not printing every possible combinations for a target ..ie..
# if target = 7 then we only show any one of these [2, 2, 3],[3, 2, 2], [2, 3, 2]
# if we want to get all the above three as a result just dont pass the index so we can get all the possible ways