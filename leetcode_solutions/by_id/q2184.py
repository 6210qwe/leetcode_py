# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2184
标题: Check if an Original String Exists Given Two Encoded Strings
难度: hard
链接: https://leetcode.cn/problems/check-if-an-original-string-exists-given-two-encoded-strings/
题目类型: 字符串、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2060. 同源字符串检测 - 原字符串由小写字母组成，可以按下述步骤编码： * 任意将其 分割 为由若干 非空 子字符串组成的一个 序列 。 * 任意选择序列中的一些元素（也可能不选择），然后将这些元素替换为元素各自的长度（作为一个数字型的字符串）。 * 重新 顺次连接 序列，得到编码后的字符串。 例如，编码 "abcdefghijklmnop" 的一种方法可以描述为： * 将原字符串分割得到一个序列：["ab", "cdefghijklmn", "o", "p"] 。 * 选出其中第二个和第三个元素并分别替换为它们自身的长度。序列变为 ["ab", "12", "1", "p"] 。 * 重新顺次连接序列中的元素，得到编码后的字符串："ab121p" 。 给你两个编码后的字符串 s1 和 s2 ，由小写英文字母和数字 1-9 组成。如果存在能够同时编码得到 s1 和 s2 原字符串，返回 true ；否则，返回 false。 注意：生成的测试用例满足 s1 和 s2 中连续数字数不超过 3 。 示例 1： 输入：s1 = "internationalization", s2 = "i18n" 输出：true 解释："internationalization" 可以作为原字符串 - "internationalization" -> 分割： ["internationalization"] -> 不替换任何元素 -> 连接： "internationalization"，得到 s1 - "internationalization" -> 分割： ["i", "nternationalizatio", "n"] -> 替换： ["i", "18", "n"] -> 连接： "i18n"，得到 s2 示例 2： 输入：s1 = "l123e", s2 = "44" 输出：true 解释："leetcode" 可以作为原字符串 - "leetcode" -> 分割： ["l", "e", "et", "cod", "e"] -> 替换： ["l", "1", "2", "3", "e"] -> 连接： "l123e"，得到 s1 - "leetcode" -> 分割： ["leet", "code"] -> 替换： ["4", "4"] -> 连接： "44"，得到 s2 示例 3： 输入：s1 = "a5b", s2 = "c5b" 输出：false 解释：不存在这样的原字符串 - 编码为 s1 的字符串必须以字母 'a' 开头 - 编码为 s2 的字符串必须以字母 'c' 开头 示例 4： 输入：s1 = "112s", s2 = "g841" 输出：true 解释："gaaaaaaaaaaaas" 可以作为原字符串 - "gaaaaaaaaaaaas" -> 分割： ["g", "aaaaaaaaaaaa", "s"] -> 替换： ["1", "12", "s"] -> 连接： "112s"，得到 s1 - "gaaaaaaaaaaaas" -> 分割： ["g", "aaaaaaaa", "aaaa", "s"] -> 替换： ["g", "8", "4", "1"] -> 连接 "g841"，得到 s2 示例 5： 输入：s1 = "ab", s2 = "a2" 输出：false 解释：不存在这样的原字符串 - 编码为 s1 的字符串由两个字母组成 - 编码为 s2 的字符串由三个字母组成 提示： * 1 <= s1.length, s2.length <= 40 * s1 和 s2 仅由数字 1-9 和小写英文字母组成 * s1 和 s2 中连续数字数不超过 3
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来解决这个问题。我们定义 dp[i][j] 表示 s1 的前 i 个字符和 s2 的前 j 个字符是否可以由同一个原字符串编码得到。

算法步骤:
1. 初始化一个二维数组 dp，大小为 (len(s1) + 1) x (len(s2) + 1)，初始值为 False。
2. 设置 dp[0][0] 为 True，表示空字符串可以由空字符串编码得到。
3. 遍历 s1 和 s2 的每个字符，根据字符是字母还是数字来更新 dp 数组。
4. 如果当前字符是字母，则检查对应的字符是否相同，如果相同则更新 dp 数组。
5. 如果当前字符是数字，则计算可能的长度范围，并更新 dp 数组。
6. 最后返回 dp[len(s1)][len(s2)] 的值。

关键点:
- 动态规划的状态转移方程需要考虑字母和数字的不同情况。
- 数字的处理需要考虑多个连续数字的情况。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m * 1000)，其中 n 和 m 分别是 s1 和 s2 的长度。最坏情况下，每个数字可以表示的最大长度为 1000。
空间复杂度: O(n * m)，dp 数组的大小。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def can_be_encoded(s1: str, s2: str) -> bool:
    len1, len2 = len(s1), len(s2)
    dp = [[False] * (len2 + 1) for _ in range(len1 + 1)]
    dp[0][0] = True

    def get_length_range(s: str, start: int) -> (int, int):
        length = 0
        while start < len(s) and s[start].isdigit():
            length = length * 10 + int(s[start])
            start += 1
        return max(1, length), min(1000, length)

    for i in range(len1 + 1):
        for j in range(len2 + 1):
            if i > 0 and s1[i - 1].isalpha() and j > 0 and s2[j - 1].isalpha():
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
            elif i > 0 and s1[i - 1].isdigit():
                min_len, max_len = get_length_range(s1, i - 1)
                for k in range(j, max(0, j - max_len - 1), -1):
                    if dp[i - (i - k + 1)][k]:
                        dp[i][j] = True
                        break
            elif j > 0 and s2[j - 1].isdigit():
                min_len, max_len = get_length_range(s2, j - 1)
                for k in range(i, max(0, i - max_len - 1), -1):
                    if dp[k][j - (j - k + 1)]:
                        dp[i][j] = True
                        break
            else:
                dp[i][j] = dp[i - 1][j - 1]

    return dp[len1][len2]


Solution = create_solution(can_be_encoded)