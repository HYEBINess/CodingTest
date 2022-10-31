# 목표: 2로 나눠지는 횟수 리턴하기
# 1. 짝수면 count +1하고 홀수 리턴
# 2. 홀수이면 count +1하고 짝수 리턴

def numberOfSteps(n):
    count = 0
    a = n+1

    while True:
        if a % 2 == 0: # a가 짝수이면
            a = a // 2 # a는 2로 나눈 몫
