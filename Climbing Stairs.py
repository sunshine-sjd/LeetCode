'''
ou are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top? 

'''
 
 # 斐那波契数数列
 
def climbStairs(n):
    a,b = 1, 1
    for i in range(2, n+1):
        a, b = b, a+b
    return b
