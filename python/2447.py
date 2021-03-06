'''
문제
> 재귀적인 패턴으로 별을 찍어 보자. N이 3의 거듭제곱(3, 9, 27, ...)이라고 할 때, 크기 N의 패턴은 N×N 정사각형 모양이다.
크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.

***
* *
***
N이 3보다 클 경우, 크기 N의 패턴은 공백으로 채워진 가운데의 (N/3)×(N/3) 정사각형을 크기 N/3의 패턴으로 둘러싼 형태이다.
 예를 들어 크기 27의 패턴은 예제 출력 1과 같다.

입력
> 첫째 줄에 N이 주어진다. N은 3의 거듭제곱이다. 즉 어떤 정수 k에 대해 N=3k이며, 이때 1 ≤ k < 8이다.

출력
> 첫째 줄부터 N번째 줄까지 별을 출력한다.
'''

'''
1. 2차원 배열을 만든다
2. 입력받은 값의 3 제곱근을 구해서 몇번 반복해야하는지 확인한다. 
3. 중간의 네모 사이즈는 3^3 이면 3^2 크기이다.

3 3x3 1
9 9x9 3x3
27 3^2 
(9,9) (9 + 8, 9)
(9,9 + 8)(9 + 8,9 + 8)) 


'''
import math

def star(n):
    if n == 3:
        star_list = ['***', '* *', '***']
        return star_list
    else:
        new_star_list = [x * 3 for x in star(n//3)] 
        new_star_list += [x + ' '*(n//3) + x for x in star(n//3)] 
        new_star_list += [x * 3 for x in star(n//3)]
        return new_star_list

for i in star(int(input())):
    print(i)





num = int(input())
count = int(math.log(num * num, 9))

star_table = [['*' for col in range(num)] for row in range(num)]

def getSquareStar(count, star_table, sq_count):
    incount = count
    tb = star_table
    square_count = int(9**sq_count)
    square_size = int(3**(count - 1))

    for a in range(int(square_count**(1/2))):
        for b in range(int(square_count**(1/2))):
            for i in range(square_size):
                for j in range(square_size):
                    a1 = int(3**incount)*a + square_size
                    b1 = int(3**incount)*b + square_size
                    tb[a1 + i][b1 + j] = ' '

    
    incount = incount - 1

    if count == 0:
        return tb
    else : 
        return getSquareStar(incount, tb, sq_count + 1)

result = getSquareStar(count, star_table, 0)


str = ''
for i in range(num):
    for j in  range(num):
        str += result[i][j]

    if i != (num -1):
        str += '\n' 

print(str)  

