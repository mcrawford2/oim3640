# Count by using get
def histogram(s):
    """Return a dictionary that contains the count of each character in s."""
    d = {}
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d

result = histogram('bookkeeper')
print(result['o'])
print(result.get('o', 0))
print(result.get('z', 0))