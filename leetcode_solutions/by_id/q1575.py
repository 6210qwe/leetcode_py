# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1575
标题: Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
难度: medium
链接: https://leetcode.cn/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/
题目类型: 贪心、数组、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1465. 切割后面积最大的蛋糕 - 矩形蛋糕的高度为 h 且宽度为 w，给你两个整数数组 horizontalCuts 和 verticalCuts，其中： * horizontalCuts[i] 是从矩形蛋糕顶部到第 i 个水平切口的距离 * verticalCuts[j] 是从矩形蛋糕的左侧到第 j 个竖直切口的距离 请你按数组 horizontalCuts 和 verticalCuts 中提供的水平和竖直位置切割后，请你找出 面积最大 的那份蛋糕，并返回其 面积 。由于答案可能是一个很大的数字，因此需要将结果 对 109 + 7 取余 后返回。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/05/30/leetcode_max_area_2.png] 输入：h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3] 输出：4 解释：上图所示的矩阵蛋糕中，红色线表示水平和竖直方向上的切口。切割蛋糕后，绿色的那份蛋糕面积最大。 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/05/30/leetcode_max_area_3.png] 输入：h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1] 输出：6 解释：上图所示的矩阵蛋糕中，红色线表示水平和竖直方向上的切口。切割蛋糕后，绿色和黄色的两份蛋糕面积最大。 示例 3： 输入：h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3] 输出：9 提示： * 2 <= h, w <= 109 * 1 <= horizontalCuts.length <= min(h - 1, 105) * 1 <= verticalCuts.length <= min(w - 1, 105) * 1 <= horizontalCuts[i] < h * 1 <= verticalCuts[i] < w * 题目数据保证 horizontalCuts 中的所有元素各不相同 * 题目数据保证 verticalCuts 中的所有元素各不相同
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
