# 큰 수의 법칙 (풀이 1)
n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort() # 정렬 
first = data[n - 1]
second = data [n - 2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)

# 큰 수의 법칙 (풀이 2)
