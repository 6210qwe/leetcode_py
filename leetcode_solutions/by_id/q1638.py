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
核心思想: [TODO]

算法步骤:
1. [TODO]
2. [TODO]

关键点:
- [TODO]
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O([TODO])
空间复杂度: O([TODO])
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(params):
    """
    函数式接口 - [TODO] 实现
    """
    # TODO: 实现最优解法
    pass


Solution = create_solution(solution_function_name)
