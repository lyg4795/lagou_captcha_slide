import random
def get_track(distance):      # distance为传入的总距离
    # 移动轨迹
    tracks = []
    # 当前位移
    current = 0
    # 减速阈值
    mid = distance * 4 / 5
    # 时间间隔
    t = 0.1
    # 初始速度
    v = 0

    while current < mid:
        a = random.uniform(2, 5)
        v0 = v
        v = v0 + a * t
        x = int(v0 * t + 1 / 2 * a * t * t)+1
        current += x
        tracks.append(x)
    while current<distance:
        # a=random.randint(-30,-15)
        # v0=v
        # v = v0 + a * t
        # x = int(v0 * t + 1 / 2 * a * t * t) + 1
        # if x<1:
        #     x=1
        x-=1
        if x<1:
            x=1
        current += x
        tracks.append(x)
    while current>distance:
        current-=1
        tracks.append(-1)

    return tracks
if __name__ == '__main__':
    print(get_track(84))