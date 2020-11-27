import numpy as np

def openDoors(n):
  loop = np.full(n, True)
  doors = np.full(n, True)
  openDoorsArr = []
  totalOpenDoors = 0
  count = 2
  
  while count <= n:
    for index, val in enumerate(loop, start=1):
      if index%count == 0:
        if doors[index-1] == True:
          doors[index-1] = False
        else:
          doors[index-1] = True
    count+=1

  for index, val in enumerate(doors, start=1):
    if val == True:
      openDoorsArr.append(index)
      totalOpenDoors+=1

  return totalOpenDoors, openDoorsArr

print(openDoors(18))