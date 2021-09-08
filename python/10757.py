'''
https://www.acmicpc.net/problem/10757

문제
> 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

입력
> 첫째 줄에 A와 B가 주어진다. (0 < A,B < 1010000)

풀이
> https://ahracho.github.io/posts/python/2017-05-09-python-integer-overflow/

'''

A, B = map(int, input().split())

print(A+B)