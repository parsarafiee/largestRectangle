

def getmaxrec(arr):
    maxrec=0
    for i in range(len(arr))  :
        minarr= arr[i]
        for j in range(i,len(arr)):
            minarr = min(minarr,arr[j])
            curarea = (j-i+1)*minarr
            maxrec = max(curarea ,maxrec)
    return maxrec





def sum_arrays(array_num1,array_num2):
    sumarray = []
    for i in range(len(array_num1)):
        if array_num2[i]==0:
            sumarray.append(0)
        else:
            sumarray.append(array_num1[i]+array_num2[i])



    return sumarray

def main (my_array):

    maxrectangl=getmaxrec(my_array[0])
    sumarrayonload=my_array[0]
    for i in range(len(my_array)-1):
        sumarrayonload=sum_arrays(sumarrayonload,my_array[i+1])
        maxrecinhere = getmaxrec(sumarrayonload)
        maxrectangl=max(maxrecinhere,maxrectangl)

    print(maxrectangl)



array1= [[0,0,1,0,1],
           [1,0,1,1,1],
           [1,1,1,1,1],
           [1,1,1,1,1],
           [1,1,1,1,1],
           [0,1,1,1,1]]

main(array1)