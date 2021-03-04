def minCost(sample):
    if len(sample) == 2:
        return sum(sample)
    curr = sorted(sample) # nlogn + n-2logn-2
    combo = curr[0] + curr[1]
    curr = curr[2:]
    curr.append(combo)
    return combo + minCost(curr)
