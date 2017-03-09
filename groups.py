11:00 AM to 1:00 PM A
12:00 noon to 2:00 PM B
1:30 PM to 2:30 PM C
3:00 PM to 4:00 PM D
3:30 PM to 5:00 PM E
6:00 PM to 7:00 PM F

input: list [A, B, C, D, E, F]
output: list of lists [[A, B, C], [D, E], [F]]
'''

[[[1100, 1300], [1200, 1400], [1330, 1430]], [[1500, 1600], [1530, 1700]], [[1800, 1900]]]

## 1100,1200]
## Python
schedule =[ [1100,1300], [1200,1400],[1330,1430],[1500,1600],[1530,1700],[1800,1900]]

class 

def checkOverlap(item,slot):
    if slot[0] < item[1] :  # it is an overlap
        return True
    return False    # it is not an overlap
    
def belongs(slot,group):
    if len(group) == 0 :
        return True
    # Assumption : Sorted in increasing order of start time i.e. the first time in the slot
    #  slot would be always later in time than any other slots in the group
    #lenG = len(group)
    for item in group:
        result = checkOverlap(item,slot)
        if result == True :
            return True
    return False
    

def generateGroups(list1):
    result = []
    items = len(list1)
    group = []
    for slot in list1:
    ## if group is empty
        if belongs(slot,group):
            group.append(slot)
        else :
            result.append(group)
            group = [slot]
    if len(group) > 0 :
        result.append(group)
    return result
            


print generateGroups(schedule)

