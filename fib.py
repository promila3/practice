# 0 1(1) 1(2) 2(3) 3(4) 5 8 13
# Straightforward approach to it. Running time O(2^n)
# Promila Agarwal 
def fib(n):
    if n <= 0:    # error/Boundary condition
        return 0
    if (n == 1) or (n == 2) :  ## Boundary condition
        return 1
    return fib(n-1) + fib(n-2)

## Memoization/Dynamic Programming approach
## Declare an array memo[n]

### O(n) 

def fibDP(n,memo):
    #global memo
    #print memo
    if n <= 0 :
        return 0
    if memo[n-1] == 0 :
        memo[n-1] = fibDP(n-1,memo) + fibDP(n-2,memo)  # gives me my result here
        
    return memo[n-1]

def fib2(n):
    memo = [ 0 for _ in range(n)]  ## 0 to n-1  indices 
    memo[0] = 1
    memo[1] = 1
    return fibDP(n,memo)
    
    
print fib(7)
memo=[]
print fib2(7)
    
    
