/* Promila Agarwal */
lst = [1, 0, 4, 9]
target = 13

def find_indices1(lst, target): #-> Returns a pair of indices that sum to target (2, 3)
    ## O(n^2)
    lenList = len(lst)
  
    for i in range(lenList-1): 
        for j in range(i+1, lenList):
            if ( (lst[i] + lst[j]) == target) :
                return i, j
          
    return -1, -1  # I was not able to find matching pair, I return -1, -1
  
    # assuming my list is sorted or I sort it then it would like this  n lg (n) [0,1,4,9]
    #  this can be definitenely be split up using binary search ..  target == 1 , anything larger than 1 from this list.. 
lst2 = [0, 1, 2, 4] # target = 4 
    #[0,1,2,2,2,2,2,2,2,2,2,3,3,4] target == 2
  
def find_indices(lst,target):
    lenList = len(lst)
    #lst.sort()
    # Boundary check if len == 0 
    # if len = 1 or if len == 2
    #mid = lenList/2
    
    # if target - the value is in the list or not.. has it been seen or not.. 
    targetMinus = {}  # key being the targetMinus value and the value being the indices.
    
    for i in range(lenList):
        if (target - lst[i] ) in targetMinus :
            return i, targetMinus[target-lst[i]] 
        else :
            if lst[i] in targetMinus :
            #targetMinus[lst[i]].append(i) : 
                pass
            else :
                targetMinus[lst[i]] = i     
                #targetMinus = { 0 : [0], 1 :[1], 2:[2], 
          
    return -1, -1

print find_indices1(lst2,4)
print find_indices(lst2,4)
