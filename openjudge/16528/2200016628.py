def max_activities(activities):
    # 按照活动的结束时间进行排序
    activities.sort(key=lambda x: x[1])
    
    count = 0
    last_end_time = -1
    
    for start, end in activities:
        if start > last_end_time:
            count += 1
            last_end_time = end
    return count

n = int(input())
activities = [tuple(map(int, input().split())) for _ in range(n)]


print(max_activities(activities))