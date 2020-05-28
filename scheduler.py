# Homework 6 - Problem 2
# Weighted Interval Scheduling
# By Charles Son and Ashley Ahn

inputjobs = [[1, 2, 94, 1024],
            [2, 7, 14, 273],
            [3, 17, 41, 115],
            [4, 14, 32, 100],
            [5, 51, 93, 478],
            [6, 93, 98, 160],
            [7, 99, 100, 2],
            [8, 33, 40, 14],
            [9, 40, 49, 3],
            [10, 1, 50, 389]
            ]


# step 1: sort jobs by finish time
def sortbyfinishTime(val): 
    return val[2]
inputjobs.sort(key = sortbyfinishTime)  
# print(inputjobs)

# Do not modify!
inputjobs.insert(0, [0,0,0,0]) # dummy 0th item for debugging purposes related to index)

# Step 2: set up memoization array
memo = [0] * (len(inputjobs)) # memoization array : base case with no jobs selected

def latestCompatible(jobs, n):
    for i in reversed(range(n)):
        if jobs[i][2] <= jobs[n][1]:
            return i
    return 0

for i in range(1, len(inputjobs)):
    # print(inputjobs[i])
    memo[i] = max(inputjobs[i][3] + memo[latestCompatible(inputjobs, i)], memo[i-1])
# print ("Memoization array: " + str(memo))
# print ("Max profit from optimal set of jobs: " + str(memo[-1]))

# Step 3: find optimal solution
includedjobs = []

def findSolution(n):
    if (n != 0):
        compatibleIndex = latestCompatible(inputjobs, n)
        if (inputjobs[n][3]+ memo[compatibleIndex] > memo[n-1]): #Case where job j was included (from optimal substructure)
            includedjobs.append(n) # add job index to solution
            findSolution(compatibleIndex)
        else:
            findSolution(n-1)

findSolution(len(memo)-1)

# Step 4: print optimal jobs
includedjobs.reverse()
print ("=============================================================================")
print ("Optimal set of jobs for max profit of " + str(memo[-1]))
for index in includedjobs:
    print ("Job " + str(inputjobs[index][0]) + ": Time (" + str(inputjobs[index][1]) + "-" + str(inputjobs[index][2]) + ") Value:" + str(inputjobs[index][3]))
print ("=============================================================================")