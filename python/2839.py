'''
문제
> 상근이는 요즘 설탕공장에서 설탕을 배달하고 있다. 상근이는 지금 사탕가게에 설탕을 정확하게 N킬로그램을 배달해야 한다.
 설탕공장에서 만드는 설탕은 봉지에 담겨져 있다. 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.
 상근이는 귀찮기 때문에, 최대한 적은 봉지를 들고 가려고 한다. 
 
 예를 들어, 18킬로그램 설탕을 배달해야 할 때, 3킬로그램 봉지 6개를 가져가도 되지만, 5킬로그램 3개와 3킬로그램 1개를 배달하면, 
 더 적은 개수의 봉지를 배달할 수 있다.

 상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오.

입력
> 첫째 줄에 N이 주어진다. (3 ≤ N ≤ 5000)

출력
> 상근이가 배달하는 봉지의 최소 개수를 출력한다. 만약, 정확하게 N킬로그램을 만들 수 없다면 -1을 출력한다.
'''

SUGAR_3 = 3
SUGAR_5 = 5

test = int(input())
result = -1

# 1. 5로 나누었을때 나머지가 0이면 최소값
# 2. 5로 나누었을때 나머지가 있다면 나머지를 3으로 나누기
# 3. 5로 나누었을때 몫을 -1하여 5 * (몫-1) 한 뒤 test로 그 값을 빼서 남은 값을 3으로 나누기 
# 4. 3으로 나누어 위의 방식 반복

# [몫,나머지]
def division_Func(num, val):
    arr = []
    arr.append(int(num/val))
    arr.append(num % val)

    return arr

first = division_Func(test, SUGAR_5)

if(first[1] == 0):
    result = first[0]     # 5로 나누어 떨어지면 최소값
else:
    for x in reversed(range(first[0]+1)):
        test_div5 = test - (SUGAR_5*(x))
        test_div3 = division_Func(test_div5, SUGAR_3)

        #print(test, (x+1),test_div5, test_div3)

        if test_div3[1] == 0:
            result = (x) + test_div3[0]
            break
            

print(result)

