def linear(value,lst):
    i=0
    n = len(lst)
    while(i<= n and value!=lst[i]):
        i = i+1
    if i <= n:
        location = i
        print('your value is on location ', i)
    else:
        print('value not found')
value = int(input('enter value to find '))
lst = [12,34,56,78,90]
linear(value,lst)
