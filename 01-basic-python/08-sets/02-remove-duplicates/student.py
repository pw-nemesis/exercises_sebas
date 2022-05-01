# Write your code here
def remove_duplicates(xs):
    result = set()
    xx = []

    for x in xs:
        if x not in result:
            xx.append(x)
            result.add(x)
    
    return xx

