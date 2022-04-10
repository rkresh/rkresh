subtaskId = 2
growthRate = [10,10,10,10,50,50,50,50,250,250,250,250,1250,1250,1250,1250,6250,6250,6250,6250]

# Dont change anything above this line
# ===================================

# enter your username for EVERY file you submit
username = "MWS_USERNAME"

# generate your solution as a list
queue = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# ====================================
# Dont change anything below this line

from collections import deque

solution = deque()
# add each element to the solution
for i in queue:
    solution.append(i)

import bamboo

# records your solution
bamboo.calculateRatio(growthRate, solution, username, subtaskId)
