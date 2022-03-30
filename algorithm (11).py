

def kitt(n):

    for i in range(0,n):
        rowtoAdd = ""
        for j in range(0, n):
            if i == j:
                rowtoAdd = rowtoAdd + "*"
            else:
                rowtoAdd = rowtoAdd + "="
        print(rowtoAdd)



def str_pattern(n):
    num = int(n)

    for i in range(0,num):
        result = ""
        for j in range(num,i,-1):
            result += str(j)
        print(result)








def recurrence2(n):
   if n == 0:
       return 0
   elif n == 1:
       return 1
   else:
       return(3*recurrence2(n-1)) - (2*recurrence2(n-2))

def recurrence(n):
    result = ""
    for i in range(n):
        result = result + str(recurrence2(i))
        if i < n-1:
            result = result + ","

    print(result)






def manhattan(points):
    sum = 0
    firstItem = points[0]
    indices = (firstItem[0],firstItem[1])

    for item in points:
        for item2  in points:

            item0Sum = item[0] - item2[0]
            item1Sum = item[1] - item2[1]

            if item0Sum < 0:
                item0Sum *= -1

            if item1Sum < 0:
                item1Sum *= -1

            tempSum = item0Sum + item1Sum
            if sum < tempSum:
                sum = tempSum
                indices = (item[0], item2[0])

    return indices


def find_mode(list1):


    list1WithoutDuplicates = []

    # create a new without duplicates
    for i in list1:
        if i not in list1WithoutDuplicates:
            list1WithoutDuplicates.append(i)

    maxOccurence = [0] * len(list1WithoutDuplicates)
    mostOccuredElement = []

    # find occurance of each number from the previous list
    for i in range(0,len(list1WithoutDuplicates)):
        currentNum = list1WithoutDuplicates[i]
        for j in range(0,len(list1)):
            if currentNum == list1[j]:
                maxOccurence[i] += 1

    max = 0
    # get the largest occurance nummber
    for i in range(0,len(maxOccurence)):
        if max < maxOccurence[i]:
            max = maxOccurence[i]

    # find the numbers with the largest occurances & create a list from them
    for i in range(0,len(maxOccurence)):
        if maxOccurence[i] == max:
            mostOccuredElement.append(list1WithoutDuplicates[i])

    return mostOccuredElement

