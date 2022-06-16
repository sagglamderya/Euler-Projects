#What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?
import numpy as np
f = open("Problem-11txt.txt", "r")
x=(f.read()).split()
arr=(np.array(x, dtype=int)).reshape(20,20)
k=1
for i in range(19):
    for j in range(19):
        try: 
            
            hor=(arr[i,j]*arr[i,j+1]*arr[i,j+2]*arr[i,j+3])
            if hor>k:
                k=hor
            prep=(arr[i,j]*arr[i+1,j]*arr[i+2,j]*arr[i+3,j])
            if prep>k:
                k=prep
            cross1=(arr[i,j]*arr[i+1,j+1]*arr[i+2,j+2]*arr[i+3,j+3])
            if cross1>k:
                k=cross1
            cross2=(arr[i,j]*arr[i+1,j-1]*arr[i+2,j-2]*arr[i+3,j-3])
            if cross2>k:
                k=cross2              
        except IndexError:
            pass
print(k)



