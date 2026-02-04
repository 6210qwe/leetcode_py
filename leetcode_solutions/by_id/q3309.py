# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3309
标题: Count Prefix and Suffix Pairs I
难度: easy
链接: https://leetcode.cn/problems/count-prefix-and-suffix-pairs-i/
题目类型: 字典树、数组、字符串、字符串匹配、哈希函数、滚动哈希
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3042. 统计前后缀下标对 I - 给你一个下标从 0 开始的字符串数组 words 。 定义一个 布尔 函数 isPrefixAndSuffix ，它接受两个字符串参数 str1 和 str2 ： * 当 str1 同时是 str2 的前缀（prefix）和后缀（suffix）时，isPrefixAndSuffix(str1, str2) 返回 true，否则返回 false。 例如，isPrefixAndSuffix("aba", "ababa") 返回 true，因为 "aba" 既是 "ababa" 的前缀，也是 "ababa" 的后缀，但是 isPrefixAndSuffix("abc", "abcd") 返回 false。 以整数形式，返回满足 i < j 且 isPrefixAndSuffix(words[i], words[j]) 为 true 的下标对 (i, j) 的 数量 。 示例 1： 输入：words = ["a","aba","ababa","aa"] 输出：4 解释：在本示例中，计数的下标对包括： i = 0 且 j = 1 ，因为 isPrefixAndSuffix("a", "aba") 为 true 。 i = 0 且 j = 2 ，因为 isPrefixAndSuffix("a", "ababa") 为 true 。 i = 0 且 j = 3 ，因为 isPrefixAndSuffix("a", "aa") 为 true 。 i = 1 且 j = 2 ，因为 isPrefixAndSuffix("aba", "ababa") 为 true 。 因此，答案是 4 。 示例 2： 输入：words = ["pa","papa","ma","mama"] 输出：2 解释：在本示例中，计数的下标对包括： i = 0 且 j = 1 ，因为 isPrefixAndSuffix("pa", "papa") 为 true 。 i = 2 且 j = 3 ，因为 isPrefixAndSuffix("ma", "mama") 为 true 。 因此，答案是 2 。 示例 3： 输入：words = ["abab","ab"] 输出：0 解释：在本示例中，唯一有效的下标对是 i = 0 且 j = 1 ，但是 isPrefixAndSuffix("abab", "ab") 为 false 。 因此，答案是 0 。 提示： * 1 <= words.length <= 50 * 1 <= words[i].length <= 10 * words[i] 仅由小写英文字母组成。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用双重循环遍历所有可能的下标对 (i, j)，并检查 words[i] 是否同时是 words[j] 的前缀和后缀。

算法步骤:
1. 初始化计数器 count 为 0。
2. 使用双重循环遍历所有可能的下标对 (i, j)，其中 i < j。
3. 对于每一对 (i, j)，检查 words[i] 是否同时是 words[j] 的前缀和后缀。
4. 如果是，则将计数器 count 加 1。
5. 返回计数器 count 的值。

关键点:
- 使用字符串切片来检查前缀和后缀。
- 双重循环的时间复杂度为 O(n^2)，但考虑到输入长度较小，可以接受。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2 * m)，其中 n 是 words 的长度，m 是每个字符串的最大长度。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def count_prefix_suffix_pairs(words: List[str]) -> int:
    """
    函数式接口 - 统计满足条件的前后缀下标对
    """
    count = 0
    n = len(words)
    
    for i in range(n):
        for j in range(i + 1, n):
            if words[i] == words[j][:len(words[i])] and words[i] == words[j][-len(words[i]):]:
                count += 1
    
    return count


Solution = create_solution(count_prefix_suffix_pairs)