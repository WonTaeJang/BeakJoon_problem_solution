'''
문제
> M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

입력
> 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

출력
> 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.


https://wikidocs.net/21638
'''
# 에라토스테네스의 체
# 방식: 범위에서 합성수를 지우는 방식으로 소수를 찾는 방법.
# 장점: 범위의 모든 소수를 구할 때 효율적

def getPrimes(min, max):
    n = max

    a = [False,False] + [True]*(n-1)
    primes=[]

    for i in range(2,n+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False

    return primes

min, max = map(int,input().split())

arr = getPrimes(min, max)

for x in arr:
    if(x >= min):
        print(x)