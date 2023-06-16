'''
문제: 총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하시오.
'''

number =int(input())
num_list = list(map(int, input().split())) 
target = int(input())

count = 0
for i in range(number):
    if num_list[i] == target:
        count +=1
        
print(count)
