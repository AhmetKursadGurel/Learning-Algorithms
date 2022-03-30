def bubbleSort(arr):
    
    n = len(arr)
    for i in range(n-1):
        print("Current list: ", arr)
        print("We will go up to index", (n - (i+2)))
        for j in range(0, n-i-1):

            print(" Comparing " + str(arr[j]) + "(" + str(j) + ") and " + str(arr[j + 1]) + "(" + str(j+1) + ")")
            if arr[j] > arr[j + 1] :
                print("  Swap ", arr[j], " and", arr[j + 1])
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print("  List becomes: ", arr)

        