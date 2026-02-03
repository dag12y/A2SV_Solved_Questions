def swap_case(s):
    caps="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result=''
    for letter in s:
        if letter in caps:
            result+=letter.lower()
        else:
            result+=letter.upper()
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
