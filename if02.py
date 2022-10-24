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
    if a<b:
        if a<c:
            return a
        else:
            return c
    else:
        if c<b:
            return c
        else:
            return b
print(main(7,-7,3))