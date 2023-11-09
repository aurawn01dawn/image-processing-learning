# 这里是基本的源码，若想运行测试建议在jupyter lab下的 ".ipynb" 中运行
# 主要使用numpy和基本的python,matplotlib用于可视化
import numpy as np
import matplotlib.pyplot as plt
# 定义一个类实现KMeans的基本原理
class KMeansClustering:
    def __init__(self, k=3):
        self.k = k
        self.centroids = None
    # 计算欧式距离的方法
    @staticmethod
    def euclidean_distance(data_point, centroids):
        return np.sqrt(np.sum((centroids - data_point)**2, axis=1))
    # 拟合：X是输入的聚类数据
    def fit(self, X, max_iterations=200):
        # 随即初始化聚类中心：在数据的边界内随机选择质心
        self.centroids = np.random.uniform(np.amin(X, axis=0), np.amax(X, axis=0), 
                                            size=(self.k, X.shape[1]))
        # 迭代
        for _ in range(max_iterations):
            # 簇的标签
            y = []    
            # 计算每个数据点到所有质心的欧式距离
            for data_point in X:
                distances = KMeansClustering.euclidean_distance(data_point, self.centroids)
                # 返回最小距离对应点的索引作为簇的标签
                cluster_num = np.argmin(distances)
                y.append(cluster_num)
            y = np.array(y)

            # 簇中数据点的索引
            cluster_indices = []
            #将数据集中被分配到每个簇的数据点的索引进行收集
            for i in range(self.k):
                cluster_indices.append(np.argwhere(y == i))
            # 新的聚类中心
            cluster_centers = []

            # 计算新的聚类中心
            for i, indices in enumerate(cluster_indices):
                if len(indices) == 0:
                    cluster_centers.append(self.centroids[i])
                else:
                    cluster_centers.append(np.mean(X[indices], axis=0)[0])

            # 设置聚类中心更新的差异阈值
            if np.max(self.centroids - np.array(cluster_centers)) < 0.0001:
                break
            else:
                self.centroids = np.array(cluster_centers)
        # 返回X对应的簇-索引对照数组
        return y