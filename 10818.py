'''
N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
'''

num = int(input())
a = list(map(int, input().split()))

max = max(a)
min = min(a)

print(min, max)
