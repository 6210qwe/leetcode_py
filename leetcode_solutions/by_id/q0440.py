# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 440
标题: K-th Smallest in Lexicographical Order
难度: hard
链接: https://leetcode.cn/problems/k-th-smallest-in-lexicographical-order/
题目类型: 字典树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
440. 字典序的第K小数字 - 给定整数 n 和 k，返回 [1, n] 中字典序第 k 小的数字。 示例 1: 输入: n = 13, k = 2 输出: 10 解释: 字典序的排列是 [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]，所以第二小的数字是 10。 示例 2: 输入: n = 1, k = 1 输出: 1 提示: * 1 <= k <= n <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用字典树的思想来解决这个问题。我们可以通过计算某个前缀下的所有可能的字典序数字的数量，来确定当前前缀是否包含第 k 个字典序数字。

算法步骤:
1. 初始化当前前缀为 1。
2. 计算当前前缀下的所有可能的字典序数字的数量 `count`。
3. 如果 `count` 小于 `k`，则说明第 k 个字典序数字不在当前前缀下，更新 `k -= count` 并将前缀加 1。
4. 否则，说明第 k 个字典序数字在当前前缀下，将前缀乘以 10，并减少 `k`。
5. 重复上述步骤直到找到第 k 个字典序数字。

关键点:
- 注意边界条件，特别是当 n 为 9 时的情况。
- 通过计算前缀下的所有可能的字典序数字的数量来优化时间和空间复杂度。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log n) - 每次迭代中，前缀长度增加或减少一个数量级。
空间复杂度: O(1) - 只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def k_th_smallest_in_lexicographical_order(n: int, k: int) -> int:
    """
    函数式接口 - 返回 [1, n] 中字典序第 k 小的数字
    
    实现思路:
    使用字典树的思想来解决这个问题。通过计算某个前缀下的所有可能的字典序数字的数量，来确定当前前缀是否包含第 k 个字典序数字。

    Args:
        n (int): 范围 [1, n]
        k (int): 第 k 小的字典序数字
        
    Returns:
        int: 第 k 小的字典序数字
        
    Example:
        >>> k_th_smallest_in_lexicographical_order(13, 2)
        10
    """
    def count_prefix(prefix: int) -> int:
        """计算以 prefix 开头的所有可能的字典序数字的数量"""
        count, next_prefix = 0, prefix + 1
        while prefix <= n:
            count += min(n + 1, next_prefix) - prefix
            prefix *= 10
            next_prefix *= 10
        return count

    current, k = 1, k - 1  # k - 1 因为我们要找的是第 k 个，而不是第 k+1 个
    while k > 0:
        count = count_prefix(current)
        if count <= k:
            k -= count
            current += 1
        else:
            current *= 10
            k -= 1
    return current


# 自动生成Solution类（无需手动编写）
Solution = create_solution(k_th_smallest_in_lexicographical_order)