from collections import deque

csvSplitBy = ","
NUMBER_OF_ITERATIONS = 10000
csvFile = "results.csv"

def writeResults(subtaskId: int, height: int, username: str, csvFile: str) :
    heightString = str(height)
    try:
        file = open(csvFile)
        line = file.readline().strip()
        fields = line.split(sep=csvSplitBy)
        if len(fields) != 6:
            raise
        results = fields[0:6]
    except:
        # ignore, use empty default
        results = ["", "", "", "", "", ""]
    else:
        file.close()
    results[subtaskId] = heightString
    with open(csvFile, 'w') as file:
        file.writelines(username +
                        csvSplitBy + results[1].strip() +
                        csvSplitBy + results[2].strip() +
                        csvSplitBy + results[3].strip() +
                        csvSplitBy + results[4].strip() +
                        csvSplitBy + results[5].strip() + '\n'
        )


def calculateRatio(growthRate, solution: deque, username: str, position: int):
    n = len(growthRate)
    maxHeight = 0
    count = n * [1]
    sumOfGrowthRates = sum(growthRate)
    for i in range(0, NUMBER_OF_ITERATIONS):
        toCut = solution.popleft()
        for j in range(0, n):
            maxHeight = max(maxHeight, count[j] * growthRate[j])
        for j in range(0, n):
            if j == toCut:
                count[j] = 1
            else:
                count[j] += 1
        solution.append(toCut)
    ratio = maxHeight / sumOfGrowthRates
    print("Ratio=" + str(ratio) + " MaxHeight=" + str(maxHeight) + " SumOfGrowthRates=" + str(sumOfGrowthRates))
    try:
        writeResults(position, maxHeight, username, csvFile)
    except:
        print("Could not save result to " + csvFile)

