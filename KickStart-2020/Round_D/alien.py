import sys
sys.stdin = open("/home/qainfotech/Akashtyagi/Python_Projects/Misc/Code/input.txt",'r')
sys.stdout = open("/home/qainfotech/Akashtyagi/Python_Projects/Misc/Code/output.txt",'w')

# input = stdin

#Testcases
T = int(input())
output = [0]*T


# Main function
def main(arr,N):
    c = 0
    low = 1
    high = 4
    
    for i in range(1,N):
        diff = arr[i]-arr[i-1]
        if diff>0:
            low+=1
            high = 4
        elif diff<0 :
            low = 1
            high-=1
        if low>4 or high==0:
            c+=1
            low=1
            high = 4
    return c


# Further Inputs
for i in range(T):
    # Second line input
    N = int(input())
    arr = list(map(int, raw_input().split()))
    output[i] = main(arr,N)


for i in range(len(output)):
    print("Case #{}: {}".format(i+1,output[i]))
