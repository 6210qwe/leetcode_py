# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 809
标题: Preimage Size of Factorial Zeroes Function
难度: hard
链接: https://leetcode.cn/problems/preimage-size-of-factorial-zeroes-function/
题目类型: 数学、二分查找
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
793. 阶乘函数后 K 个零 - f(x) 是 x! 末尾是 0 的数量。回想一下 x! = 1 * 2 * 3 * ... * x，且 0! = 1 。 * 例如， f(3) = 0 ，因为 3! = 6 的末尾没有 0 ；而 f(11) = 2 ，因为 11!= 39916800 末端有 2 个 0 。 给定 k，找出返回能满足 f(x) = k 的非负整数 x 的数量。 示例 1： 输入：k = 0 输出：5 解释：0!, 1!, 2!, 3!, 和 4! 均符合 k = 0 的条件。 示例 2： 输入：k = 5 输出：0 解释：没有匹配到这样的 x!，符合 k = 5 的条件。 示例 3: 输入: k = 3 输出: 5 提示: * 0 <= k <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用二分查找来找到满足 f(x) = k 的 x 的范围。

算法步骤:
1. 定义一个辅助函数 `count_trailing_zeros` 来计算 n! 末尾的 0 的数量。
2. 使用二分查找来找到最小的 x 使得 f(x) >= k。
3. 如果找不到这样的 x，返回 0。
4. 检查 f(x) 是否等于 k，如果不等，返回 0。
5. 返回 5，因为如果 f(x) = k，则 x, x+1, x+2, x+3, x+4 都满足 f(x) = k。

关键点:
- 使用二分查找来高效地找到满足条件的 x。
- 辅助函数 `count_trailing_zeros` 用于计算 n! 末尾的 0 的数量。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log(n) * log(n))，其中 n 是 k 的值。二分查找的时间复杂度是 O(log(n))，每次计算末尾 0 的数量的时间复杂度是 O(log(n))。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def count_trailing_zeros(n: int) -> int:
    """计算 n! 末尾的 0 的数量"""
    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count


def preimage_size_of_factorial_zeroes_function(k: int) -> int:
    """
    函数式接口 - 找出返回能满足 f(x) = k 的非负整数 x 的数量。
    """
    left, right = 0, 5 * (k + 1)
    
    while left < right:
        mid = (left + right) // 2
        if count_trailing_zeros(mid) < k:
            left = mid + 1
        else:
            right = mid
    
    if count_trailing_zeros(left) != k:
        return 0
    return 5


Solution = create_solution(preimage_size_of_factorial_zeroes_function)