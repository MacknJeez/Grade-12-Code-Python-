def print_prime(x):
    print("List of prime:")
    for i in range(3,x):
        flag=0
        for j in range(3,i):
            if i%j==0:
                flag = 1
        if flag==1:
            continue
        print(i)

print_prime(35)
