
# def factorial(n):
#     if n<=1:
#         return 1
#     return n*factorial(n-1)
# print(factorial(5))

# def sum(arr):
#     if len(arr)==0:
#         return 0
#     return arr[0]+sum(arr[1:])
# print(sum(arr=[1,2,3,4,5]))

# def palindrome(str1):
#     if len(str1)==1:
#         return True
#     if str1[0]==str1[-1]:
#         return palindrome(str1[1:-1])
#     return False
# print(palindrome("racecar"))


# def power(base,exponent):
#     if exponent==0:
#         return 1
#     return base*power(base,exponent-1)
# print(power(2,2))
    
# def fibanocci(n):
#     feb=[0,1]
#     for i in range(2,n+1):
#         feb.append(feb[i-1]+feb[i-2])
#     return feb
# print(fibanocci(5))

# def fibonacci_recursion(n):
#     if n<=1:
#         return n
#     return fibonacci_recursion(n-1)+fibonacci_recursion(n-2)
# print(fibanocci(5))



def factorial(n):
    if n<=1:
        return 1
    return n*factorial(n-1)
print(factorial(5))

def sum(arr):
    if not arr:
        return 0
    return arr[0]+sum(arr[1:])
print(sum(arr=[500,80,900,1000]))

def palindrome(str):
    if len(str)<=1:
        return True
    if str[0]!=str[-1]:
        return False
    return palindrome(str[1:-1])
print(palindrome("malayalam"))


def reverse_string(str):
    if str=="":
        return str
    return str[-1]+reverse_string(str[:-1])
print(reverse_string("move on"))


def reverse_array(arr):
    if not arr:
        return []
    return [arr[-1]]+reverse_array(arr[:-1])
print(reverse_array([1,2,3,4,5,6]))


def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(n=6))