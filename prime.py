flag =True
def prime(num):
    global flag
    for i in range(2,num):
        if num%i==0 :
            flag = False
            break
        else:
            flag= True   
a=int(input("enter a number"))
prime(a)

if flag == True :
    print(f"{a} is a prime")
else:
    print(f"{a} is not a prime")       

        

