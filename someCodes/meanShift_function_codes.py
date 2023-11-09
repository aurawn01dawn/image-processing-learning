
def MeanShift(input, r):
    classification = []
    startNum = 512  # 起始点数量
    radium = r   # 窗口半径
    num = len(input)   # 样本数量
    Sample = np.int32([[0, 0, 0] for m in range(num)])    # 添加分类信息 0为未分类
    for i in range(num):
        Sample[i][0] = input[i][0]
        Sample[i][1] = input[i][1]

    # 随机选择一个起始点
    for i in range(startNum):
        # 范围
        ptr = random.randint(0, num-1)
        # 记录分类中心点
        center = [0, 0]
        center[0] = Sample[ptr][0]
        center[1] = Sample[ptr][1]
        Flag = 0
        # 判断终止条件
        iteration = 0
        while ((Flag == 0) & (iteration < 10)):
            orientation = [0, 0]   # 移动方向
            # 找出窗口内的所有样本点
            for j in range(num):
                oX = Sample[j][0] - center[0]
                oY = Sample[j][1] - center[1]
                dist = math.sqrt(oX*oX+oY*oY)
                # 该点在观察窗内
                if dist <= radium:
                    orientation[0] = orientation[0] + oX/20
                    orientation[1] = orientation[1] + oY/20
            # 开始漂移
            center[0] = center[0] + orientation[0]
            center[1] = center[1] + orientation[1]
            # 中心点不再移动时
            oX = orientation[0]
            oY = orientation[1]
            iteration = iteration + 1
            if math.sqrt(oX*oX + oY*oY) < 3:
                Flag = 1

        # 添加不重复的新分类信息
        Flag = 1
        for i in range(len(classification)):
            # 与当前存在的分类位置差别小于5
            oX = classification[i][0]-center[0]
            oY = classification[i][1]-center[1]
            if math.sqrt(oX*oX + oY*oY) < math.sqrt(classification[i][2]) + 30:
                Flag = 0
                break
        if Flag == 1:
            temp = [center[0], center[1], 0]
            classification.append(temp)

    # 给所有样本点分类
    for i in range(num):
        Index = 0
        minValue = 99999
        # 找出最近的分类
        for j in range(len(classification)):
            xx = classification[j][0]-Sample[i][0]
            yy = classification[j][1]-Sample[i][1]
            distination = abs(xx*xx + yy*yy)
            if distination <= minValue:
                Index = j
                minValue = distination
        Sample[i][2] = Index
        classification[Index][2] = classification[Index][2] + 1
    
    
    return classification, Sample
