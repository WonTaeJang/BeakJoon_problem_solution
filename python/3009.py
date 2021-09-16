'''
문제 
> 세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.

입력
> 세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.

출력
> 직사각형의 네 번째 점의 좌표를 출력한다.
'''

rect_lists = []
for i in range(3):
    rect_list = input().split()
    
    rect_lists.append(rect_list)

x = 1
_x = 0
_xCount = 0
y = 1
_y = 0
_yCount = 0

if(rect_lists[0][0] == rect_lists[1][0]):
    x += 1
else:
    _x += 1
    _xCount = 1

if(rect_lists[0][0] == rect_lists[2][0]):
    x += 1
else:
    _x += 1
    _xCount = 2

if(rect_lists[0][1] == rect_lists[1][1]):
    y += 1
else:
    _y += 1
    _yCount = 1

if(rect_lists[0][1] == rect_lists[2][1]):
    y += 1
else:
    _y += 1
    _yCount = 2


print(rect_lists[0][0] if x < _x else rect_lists[_xCount][0], rect_lists[0][1] if y < _y else rect_lists[_yCount][1])