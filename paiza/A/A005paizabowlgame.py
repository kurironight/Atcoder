# 入力情報
a, b, n = map(int, input().split())
hit_pin_list = list(input().split())
hit_pin_list = [int(i) if i != "G" else 0 for i in hit_pin_list]
score_list = []

# frame_counts
frame_counts = [2]*(a-1)
frame_counts += [3]
# scoreを入れていく
frame_score_list = []
index = 0
for frame_count in frame_counts:
    frame_score = []
    if frame_count == 2:
        for i in range(frame_count):
            frame_score.append(hit_pin_list[index])
            index += 1
            if sum(frame_score) == b:
                break
    else:
        frame_score = hit_pin_list[index:]
    frame_score_list.append(frame_score)


def classify(hitpinlist):
    total = sum(hitpinlist)
    if total != b:
        return [total, 0]
    elif hitpinlist[0] == b:
        return [total, 2]
    else:
        return [total, 1]


def classify_last_score(hitpinlist):
    if hitpinlist[0] == b:
        if hitpinlist[1] == b:
            return (hitpinlist[0]+hitpinlist[1]*2+hitpinlist[2]*3)
        else:
            return (hitpinlist[0]+hitpinlist[1]*2+hitpinlist[2]*2)
    elif sum(hitpinlist[:2]) == b:
        return (b+hitpinlist[2]*2)
    else:
        return sum(hitpinlist)


status_list = [classify(i) for i in frame_score_list[:-1]]

index = 0
sum_score = 0
for i in status_list:
    if i[1] == 0:
        index += 2
        sum_score += i[0]
    elif i[1] == 1:
        index += 2
        sum_score += i[0]+hit_pin_list[index]
    else:
        index += 1
        sum_score += i[0]+sum(hit_pin_list[index:index+2])

print(sum_score+classify_last_score(frame_score_list[-1]))
