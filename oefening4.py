import random

#def countTargetPairs(lijst, target):
    #aantalparen = 0
    #lengte = len(lijst)
   # for i in range(lengte) and j in range(lengte +1):
    #    if  i < j and i + j < target :
      #      aantalparen = aantalparen + 1
    #return aantalparen

def countTargetPairs(nums, target):
    aantalpairs = 0
    lengte = len(nums)
    for i in range(lengte - 1):
        for j in range(i + 1, lengte):
            if nums[i] + nums[j] < target:
                aantalpairs = aantalpairs + 1
    return aantalpairs

voorbeeld1 = countTargetPairs([-1,1,2,3,1], 2)
print(voorbeeld1)
