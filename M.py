if __name__ == '__main__':
    n1 = str(input())
    n1 = [int(x) for x in n1.split()]
    A = str(input())
    A = [int(x) for x in A.split()]
    res = [ -1 for _ in range (n1[0])]
    
    part = {}
    for i in range(n1[0]):
        part[i] = A[i]
    for i in range(n1[1]):
        movQ = str(input())
        movQ = [int(x) for x in movQ.split()]
        for key in part:
            if not(key % movQ[0]) :
                print("resta", key)
                resta = part[key] - movQ[1]
                if resta <= 0:
                    part[key] = 0
                    if res[key] >= 1:
                        res[key] = i + 1
                else:
                    part[key] = resta
    for i in res:
        print(i)