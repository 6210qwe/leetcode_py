# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3317
标题: Maximum Palindromes After Operations
难度: medium
链接: https://leetcode.cn/problems/maximum-palindromes-after-operations/
题目类型: 贪心、数组、哈希表、字符串、计数、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3035. 回文字符串的最大数量 - 给你一个下标从 0 开始的字符串数组 words ，数组的长度为 n ，且包含下标从 0 开始的若干字符串。 你可以执行以下操作 任意 次数（包括零次）： * 选择整数i、j、x和y，满足0 <= i, j < n，0 <= x < words[i].length，0 <= y < words[j].length，交换 字符 words[i][x] 和 words[j][y] 。 返回一个整数，表示在执行一些操作后，words 中可以包含的回文串的 最大 数量。 注意：在操作过程中，i 和 j 可以相等。 示例 1： 输入：words = ["abbb","ba","aa"] 输出：3 解释：在这个例子中，获得最多回文字符串的一种方式是： 选择 i = 0, j = 1, x = 0, y = 0，交换 words[0][0] 和 words[1][0] 。words 变成了 ["bbbb","aa","aa"] 。 words 中的所有字符串都是回文。 因此，可实现的回文字符串的最大数量是 3 。 示例 2： 输入：words = ["abc","ab"] 输出：2 解释：在这个例子中，获得最多回文字符串的一种方式是： 选择 i = 0, j = 1, x = 1, y = 0，交换 words[0][1] 和 words[1][0] 。words 变成了 ["aac","bb"] 。 选择 i = 0, j = 0, x = 1, y = 2，交换 words[0][1] 和 words[0][2] 。words 变成了 ["aca","bb"] 。 两个字符串都是回文 。 因此，可实现的回文字符串的最大数量是 2。 示例 3： 输入：words = ["cd","ef","a"] 输出：1 解释：在这个例子中，没有必要执行任何操作。 words 中有一个回文 "a" 。 可以证明，在执行任何次数操作后，无法得到更多回文。 因此，答案是 1 。 提示： * 1 <= words.length <= 1000 * 1 <= words[i].length <= 100 * words[i] 仅由小写英文字母组成。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过计数每个字符出现的次数，我们可以将所有字符配对来形成尽可能多的回文字符串。

算法步骤:
1. 计算所有字符的出现次数。
2. 将字符按长度进行分组，并计算每个长度的字符串数量。
3. 使用字符配对来形成回文字符串，优先处理长度为奇数的字符串。
4. 计算最终可以形成的回文字符串的最大数量。

关键点:
- 通过字符配对，我们可以确保每个字符串都能变成回文。
- 优先处理长度为奇数的字符串，因为它们需要一个中心字符。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是 words 的总长度，m 是 words 的数量。
空间复杂度: O(1)，因为字符计数和长度分组使用的额外空间是常数级的。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from leetcode_solutions.utils.solution import create_solution


def max_palindromes_after_operations(words: List[str]) -> int:
    from collections import Counter
    
    # 计算所有字符的出现次数
    char_count = Counter()
    for word in words:
        char_count += Counter(word)
    
    # 计算每个长度的字符串数量
    length_count = Counter(len(word) for word in words)
    
    # 计算可以配对的字符数量
    pairs = sum(count // 2 for count in char_count.values())
    
    # 计算可以形成的回文字符串的最大数量
    result = 0
    for length in sorted(length_count.keys()):
        if length % 2 == 0:
            # 长度为偶数的字符串可以直接使用成对的字符
            result += min(length_count[length], pairs // (length // 2))
            pairs -= min(length_count[length], pairs // (length // 2)) * (length // 2)
        else:
            # 长度为奇数的字符串需要一个中心字符
            result += min(length_count[length], pairs // ((length - 1) // 2))
            pairs -= min(length_count[length], pairs // ((length - 1) // 2)) * ((length - 1) // 2)
    
    return result


Solution = create_solution(max_palindromes_after_operations)