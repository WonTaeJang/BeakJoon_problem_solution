'''
문제
> 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

입력
> 첫째 줄에 시험 점수가 주어진다. 시험 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

'''

var1 = input()
var1 = int(var1)

if var1 >= 90 and var1 <= 100:
    print('A')
elif var1 >= 80 and var1 <= 89:
    print('B')
elif var1 >= 70 and var1 <= 79:
    print('C')
elif var1 >= 60 and var1 <= 69:
    print('D')
else:
    print('F')
