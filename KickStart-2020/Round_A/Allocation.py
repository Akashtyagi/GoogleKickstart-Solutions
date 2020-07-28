# Question: https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d3f56
from collections import defaultdict
test_cases = int(input())
output = []

def xs(x,b):
    out = 0    
    x = sorted(x)
    for item in x:
        if item>b:
            # print(out,passes)
            return out
        else:
            # print(out,passes)
            out+=1
            b = b-item
    return out
    
for _ in range(test_cases):
    z = input().split()
    b = int(z[1])
    cost = [int(i) for i in input().split()]
    output.append(xs(cost, b))
    
for i,o in enumerate(output):
    print("Case #{}: {}".format(i+1, o))
          
          
          
