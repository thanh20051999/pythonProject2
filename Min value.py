def min(a,b,c):
    min_of_two = 0
    result = 0
    if a>b:
        min_of_two = b
    else:
        min_of_two = a
    if min_of_two<c:
        result = min_of_two
    else:
        result = c
    return result


def main():
    print(min(2,3,15), end='')

main()




