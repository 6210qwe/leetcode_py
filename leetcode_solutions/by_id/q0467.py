# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 467
标题: Unique Substrings in Wraparound String
难度: medium
链接: https://leetcode.cn/problems/unique-substrings-in-wraparound-string/
题目类型: 字符串、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
467. 环绕字符串中唯一的子字符串 - 定义字符串 base 为一个 "abcdefghijklmnopqrstuvwxyz" 无限环绕的字符串，所以 base 看起来是这样的： * "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....". 给你一个字符串 s ，请你统计并返回 s 中有多少 不同非空子串 也在 base 中出现。 示例 1： 输入：s = "a" 输出：1 解释：字符串 s 的子字符串 "a" 在 base 中出现。 示例 2： 输入：s = "cac" 输出：2 解释：字符串 s 有两个子字符串 ("a", "c") 在 base 中出现。 示例 3： 输入：s = "zab" 输出：6 解释：字符串 s 有六个子字符串 ("z", "a", "b", "za", "ab", and "zab") 在 base 中出现。 提示： * 1 <= s.length <= 105 * s 由小写英文字母组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 动态规划，记录以每个字符结尾的最长连续子串长度

算法步骤:
1. 遍历字符串，计算以每个字符结尾的最长连续子串长度
2. 对于每个字符，以它结尾的子串数量等于连续长度
3. 使用字典记录每个字符的最大连续长度，避免重复计算

关键点:
- 动态规划记录连续长度
- 使用字典去重
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 遍历字符串一次
空间复杂度: O(1) - 最多26个字符
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def unique_substrings_in_wraparound_string(s: str) -> int:
    """
    函数式接口 - 环绕字符串中唯一的子字符串
    
    实现思路:
    动态规划：记录以每个字符结尾的最长连续子串长度。
    
    Args:
        s: 输入字符串
        
    Returns:
        不同非空子串的数量
        
    Example:
        >>> unique_substrings_in_wraparound_string("zab")
        6
    """
    # 记录以每个字符结尾的最长连续子串长度
    max_len = {}
    
    # 当前连续子串长度
    current_len = 0
    
    for i, char in enumerate(s):
        if i > 0 and (ord(char) - ord(s[i-1]) == 1 or ord(char) - ord(s[i-1]) == -25):
            # 连续
            current_len += 1
        else:
            # 不连续，重新开始
            current_len = 1
        
        # 更新以当前字符结尾的最大长度
        max_len[char] = max(max_len.get(char, 0), current_len)
    
    return sum(max_len.values())


# 自动生成Solution类（无需手动编写）
Solution = create_solution(unique_substrings_in_wraparound_string)
