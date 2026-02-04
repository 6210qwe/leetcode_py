# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2010
标题: Check if Word Equals Summation of Two Words
难度: easy
链接: https://leetcode.cn/problems/check-if-word-equals-summation-of-two-words/
题目类型: 字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1880. 检查某单词是否等于两单词之和 - 字母的 字母值 取决于字母在字母表中的位置，从 0 开始 计数。即，'a' -> 0、'b' -> 1、'c' -> 2，以此类推。 对某个由小写字母组成的字符串 s 而言，其 数值 就等于将 s 中每个字母的 字母值 按顺序 连接 并 转换 成对应整数。 * 例如，s = "acb" ，依次连接每个字母的字母值可以得到 "021" ，转换为整数得到 21 。 给你三个字符串 firstWord、secondWord 和 targetWord ，每个字符串都由从 'a' 到 'j' （含 'a' 和 'j' ）的小写英文字母组成。 如果 firstWord 和 secondWord 的 数值之和 等于 targetWord 的数值，返回 true ；否则，返回 false 。 示例 1： 输入：firstWord = "acb", secondWord = "cba", targetWord = "cdb" 输出：true 解释： firstWord 的数值为 "acb" -> "021" -> 21 secondWord 的数值为 "cba" -> "210" -> 210 targetWord 的数值为 "cdb" -> "231" -> 231 由于 21 + 210 == 231 ，返回 true 示例 2： 输入：firstWord = "aaa", secondWord = "a", targetWord = "aab" 输出：false 解释： firstWord 的数值为 "aaa" -> "000" -> 0 secondWord 的数值为 "a" -> "0" -> 0 targetWord 的数值为 "aab" -> "001" -> 1 由于 0 + 0 != 1 ，返回 false 示例 3： 输入：firstWord = "aaa", secondWord = "a", targetWord = "aaaa" 输出：true 解释： firstWord 的数值为 "aaa" -> "000" -> 0 secondWord 的数值为 "a" -> "0" -> 0 targetWord 的数值为 "aaaa" -> "0000" -> 0 由于 0 + 0 == 0 ，返回 true 提示： * 1 <= firstWord.length, secondWord.length, targetWord.length <= 8 * firstWord、secondWord 和 targetWord 仅由从 'a' 到 'j' （含 'a' 和 'j' ）的小写英文字母组成。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 将每个字符串转换为其对应的数值，然后检查 firstWord 和 secondWord 的数值之和是否等于 targetWord 的数值。

算法步骤:
1. 定义一个辅助函数 `word_to_num`，将字符串转换为其对应的数值。
2. 使用 `word_to_num` 函数计算 firstWord、secondWord 和 targetWord 的数值。
3. 检查 firstWord 和 secondWord 的数值之和是否等于 targetWord 的数值。

关键点:
- 字符串转换为数值时，需要将每个字符映射到其对应的数字。
- 使用字符串拼接来构建数值，最后转换为整数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是字符串的最大长度。我们需要遍历每个字符串一次。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def word_to_num(word: str) -> int:
    """将字符串转换为其对应的数值"""
    return int("".join(str(ord(char) - ord('a')) for char in word))


def solution_function_name(firstWord: str, secondWord: str, targetWord: str) -> bool:
    """
    函数式接口 - 检查 firstWord 和 secondWord 的数值之和是否等于 targetWord 的数值
    """
    num_first = word_to_num(firstWord)
    num_second = word_to_num(secondWord)
    num_target = word_to_num(targetWord)
    
    return num_first + num_second == num_target


Solution = create_solution(solution_function_name)