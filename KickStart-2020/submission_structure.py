import sys
sys.stdin = open("/home/qainfotech/Akashtyagi/Python_Projects/Misc/Code/input.txt",'r')
sys.stdout = open("/home/qainfotech/Akashtyagi/Python_Projects/Misc/Code/output.txt",'w')

# input = stdin

#Testcases
T = int(input())
output = [0]*T


# Main function
def main(arr,N):
    pass




# Further Inputs
for i in range(T):
    # Second line input
    N = int(input())
    arr = list(map(int, raw_input().split()))
    output[i] = main(arr,N)


for i in range(len(output)):
    print("Case #{}: {}".format(i+1,output[i]))


testcases = [
    # nums,  b,  expeected result
    [[3,2,1],3,1],
    [[1,2,1,2],1,1],
    [[0],1,1],
    [[4,3,2,1,1],4,1],
    [[4,3,2,4],4,1],
    [[],0,0],
    [[1,2,1,5,2,3,9,7],1,3]
    ]


for i in testcases:
    nums = i[0]
    k = i[1]
    exp = i[2]
    res = c(nums,len(nums))
    print(res,exp==res)
    
