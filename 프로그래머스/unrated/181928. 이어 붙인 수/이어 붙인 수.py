def solution(num_list):
    even=''
    odd=''
    for i in num_list:
        if i%2==0:
            even=even+str(i)
        else:
            odd=odd+str(i)
    return int(even)+int(odd)