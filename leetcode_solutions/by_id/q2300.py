# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2300
标题: Construct String With Repeat Limit
难度: medium
链接: https://leetcode.cn/problems/construct-string-with-repeat-limit/
题目类型: 贪心、哈希表、字符串、计数、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2182. 构造限制重复的字符串 - 给你一个字符串 s 和一个整数 repeatLimit ，用 s 中的字符构造一个新字符串 repeatLimitedString ，使任何字母 连续 出现的次数都不超过 repeatLimit 次。你不必使用 s 中的全部字符。 返回 字典序最大的 repeatLimitedString 。 如果在字符串 a 和 b 不同的第一个位置，字符串 a 中的字母在字母表中出现时间比字符串 b 对应的字母晚，则认为字符串 a 比字符串 b 字典序更大 。如果字符串中前 min(a.length, b.length) 个字符都相同，那么较长的字符串字典序更大。 示例 1： 输入：s = "cczazcc", repeatLimit = 3 输出："zzcccac" 解释：使用 s 中的所有字符来构造 repeatLimitedString "zzcccac"。 字母 'a' 连续出现至多 1 次。 字母 'c' 连续出现至多 3 次。 字母 'z' 连续出现至多 2 次。 因此，没有字母连续出现超过 repeatLimit 次，字符串是一个有效的 repeatLimitedString 。 该字符串是字典序最大的 repeatLimitedString ，所以返回 "zzcccac" 。 注意，尽管 "zzcccca" 字典序更大，但字母 'c' 连续出现超过 3 次，所以它不是一个有效的 repeatLimitedString 。 示例 2： 输入：s = "aababab", repeatLimit = 2 输出："bbabaa" 解释： 使用 s 中的一些字符来构造 repeatLimitedString "bbabaa"。 字母 'a' 连续出现至多 2 次。 字母 'b' 连续出现至多 2 次。 因此，没有字母连续出现超过 repeatLimit 次，字符串是一个有效的 repeatLimitedString 。 该字符串是字典序最大的 repeatLimitedString ，所以返回 "bbabaa" 。 注意，尽管 "bbabaaa" 字典序更大，但字母 'a' 连续出现超过 2 次，所以它不是一个有效的 repeatLimitedString 。 提示： * 1 <= repeatLimit <= s.length <= 105 * s 由小写英文字母组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法和双指针方法来构建字典序最大的字符串。

算法步骤:
1. 统计每个字符的频率。
2. 从字典序最大的字符开始，尽可能多地添加字符，直到达到 repeatLimit。
3. 如果当前字符达到 repeatLimit，尝试添加下一个字典序最大的字符。
4. 如果无法添加更多字符，结束构建。

关键点:
- 使用双指针方法来管理当前字符和下一个字符。
- 确保每个字符的连续出现次数不超过 repeatLimit。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是字符串 s 的长度。我们需要遍历字符串并进行一些常数时间的操作。
空间复杂度: O(1)，因为字母表的大小是固定的（26 个小写字母），所以使用的额外空间是常数级别的。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(s: str, repeatLimit: int) -> str:
    """
    函数式接口 - 构造限制重复的字符串
    """
    # 统计每个字符的频率
    char_count = [0] * 26
    for char in s:
        char_count[ord(char) - ord('a')] += 1
    
    result = []
    i = 25  # 从字典序最大的字符开始
    j = 24  # 下一个字典序最大的字符
    
    while i >= 0:
        if char_count[i] > 0:
            # 尽可能多地添加当前字符
            add_count = min(char_count[i], repeatLimit)
            result.append(chr(i + ord('a')) * add_count)
            char_count[i] -= add_count
            
            if char_count[i] > 0:
                # 当前字符达到 repeatLimit，尝试添加下一个字符
                while j >= 0 and char_count[j] == 0:
                    j -= 1
                if j >= 0:
                    result.append(chr(j + ord('a')))
                    char_count[j] -= 1
                    j = min(j, 24)  # 更新 j 为下一个字典序最大的字符
                else:
                    break
        else:
            i -= 1
            j = i - 1
    
    return ''.join(result)


Solution = create_solution(solution_function_name)