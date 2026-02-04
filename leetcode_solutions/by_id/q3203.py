# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3203
标题: Palindrome Rearrangement Queries
难度: hard
链接: https://leetcode.cn/problems/palindrome-rearrangement-queries/
题目类型: 哈希表、字符串、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2983. 回文串重新排列查询 - 给你一个长度为 偶数 n ，下标从 0 开始的字符串 s 。 同时给你一个下标从 0 开始的二维整数数组 queries ，其中 queries[i] = [ai, bi, ci, di] 。 对于每个查询 i ，你需要执行以下操作： * 将下标在范围 0 <= ai <= bi < n / 2 内的 子字符串 s[ai:bi] 中的字符重新排列。 * 将下标在范围 n / 2 <= ci <= di < n 内的 子字符串 s[ci:di] 中的字符重新排列。 对于每个查询，你的任务是判断执行操作后能否让 s 变成一个 回文串 。 每个查询与其他查询都是 独立的 。 请你返回一个下标从 0 开始的数组 answer ，如果第 i 个查询执行操作后，可以将 s 变为一个回文串，那么 answer[i] = true，否则为 false 。 * 子字符串 指的是一个字符串中一段连续的字符序列。 * s[x:y] 表示 s 中从下标 x 到 y 且两个端点 都包含 的子字符串。 示例 1： 输入：s = "abcabc", queries = [[1,1,3,5],[0,2,5,5]] 输出：[true,true] 解释：这个例子中，有 2 个查询： 第一个查询： - a0 = 1, b0 = 1, c0 = 3, d0 = 5 - 你可以重新排列 s[1:1] => abcabc 和 s[3:5] => abcabc 。 - 为了让 s 变为回文串，s[3:5] 可以重新排列得到 => abccba 。 - 现在 s 是一个回文串。所以 answer[0] = true 。 第二个查询： - a1 = 0, b1 = 2, c1 = 5, d1 = 5. - 你可以重新排列 s[0:2] => abcabc 和 s[5:5] => abcabc 。 - 为了让 s 变为回文串，s[0:2] 可以重新排列得到 => cbaabc 。 - 现在 s 是一个回文串，所以 answer[1] = true 。 示例 2： 输入：s = "abbcdecbba", queries = [[0,2,7,9]] 输出：[false] 解释：这个示例中，只有一个查询。 a0 = 0, b0 = 2, c0 = 7, d0 = 9. 你可以重新排列 s[0:2] => abbcdecbba 和 s[7:9] => abbcdecbba 。 无法通过重新排列这些子字符串使 s 变为一个回文串，因为 s[3:6] 不是一个回文串。 所以 answer[0] = false 。 示例 3： 输入：s = "acbcab", queries = [[1,2,4,5]] 输出：[true] 解释：这个示例中，只有一个查询。 a0 = 1, b0 = 2, c0 = 4, d0 = 5. 你可以重新排列 s[1:2] => acbcab 和 s[4:5] => acbcab 。 为了让 s 变为回文串，s[1:2] 可以重新排列得到 => abccab 。 然后 s[4:5] 重新排列得到 abccba 。 现在 s 是一个回文串，所以 answer[0] = true 。 提示： * 2 <= n == s.length <= 105 * 1 <= queries.length <= 105 * queries[i].length == 4 * ai == queries[i][0], bi == queries[i][1] * ci == queries[i][2], di == queries[i][3] * 0 <= ai <= bi < n / 2 * n / 2 <= ci <= di < n * n 是一个偶数。 * s 只包含小写英文字母。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想:
- 使用前缀和来快速计算任意子字符串的字符频率。
- 对于每个查询，检查重新排列后的子字符串是否可以使整个字符串变成回文串。

算法步骤:
1. 计算前缀和数组，用于快速计算任意子字符串的字符频率。
2. 对于每个查询，使用前缀和数组计算指定子字符串的字符频率。
3. 检查重新排列后的子字符串是否可以使整个字符串变成回文串。

关键点:
- 使用前缀和数组来优化字符频率的计算。
- 检查字符频率是否满足回文串的要求。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + q)，其中 n 是字符串 s 的长度，q 是查询的数量。
空间复杂度: O(n)，用于存储前缀和数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def can_form_palindrome(s: str, queries: List[List[int]]) -> List[bool]:
    n = len(s)
    half_n = n // 2
    prefix_sum = [[0] * 26 for _ in range(half_n + 1)]
    
    # 计算前缀和数组
    for i in range(half_n):
        for j in range(26):
            prefix_sum[i + 1][j] = prefix_sum[i][j]
        prefix_sum[i + 1][ord(s[i]) - ord('a')] += 1
        prefix_sum[i + 1][ord(s[n - 1 - i]) - ord('a')] -= 1
    
    def get_freq(left: int, right: int) -> List[int]:
        freq = [0] * 26
        for j in range(26):
            freq[j] = prefix_sum[right + 1][j] - prefix_sum[left][j]
        return freq
    
    def is_palindrome_possible(freq1: List[int], freq2: List[int]) -> bool:
        for i in range(26):
            if (freq1[i] + freq2[i]) % 2 != 0:
                return False
        return True
    
    result = []
    for a, b, c, d in queries:
        freq1 = get_freq(a, b)
        freq2 = get_freq(n - 1 - d, n - 1 - c)
        result.append(is_palindrome_possible(freq1, freq2))
    
    return result

Solution = create_solution(can_form_palindrome)