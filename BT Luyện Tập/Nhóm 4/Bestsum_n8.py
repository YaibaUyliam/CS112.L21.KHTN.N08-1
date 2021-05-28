def Bestsum(K, arr):
    KQ = [(int(1e9), 0)] * (K + 1) 
    for i in range(len(arr)):
        if arr[i] > K:
            break
        KQ[arr[i]] = (1, i)
        for x in range(arr[i]+1, K + 1):
            if KQ[x-arr[i]][0] != 0:
                if KQ[x][0] > KQ[x-arr[i]][0] + 1:
                    KQ[x] = (KQ[x-arr[i]][0] + 1, i)
    while(K != 0):
        print(arr[KQ[K][1]], end=" ")
        K -= arr[KQ[K][1]]

arr = []
[arr.append(int(i)) for i in input().strip().split()]
K = int(input())
Bestsum(K, arr)