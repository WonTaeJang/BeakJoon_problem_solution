'''
문제
> M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

입력
> 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

출력
> 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.


https://wikidocs.net/21638
'''
import sys
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

min, max = map(int, input().split())

result = []

for x in range(min, max+1):
    if isPrimeNumber(x):
        result.append(x)

#result
for x in result:
    sys.stdout.write(str(x)+"\n")