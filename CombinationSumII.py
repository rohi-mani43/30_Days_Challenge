def combinationSum2(candidates, target):
    candidates.sort()  # sort to handle duplicates
    res = []
    
    def dfs(start, path, total):
        if total == target:  # found valid combination
            res.append(path[:])
            return
        if total > target:  # exceed target → stop
            return
        
        prev = -1  # track duplicate
        for i in range(start, len(candidates)):
            if candidates[i] == prev:  # skip duplicates
                continue
            path.append(candidates[i])
            dfs(i + 1, path, total + candidates[i])
            path.pop()
            prev = candidates[i]
    
    dfs(0, [], 0)
    return res


# Input
n = int(input())
candidates = list(map(int, input().split()))
target = int(input())

print(combinationSum2(candidates, target))
