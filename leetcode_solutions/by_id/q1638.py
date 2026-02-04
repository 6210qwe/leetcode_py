# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1638
标题: Best Position for a Service Centre
难度: hard
链接: https://leetcode.cn/problems/best-position-for-a-service-centre/
题目类型: 几何、数组、数学、随机化
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1515. 服务中心的最佳位置 - 一家快递公司希望在新城市建立新的服务中心。公司统计了该城市所有客户在二维地图上的坐标，并希望能够以此为依据为新的服务中心选址：使服务中心 到所有客户的欧几里得距离的总和最小 。 给你一个数组 positions ，其中 positions[i] = [xi, yi] 表示第 i 个客户在二维地图上的位置，返回到所有客户的 欧几里得距离的最小总和 。 换句话说，请你为服务中心选址，该位置的坐标 [xcentre, ycentre] 需要使下面的公式取到最小值： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/07/12/q4_edited.jpg] 与真实值误差在 10-5之内的答案将被视作正确答案。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/07/12/q4_e1.jpg] 输入：positions = [[0,1],[1,0],[1,2],[2,1]] 输出：4.00000 解释：如图所示，你可以选 [xcentre, ycentre] = [1, 1] 作为新中心的位置，这样一来到每个客户的距离就都是 1，所有距离之和为 4 ，这也是可以找到的最小值。 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/07/12/q4_e3.jpg] 输入：positions = [[1,1],[3,3]] 输出：2.82843 解释：欧几里得距离可能的最小总和为 sqrt(2) + sqrt(2) = 2.82843 提示： * 1 <= positions.length <= 50 * positions[i].length == 2 * 0 <= xi, yi <= 100
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用梯度下降法来找到最优的中心位置。

算法步骤:
1. 初始化中心位置为所有点的平均值。
2. 计算当前中心位置到所有点的欧几里得距离的总和。
3. 使用梯度下降法更新中心位置，直到收敛或达到最大迭代次数。

关键点:
- 使用梯度下降法来优化中心位置。
- 设置合适的步长和停止条件以确保算法收敛。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * k)，其中 n 是 positions 的长度，k 是最大迭代次数。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution
import math


def get_distance_sum(positions: List[List[int]], x_center: float, y_center: float) -> float:
    """
    计算给定中心位置到所有点的欧几里得距离的总和。
    """
    return sum(math.sqrt((x - x_center) ** 2 + (y - y_center) ** 2) for x, y in positions)


def solution_function_name(positions: List[List[int]]) -> float:
    """
    函数式接口 - 使用梯度下降法找到最优的中心位置。
    """
    # 初始化中心位置为所有点的平均值
    x_center = sum(x for x, y in positions) / len(positions)
    y_center = sum(y for x, y in positions) / len(positions)

    # 设置梯度下降参数
    learning_rate = 0.01
    max_iterations = 1000
    tolerance = 1e-6

    for _ in range(max_iterations):
        # 计算梯度
        gradient_x = sum((x - x_center) / math.sqrt((x - x_center) ** 2 + (y - y_center) ** 2) for x, y in positions)
        gradient_y = sum((y - y_center) / math.sqrt((x - x_center) ** 2 + (y - y_center) ** 2) for x, y in positions)

        # 更新中心位置
        new_x_center = x_center - learning_rate * gradient_x
        new_y_center = y_center - learning_rate * gradient_y

        # 检查是否收敛
        if abs(new_x_center - x_center) < tolerance and abs(new_y_center - y_center) < tolerance:
            break

        x_center, y_center = new_x_center, new_y_center

    return get_distance_sum(positions, x_center, y_center)


Solution = create_solution(solution_function_name)