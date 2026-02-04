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
核心思想: 通过排序找到相邻切口之间的最大距离，从而计算出最大面积。

算法步骤:
1. 将水平和竖直切口分别排序。
2. 计算相邻水平切口之间的最大距离（包括边界）。
3. 计算相邻竖直切口之间的最大距离（包括边界）。
4. 计算最大面积并取模 10^9 + 7。

关键点:
- 排序以找到相邻切口之间的最大距离。
- 处理边界情况，确保包含从 0 到第一个切口以及最后一个切口到边界的距离。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n + m log m)，其中 n 是 horizontalCuts 的长度，m 是 verticalCuts 的长度。
空间复杂度: O(1)，除了输入和输出外，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def max_area_of_cake(h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
    """
    计算切割后面积最大的蛋糕。
    
    :param h: 蛋糕的高度
    :param w: 蛋糕的宽度
    :param horizontalCuts: 水平切口的位置
    :param verticalCuts: 竖直切口的位置
    :return: 最大面积对 10^9 + 7 取余后的结果
    """
    MOD = 10**9 + 7
    
    # 添加边界切口
    horizontalCuts = [0] + sorted(horizontalCuts) + [h]
    verticalCuts = [0] + sorted(verticalCuts) + [w]
    
    # 计算相邻水平切口之间的最大距离
    max_h_dist = max(horizontalCuts[i+1] - horizontalCuts[i] for i in range(len(horizontalCuts) - 1))
    
    # 计算相邻竖直切口之间的最大距离
    max_v_dist = max(verticalCuts[i+1] - verticalCuts[i] for i in range(len(verticalCuts) - 1))
    
    # 计算最大面积并取模
    return (max_h_dist * max_v_dist) % MOD


Solution = create_solution(max_area_of_cake)