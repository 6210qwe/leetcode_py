# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 489
标题: Kth Smallest Instructions
难度: hard
链接: https://leetcode.cn/problems/kth-smallest-instructions/
题目类型: 数组、数学、动态规划、组合数学
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1643. 第 K 条最小指令 - Bob 站在单元格 (0, 0) ，想要前往目的地 destination ：(row, column) 。他只能向 右 或向 下 走。你可以为 Bob 提供导航 指令 来帮助他到达目的地 destination 。 指令 用字符串表示，其中每个字符： * 'H' ，意味着水平向右移动 * 'V' ，意味着竖直向下移动 能够为 Bob 导航到目的地 destination 的指令可以有多种，例如，如果目的地 destination 是 (2, 3)，"HHHVV" 和 "HVHVH" 都是有效 指令 。 然而，Bob 很挑剔。因为他的幸运数字是 k，他想要遵循 按字典序排列后的第 k 条最小指令 的导航前往目的地 destination 。k 的编号 从 1 开始 。 给你一个整数数组 destination 和一个整数 k ，请你返回可以为 Bob 提供前往目的地 destination 导航的 按字典序排列后的第 k 条最小指令 。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/11/01/ex1.png] 输入：destination = [2,3], k = 1 输出："HHHVV" 解释：能前往 (2, 3) 的所有导航指令 按字典序排列后 如下所示： ["HHHVV", "HHVHV", "HHVVH", "HVHHV", "HVHVH", "HVVHH", "VHHHV", "VHHVH", "VHVHH", "VVHHH"]. 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/11/01/ex2.png] 输入：destination = [2,3], k = 2 输出："HHVHV" 示例 3： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/11/01/ex3.png] 输入：destination = [2,3], k = 3 输出："HHVVH" 提示： * destination.length == 2 * 1 <= row, column <= 15 * 1 <= k <= nCr(row + column, row)，其中 nCr(a, b) 表示组合数，即从 a 个物品中选 b 个物品的不同方案数。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用组合数学计算每一步选择 'H' 或 'V' 的可能性，并根据 k 选择合适的路径。

算法步骤:
1. 计算总步数 `total` 和需要的 'H' 步数 `h`。
2. 使用组合数计算当前剩余步数中的 'H' 步数。
3. 根据 k 选择 'H' 或 'V'，并更新 k 和剩余步数。
4. 重复上述过程直到生成完整的路径。

关键点:
- 使用组合数快速计算每一步的选择。
- 优化时间和空间复杂度，避免递归和不必要的计算。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 其中 n 是总步数（row + column），每次选择 'H' 或 'V' 的操作都是 O(1)。
空间复杂度: O(1) - 除了输入和输出外，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution
from math import comb

def kth_smallest_instructions(destination: List[int]) -> str:
    """
    函数式接口 - 返回按字典序排列后的第 k 条最小指令
    
    实现思路:
    使用组合数学计算每一步选择 'H' 或 'V' 的可能性，并根据 k 选择合适的路径。
    
    Args:
        destination: 目的地坐标 [row, column]
        
    Returns:
        按字典序排列后的第 k 条最小指令
        
    Example:
        >>> kth_smallest_instructions([2, 3])
        "HHHVV"
    """
    def find_kth_path(k: int, h: int, v: int) -> str:
        path = []
        while h > 0 and v > 0:
            # 计算当前选择 'H' 的组合数
            if k > comb(h + v - 1, v):
                path.append('V')
                k -= comb(h + v - 1, v)
                v -= 1
            else:
                path.append('H')
                h -= 1
        path.extend(['H'] * h)
        path.extend(['V'] * v)
        return ''.join(path)

    row, col = destination
    total = row + col
    h = col
    v = row
    return find_kth_path(1, h, v)


# 自动生成Solution类（无需手动编写）
Solution = create_solution(kth_smallest_instructions)