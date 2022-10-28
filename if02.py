def main(a,b,c):
    """
    Find the smallest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a<c and b>a:
        return ('First number')
    if a>b and c>b:
        return ('Second number')
    if a>c and b>c:
        return ('Third number')

print(main(8,5,7))