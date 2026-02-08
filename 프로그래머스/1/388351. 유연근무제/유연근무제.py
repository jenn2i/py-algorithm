def timeMin(t): # 분 단위로 변경 -> 10분 초과 계산 편하게 하기 위해
    return (t // 100) * 60 + t % 100

def solution(schedules, timelogs, startday):
    count = 0
    people = len(schedules)
    
    for i in range(people):
        limit = timeMin(schedules[i]) + 10 # 10분 지각까지 ㄱㅊ
        on_time = True
        for j in range(7): # 오늘 요일 계산
            currentday = (startday + j - 1) % 7 + 1
            if currentday >= 6: # 주말 거르기
                continue
            if timeMin(timelogs[i][j]) > limit: # 늦었는지 계산
                on_time = False
                break
                
        if on_time:
            count += 1
        
    
    return count