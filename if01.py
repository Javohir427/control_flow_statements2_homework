def main(a,b,c):
    """
    Find the largest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a>b and a>c:
        return ('First number')
    if b>a and b>c:
        return ('Second number')
    if c>a and c>b:
        return ('Third number')
print(main(7,9,3))  