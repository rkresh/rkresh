subtaskId = 4
growthRate = [1,1,2,3,5,8,13,21]

# Dont change anything above this line
# ===================================

# enter your username for EVERY file you submit
username = "MWS_USERNAME"

# generate your solution as a list
queue = [0, 1, 2, 3, 4, 5, 6, 7]

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
