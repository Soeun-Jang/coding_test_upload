now = [0, 0]    # 현재좌표
dic_arrows = {  # 위치 변경할 때 사용되는 딕셔너리
    0: [0, 1],
    1: [1, 1],
    2: [1, 0],
    3: [1, -1],
    4: [0, -1],
    5: [-1, -1],
    6: [-1, 0],
    7: [-1, 1]
}
path = {}  # 지나온 경로와 해당 경로에 대한 방향을 저장하는 빈 딕셔너리 선언

def check_dia(path, now, arrow):  # 대각선 방향 교차 확인 함수
    c_now = now[:]
    c_arrow = arrow
    if c_arrow > 6:
        c_arrow -= 7
    else:
        c_arrow += 1
    c_now[0] += dic_arrows[c_arrow][0]
    c_now[1] += dic_arrows[c_arrow][1]

    if c_arrow > 2:
        c_arrow -= 3
    else:
        c_arrow += 5

    try:
        c_check_list = path[str(c_now)]
        if c_arrow in c_check_list:
            return True
    except:
        pass
    return False


def solution(arrows):   # 방 개수 구하는 함수
    result = 0
    for arrow in arrows:
        # 이동전
        inline = True
        dic_p = str(now)
        try:
            if arrow not in path[dic_p]:
                path[dic_p] = path[dic_p]+[arrow]
        except:
            path[dic_p] = [arrow]
        # 이동후
        now[0] += dic_arrows[arrow][0]
        now[1] += dic_arrows[arrow][1]
        if arrow > 3:
            arrow = arrow-4
        else:
            arrow = arrow+4
        dic_p = str(now)
        try:
            if arrow not in path[dic_p]:
                path[dic_p] = path[dic_p]+[arrow]
                result += 1
                inline = False
            else:
                inline = True
        except:
            path[dic_p] = [arrow]
            inline = False
        if (arrow % 2 == 1) and (not inline):
            result += check_dia(path, now, arrow)
    return result