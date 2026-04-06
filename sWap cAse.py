def swap_case(s):
    result = ""
    
    for ch in s:
        if ch.isupper():
            result += ch.lower()
        else:
            result += ch.upper()
    
    return result


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
