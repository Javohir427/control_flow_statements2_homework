from cmath import e
from tkinter import E


def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    a = n%10
    b = n%100//10
    c = n%1000//100
    d = n%10000//1000
    e = n//10000

    if a>b and  a>c and a>d and a>e:
        return 1
    if b>a and b>c and b>d and b>e :
        return 2
    if c>a and c>b and c>d and c>e:
        return 3
    if d>a and d>b and d>c and d>e:
        return 4
    if e>a and e>b and e>c and e>d:
        return 5

     
print(main(76514))

