# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000236
标题: 最大单词长度乘积
难度: medium
链接: https://leetcode.cn/problems/aseY1I/
题目类型: 位运算、数组、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 005. 最大单词长度乘积 - 给定一个字符串数组 words，请计算当两个字符串 words[i] 和 words[j] 不包含相同字符时，它们长度的乘积的最大值。假设字符串中只包含英语的小写字母。如果没有不包含相同字符的一对字符串，返回 0。 示例 1： 输入：words = ["abcw","baz","foo","bar","fxyz","abcdef"] 输出：16 解释：这两个单词为 "abcw", "fxyz"。它们不包含相同字符，且长度的乘积最大。 示例 2： 输入：words = ["a","ab","abc","d","cd","bcd","abcd"] 输出：4 解释：这两个单词为 "ab", "cd"。 示例 3： 输入：words = ["a","aa","aaa","aaaa"] 输出：0 解释：不存在这样的两个单词。 提示： * 2 <= words.length <= 1000 * 1 <= words[i].length <= 1000 * words[i] 仅包含小写字母 注意：本题与主站 318 题相同：https://leetcode.cn/problems/maximum-product-of-word-lengths/ [https://leetcode.cn/problems/maximum-product-of-word-lengths/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 用位掩码表示单词字符集合，按位与判断是否有公共字符

算法步骤:
1. 对于每个单词 word，计算其字符掩码 mask：
   - 初始 mask = 0
   - 对于 word 中每个字符 ch，将 mask |= 1 << (ord(ch) - ord('a'))
2. 维护两个数组：
   - masks[i] 表示第 i 个单词的掩码
   - lens[i] 表示第 i 个单词的长度
3. 双重循环枚举 i < j：
   - 若 masks[i] & masks[j] == 0，说明两个单词没有公共字符
   - 更新答案 ans = max(ans, lens[i] * lens[j])
4. 返回 ans

关键点:
- 掩码最多 26 位，按位与操作 O(1)
- 位掩码预处理可以将字符比较从 O(L) 降为 O(1)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2 + 总字符数) - n 为单词数量
空间复杂度: O(n) - 存储每个单词的掩码和长度
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def max_product(words: List[str]) -> int:
    """
    函数式接口 - 最大单词长度乘积
    """
    n = len(words)
    masks = [0] * n
    lens = [0] * n

    for i, word in enumerate(words):
        mask = 0
        for ch in word:
            mask |= 1 << (ord(ch) - ord('a'))
        masks[i] = mask
        lens[i] = len(word)

    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if masks[i] & masks[j] == 0:
                prod = lens[i] * lens[j]
                if prod > ans:
                    ans = prod
    return ans


Solution = create_solution(max_product)
