# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 335
标题: Self Crossing
难度: hard
链接: https://leetcode.cn/problems/self-crossing/
题目类型: 几何、数组、数学
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
335. 路径交叉 - 给你一个整数数组 distance 。 从 X-Y 平面上的点 (0,0) 开始，先向北移动 distance[0] 米，然后向西移动 distance[1] 米，向南移动 distance[2] 米，向东移动 distance[3] 米，持续移动。也就是说，每次移动后你的方位会发生逆时针变化。 判断你所经过的路径是否相交。如果相交，返回 true ；否则，返回 false 。 示例 1： [https://assets.leetcode.com/uploads/2021/03/14/selfcross1-plane.jpg] 输入：distance = [2,1,1,2] 输出：true 示例 2： [https://assets.leetcode.com/uploads/2021/03/14/selfcross2-plane.jpg] 输入：distance = [1,2,3,4] 输出：false 示例 3： [https://assets.leetcode.com/uploads/2021/03/14/selfcross3-plane.jpg] 输入：distance = [1,1,1,1] 输出：true 提示： * 1 <= distance.length <= 105 * 1 <= distance[i] <= 105
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 检查三种交叉情况

算法步骤:
1. 情况1：第i条边与第i-3条边交叉
2. 情况2：第i条边与第i-4条边交叉
3. 情况3：第i条边与第i-5条边交叉

关键点:
- 三种交叉情况
- 时间复杂度O(n)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 遍历数组一次
空间复杂度: O(1) - 只使用常数额外空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def is_self_crossing(distance: List[int]) -> bool:
    """
    函数式接口 - 路径交叉
    
    实现思路:
    检查三种交叉情况。
    
    Args:
        distance: 距离数组
        
    Returns:
        是否路径交叉
        
    Example:
        >>> is_self_crossing([2,1,1,2])
        True
    """
    n = len(distance)
    if n < 4:
        return False
    
    for i in range(3, n):
        # 情况1：第i条边与第i-3条边交叉
        if distance[i] >= distance[i-2] and distance[i-1] <= distance[i-3]:
            return True
        
        # 情况2：第i条边与第i-4条边交叉
        if i >= 4 and distance[i-1] == distance[i-3] and \
           distance[i] + distance[i-4] >= distance[i-2]:
            return True
        
        # 情况3：第i条边与第i-5条边交叉
        if i >= 5 and distance[i-2] >= distance[i-4] and \
           distance[i] + distance[i-4] >= distance[i-2] and \
           distance[i-1] + distance[i-5] >= distance[i-3] and \
           distance[i-1] <= distance[i-3]:
            return True
    
    return False


# 自动生成Solution类（无需手动编写）
Solution = create_solution(is_self_crossing)
