# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1251
标题: Longest Chunked Palindrome Decomposition
难度: hard
链接: https://leetcode.cn/problems/longest-chunked-palindrome-decomposition/
题目类型: 贪心、双指针、字符串、动态规划、哈希函数、滚动哈希
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1147. 段式回文 - 你会得到一个字符串 text 。你应该把它分成 k 个子字符串 (subtext1, subtext2，…， subtextk) ，要求满足: * subtexti 是 非空 字符串 * 所有子字符串的连接等于 text ( 即subtext1 + subtext2 + ... + subtextk == text ) * 对于所有 i 的有效值( 即 1 <= i <= k ) ，subtexti == subtextk - i + 1 均成立 返回k可能最大值。 示例 1： 输入：text = "ghiabcdefhelloadamhelloabcdefghi" 输出：7 解释：我们可以把字符串拆分成 "(ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)"。 示例 2： 输入：text = "merchant" 输出：1 解释：我们可以把字符串拆分成 "(merchant)"。 示例 3： 输入：text = "antaprezatepzapreanta" 输出：11 解释：我们可以把字符串拆分成 "(a)(nt)(a)(pre)(za)(tep)(za)(pre)(a)(nt)(a)"。 提示： * 1 <= text.length <= 1000 * text 仅由小写英文字符组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法和双指针来找到最长的段式回文分解。

算法步骤:
1. 初始化两个指针 left 和 right 分别指向字符串的开头和结尾。
2. 从左到右和从右到左同时遍历字符串，寻找最长的相同子串。
3. 如果找到相同的子串，则将其计入结果，并移动指针。
4. 重复上述过程直到左右指针相遇。

关键点:
- 使用双指针从两端向中间遍历，确保每次找到的子串都是最长的。
- 通过比较子串的哈希值来快速判断是否相等。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2)，其中 n 是字符串的长度。最坏情况下，每个子串都需要进行比较。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def longest_decomposition(text: str) -> int:
    """
    函数式接口 - 实现最长段式回文分解
    """
    def get_hash(s: str) -> int:
        """计算字符串的哈希值"""
        p = 31
        m = 10**9 + 7
        hash_value = 0
        power = 1
        for char in s:
            hash_value = (hash_value + (ord(char) - ord('a') + 1) * power) % m
            power = (power * p) % m
        return hash_value

    n = len(text)
    left, right = 0, n - 1
    count = 0
    while left < right:
        l, r = left, right
        while l < r and get_hash(text[left:l+1]) != get_hash(text[r:right+1]):
            l += 1
            r -= 1
        if l < r:
            count += 2
            left = l + 1
            right = r - 1
        else:
            count += 1
            break
    return count if left >= right else count + 1


Solution = create_solution(longest_decomposition)