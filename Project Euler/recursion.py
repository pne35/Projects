def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)
    
def naturalSum(n):
    if n<= 1:
        return 1
    else:
        return n + naturalSum(n - 1)
    
def fibonacci(ls,n):
    if len(ls) <= 1:
        ls = [1,1]
    if len(ls) >= n:
        return ls
    else:
        ls.append(ls[-1] + ls[-2])
        return fibonacci(ls, n)
    
def power(a,b):
    if b <= 1:
        return a
    else:
        return a * power(a, b - 1)
    
def palindrome(w):
    if len(w) <= 1:
        return True
    if w[0] == w[-1]:
        return palindrome(w[1:-1])
    return False

def HCF(a,b):
    if b == 0:
        return a
    else:
        return HCF(b, a % b)
    
def reverse(s):
    if len(s) <= 0:
        return s
    return reverse(s[1:]) + s[0]

def hanoi(n, a, b, c):
    if n <= 1:
        print(f"Move disk 1 from {a} to {c}")
        return 
    else:
        hanoi(n - 1, a , c ,b)
        print(f"Move disk {n} from {a} to {c}")
        hanoi(n - 1, b, a ,c)

def digits(s,c):
    s = str(s)
    if len(s) <= 1:
        return c + 1
    else:
        return digits(s[1:], c + 1)
    
def count_paths(x, y, paths):
    if n == 2

paths = []

# print(factorial(5))
# print(naturalSum(30))
# print(fibonacci([1,2],10))
# print(power(2,5))
# print(palindrome("radar"))
# print(HCF(49, 7))
# print(reverse("ead")
# print(hanoi(1,"A", "B", "C"))
# print(digits(1253533,0))
print(count_paths(0, paths))
