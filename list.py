if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr = list(set(arr))   # duplicates hatao
    arr.sort()             # sort karo
    print(arr[-2])         # second largest ✅
