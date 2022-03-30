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


recurrence(8
)


