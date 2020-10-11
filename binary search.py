def binary(value,lst):
    i = 0
    n = len(lst)
    j = n
    while i < j:
        m = (i+j)//2
        if value > lst[m]:
            i = m+1
        else:
            j = m
    if value == lst[i]:
        print('your value is on location ', i)
    else:
        print('value not found')
value = int(input('enter value to find '))
lst = [12,34,56,78,90]
binary(value,lst)
