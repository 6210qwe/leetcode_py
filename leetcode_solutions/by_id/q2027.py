# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2027
标题: Maximum Number of Removable Characters
难度: medium
链接: https://leetcode.cn/problems/maximum-number-of-removable-characters/
题目类型: 数组、双指针、字符串、二分查找
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1898. 可移除字符的最大数目 - 给你两个字符串 s 和 p ，其中 p 是 s 的一个 子序列 。同时，给你一个元素 互不相同 且下标 从 0 开始 计数的整数数组 removable ，该数组是 s 中下标的一个子集（s 的下标也 从 0 开始 计数）。 请你找出一个整数 k（0 <= k <= removable.length），选出 removable 中的 前 k 个下标，然后从 s 中移除这些下标对应的 k 个字符。整数 k 需满足：在执行完上述步骤后， p 仍然是 s 的一个 子序列 。更正式的解释是，对于每个 0 <= i < k ，先标记出位于 s[removable[i]] 的字符，接着移除所有标记过的字符，然后检查 p 是否仍然是 s 的一个子序列。 返回你可以找出的 最大 k ，满足在移除字符后 p 仍然是 s 的一个子序列。 字符串的一个 子序列 是一个由原字符串生成的新字符串，生成过程中可能会移除原字符串中的一些字符（也可能不移除）但不改变剩余字符之间的相对顺序。 示例 1： 输入：s = "abcacb", p = "ab", removable = [3,1,0] 输出：2 解释：在移除下标 3 和 1 对应的字符后，"abcacb" 变成 "accb" 。 "ab" 是 "accb" 的一个子序列。 如果移除下标 3、1 和 0 对应的字符后，"abcacb" 变成 "ccb" ，那么 "ab" 就不再是 s 的一个子序列。 因此，最大的 k 是 2 。 示例 2： 输入：s = "abcbddddd", p = "abcd", removable = [3,2,1,4,5,6] 输出：1 解释：在移除下标 3 对应的字符后，"abcbddddd" 变成 "abcddddd" 。 "abcd" 是 "abcddddd" 的一个子序列。 示例 3： 输入：s = "abcab", p = "abc", removable = [0,1,2,3,4] 输出：0 解释：如果移除数组 removable 的第一个下标，"abc" 就不再是 s 的一个子序列。 提示： * 1 <= p.length <= s.length <= 105 * 0 <= removable.length < s.length * 0 <= removable[i] < s.length * p 是 s 的一个 子字符串 * s 和 p 都由小写英文字母组成 * removable 中的元素 互不相同
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用二分查找来确定最大可移除字符数 k，通过双指针方法检查 p 是否为 s 的子序列。

算法步骤:
1. 初始化二分查找的左右边界 left 和 right。
2. 在每次迭代中，计算中间值 mid，并尝试移除前 mid 个可移除字符。
3. 检查移除字符后的 s 是否仍然包含 p 作为子序列。
4. 根据检查结果调整二分查找的边界。
5. 最终返回最大的 k。

关键点:
- 使用二分查找来优化查找过程。
- 使用双指针方法来高效地检查 p 是否为 s 的子序列。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log m)，其中 n 是字符串 s 的长度，m 是 removable 的长度。
空间复杂度: O(n)，用于存储移除字符后的字符串。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def is_subsequence(s: str, p: str) -> bool:
    """检查 p 是否为 s 的子序列"""
    it = iter(s)
    return all(char in it for char in p)


def max_k(s: str, p: str, removable: List[int]) -> int:
    """使用二分查找找到最大可移除字符数 k"""
    left, right = 0, len(removable) + 1
    while left < right:
        mid = (left + right) // 2
        new_s = list(s)
        for i in range(mid):
            new_s[removable[i]] = ''
        if is_subsequence(''.join(new_s), p):
            left = mid + 1
        else:
            right = mid
    return left - 1


def solution_function_name(s: str, p: str, removable: List[int]) -> int:
    """
    函数式接口 - 找到最大可移除字符数 k
    """
    return max_k(s, p, removable)


Solution = create_solution(solution_function_name)