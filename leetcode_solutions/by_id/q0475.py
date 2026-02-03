# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 475
标题: Heaters
难度: medium
链接: https://leetcode.cn/problems/heaters/
题目类型: 数组、双指针、二分查找、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
475. 供暖器 - 冬季已经来临。 你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。 在加热器的加热半径范围内的每个房屋都可以获得供暖。 现在，给出位于一条水平线上的房屋 houses 和供暖器 heaters 的位置，请你找出并返回可以覆盖所有房屋的最小加热半径。 注意：所有供暖器 heaters 都遵循你的半径标准，加热的半径也一样。 示例 1: 输入: houses = [1,2,3], heaters = [2] 输出: 1 解释: 仅在位置 2 上有一个供暖器。如果我们将加热半径设为 1，那么所有房屋就都能得到供暖。 示例 2: 输入: houses = [1,2,3,4], heaters = [1,4] 输出: 1 解释: 在位置 1, 4 上有两个供暖器。我们需要将加热半径设为 1，这样所有房屋就都能得到供暖。 示例 3： 输入：houses = [1,5], heaters = [2] 输出：3 提示： * 1 <= houses.length, heaters.length <= 3 * 104 * 1 <= houses[i], heaters[i] <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 二分查找，对每个房屋找最近的供暖器

算法步骤:
1. 排序供暖器位置
2. 对每个房屋，使用二分查找找最近的供暖器
3. 取所有房屋到最近供暖器距离的最大值

关键点:
- 二分查找优化
- 时间复杂度O(n log m)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log m) - n为房屋数，m为供暖器数
空间复杂度: O(1) - 只使用常数额外空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
import bisect
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def heaters(houses: List[int], heaters: List[int]) -> int:
    """
    函数式接口 - 供暖器
    
    实现思路:
    对每个房屋，使用二分查找找最近的供暖器。
    
    Args:
        houses: 房屋位置数组
        heaters: 供暖器位置数组
        
    Returns:
        最小加热半径
        
    Example:
        >>> heaters([1,2,3], [2])
        1
    """
    heaters.sort()
    max_radius = 0
    
    for house in houses:
        # 二分查找最近的供暖器
        pos = bisect.bisect_left(heaters, house)
        left_dist = house - heaters[pos - 1] if pos > 0 else float('inf')
        right_dist = heaters[pos] - house if pos < len(heaters) else float('inf')
        max_radius = max(max_radius, min(left_dist, right_dist))
    
    return max_radius


# 自动生成Solution类（无需手动编写）
Solution = create_solution(heaters)
