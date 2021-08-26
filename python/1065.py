'''
문제
> 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 

등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. 

N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 

입력
> 첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.

출력
> 첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.
'''

def isArithmetic_Sequence(N):
    arg = list(str(N))
    isArithmetic = False

    if len(arg) > 2:
        arithA = 0     # 등차 

        for x in range(len(arg)):
            if x + 1 == len(arg):
                break
            

            # 등차수열 첫번째는 arithA에 값을 넣는다
            # 그 이후로는 arithB를 만들어 arithA와 값이 같은지 비교한다 
            # 값이 다르다면 return false
            arithB = Arithmetic(arg[x], arg[x+1])

            if x == 0: 
                arithA = arithB   
            else: 
                if arithB == arithA:
                    arithA = arithB
                    isArithmetic = True
                else: 
                    isArithmetic = False
    else:
        isArithmetic = True

    return isArithmetic
        
def Arithmetic(arg1, arg2):
    return int(arg2) - int(arg1)
    
n = input()
cnt = 0

for x in range(1, int(n) +1):
    if isArithmetic_Sequence(x):
        cnt += 1

print(cnt)