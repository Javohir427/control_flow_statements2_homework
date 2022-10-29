def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a>=b and b>=c or a<=b and b<=c:
        return ('Second number')
    if b>=a and a>=c or b<=a and a<=c:
        return ('First number')
    if a>=c and c>=b or a<=c and c<=b:
        return ('Third number')
print (main(5,5,3))