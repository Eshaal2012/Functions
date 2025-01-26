
def fibonacci (n):
    a , b=0,1
    count=0
    while count < n:
        print(a, end=':) ')
        a,b=b, a+b
        count +=1

num=int(input("Enter a number:"))
fibonacci(num)