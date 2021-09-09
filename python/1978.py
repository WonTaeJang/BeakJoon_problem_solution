'''
문제
> 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

입력
> 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

출력
> 주어진 수들 중 소수의 개수를 출력한다.
'''

loop = int(input())
arr = []
cnt = 0

arr = input().split()

def isPrimeNumber(x):
    result = True
    value = x-1

    if(x == 1):
        return False

    while value > 1:
        if x%value == 0:
            result = False
            break

        value -= 1

    return result

for x in range(len(arr)):
    if isPrimeNumber(int(arr[x])):
        cnt += 1

# result
print(cnt)