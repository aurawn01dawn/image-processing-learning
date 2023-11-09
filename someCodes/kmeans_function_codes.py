# ***************************** K-means 聚类 **********************************
# in:二维数据点 xMax,yMax：边界最大值（图像尺寸）
def Kmeans(input, k, xMax, yMax):
    # 加上分类信息
    keyPoint = [[0 for x in range(3)] for y in range(len(input))]
    for i in range(len(keyPoint)):
        keyPoint[i][0] = input[i][0]
        keyPoint[i][1] = input[i][1]
        keyPoint[i][2] = 999
    # 初始化 k 个中心点
    center = [[0 for x in range(3)] for y in range(k)]
    #radious = [0 for x in range(k)]
    for i in range(k):
        center[i][0] = random.randint(0, xMax)
        center[i][1] = random.randint(0, yMax)

    # 停止迭代的三个条件
    time = 0  # 迭代次数
    timeMax = 4
    changed = 0  # 重新分配
    a = 0.01  # 最小移动与图像尺度的比例
    move = 0  # 所有类中心移动距离小于moveMax
    moveMax = a*xMax

    # 未到最大迭代次数
    while time < timeMax:
        time = time + 1
        # 计算每个点的最近分类
        for i in range(len(keyPoint)):
            dis = -1
            for j in range(k):
                x = keyPoint[i][0] - center[j][0]
                y = keyPoint[i][1] - center[j][1]
                disTemp = x*x + y*y
                # 更新当前最近分类并标记
                if (disTemp < dis) | (dis == -1):
                    dis = disTemp
                    keyPoint[i][2] = j
        # 更新类中心点坐标
        for i in range(k):
            xSum = 0
            ySum = 0
            num = 0
            for j in range(len(keyPoint)):
                if keyPoint[j][2] == i:
                    xSum = xSum + keyPoint[j][0]
                    ySum = ySum + keyPoint[j][1]
                    num = num + 1
            if num != 0:
                center[i][0] = xSum/num
                center[i][1] = ySum/num
     # 记录每个分类的点数量
    for i in range(len(keyPoint)):
        center[keyPoint[i][2]][2] = center[keyPoint[i][2]][2] + 1
    return center