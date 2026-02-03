# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 365
标题: Water and Jug Problem
难度: medium
链接: https://leetcode.cn/problems/water-and-jug-problem/
题目类型: 深度优先搜索、广度优先搜索、数学
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
365. 水壶问题 - 有两个水壶，容量分别为 x 和 y 升。水的供应是无限的。确定是否有可能使用这两个壶准确得到 target 升。 你可以： * 装满任意一个水壶 * 清空任意一个水壶 * 将水从一个水壶倒入另一个水壶，直到接水壶已满，或倒水壶已空。 示例 1: 输入: x = 3,y = 5,target = 4 输出: true 解释： 按照以下步骤操作，以达到总共 4 升水： 1. 装满 5 升的水壶(0, 5)。 2. 把 5 升的水壶倒进 3 升的水壶，留下 2 升(3, 2)。 3. 倒空 3 升的水壶(0, 2)。 4. 把 2 升水从 5 升的水壶转移到 3 升的水壶(2, 0)。 5. 再次加满 5 升的水壶(2, 5)。 6. 从 5 升的水壶向 3 升的水壶倒水直到 3 升的水壶倒满。5 升的水壶里留下了 4 升水(3, 4)。 7. 倒空 3 升的水壶。现在，5 升的水壶里正好有 4 升水(0, 4)。 参考：来自著名的 "Die Hard"https://www.youtube.com/watch?v=BVtQNK_ZUJg 示例 2: 输入: x = 2, y = 6, target = 5 输出: false 示例 3: 输入: x = 1, y = 2, target = 3 输出: true 解释：同时倒满两个水壶。现在两个水壶中水的总量等于 3。 提示: * 1 <= x, y, target <= 103
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 数学-贝祖定理

算法步骤:
1. 根据贝祖定理，ax + by = z有解当且仅当z是gcd(x,y)的倍数
2. 检查target是否<=x+y（总容量限制）
3. 检查target是否能被gcd(x,y)整除

关键点:
- 使用最大公约数判断是否有解
- 需要检查容量限制
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log(min(x,y))) - 计算最大公约数
空间复杂度: O(1) - 只使用常数空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution
import math


def can_measure_water(jug1_capacity: int, jug2_capacity: int, target_capacity: int) -> bool:
    """
    函数式接口 - 水壶问题
    
    实现思路:
    使用贝祖定理判断是否有解，检查容量限制。
    
    Args:
        jug1_capacity: 第一个水壶容量
        jug2_capacity: 第二个水壶容量
        target_capacity: 目标容量
        
    Returns:
        是否能得到目标容量
        
    Example:
        >>> can_measure_water(3, 5, 4)
        True
    """
    if target_capacity > jug1_capacity + jug2_capacity:
        return False
    
    if target_capacity == 0:
        return True
    
    gcd = math.gcd(jug1_capacity, jug2_capacity)
    return target_capacity % gcd == 0


# 自动生成Solution类（无需手动编写）
Solution = create_solution(can_measure_water)
