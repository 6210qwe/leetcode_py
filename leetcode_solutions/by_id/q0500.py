# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 500
标题: Keyboard Row
难度: easy
链接: https://leetcode.cn/problems/keyboard-row/
题目类型: 数组、哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
500. 键盘行 - 给你一个字符串数组 words ，只返回可以使用在 美式键盘 同一行的字母打印出来的单词。键盘如下图所示。 请注意，字符串 不区分大小写，相同字母的大小写形式都被视为在同一行。 美式键盘 中： * 第一行由字符 "qwertyuiop" 组成。 * 第二行由字符 "asdfghjkl" 组成。 * 第三行由字符 "zxcvbnm" 组成。 American keyboard [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/10/12/keyboard.png] 示例 1： 输入：words = ["Hello","Alaska","Dad","Peace"] 输出：["Alaska","Dad"] 解释： 由于不区分大小写，"a" 和 "A" 都在美式键盘的第二行。 示例 2： 输入：words = ["omk"] 输出：[] 示例 3： 输入：words = ["adsdf","sfd"] 输出：["adsdf","sfd"] 提示： * 1 <= words.length <= 20 * 1 <= words[i].length <= 100 * words[i] 由英文字母（小写和大写字母）组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表存储每行的字符集合，然后检查每个单词的所有字符是否都在同一行。

算法步骤:
1. 创建三个集合，分别存储键盘第一行、第二行和第三行的字符。
2. 对于每个单词，将其转换为小写，并检查其所有字符是否都在同一个集合中。
3. 如果是，则将该单词添加到结果列表中。

关键点:
- 使用集合进行快速查找。
- 将单词转换为小写以忽略大小写差异。
- 优化时间和空间复杂度。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m) - 其中 n 是单词的数量，m 是单词的平均长度。
空间复杂度: O(1) - 除了输入和输出外，使用的额外空间是常数级别的。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def keyboard_row(words: List[str]) -> List[str]:
    """
    函数式接口 - 返回可以使用在美式键盘同一行的字母打印出来的单词
    
    实现思路:
    使用哈希表存储每行的字符集合，然后检查每个单词的所有字符是否都在同一行。

    Args:
        words: 字符串数组
        
    Returns:
        可以使用在美式键盘同一行的字母打印出来的单词列表
        
    Example:
        >>> keyboard_row(["Hello", "Alaska", "Dad", "Peace"])
        ['Alaska', 'Dad']
    """
    # 定义键盘行的字符集合
    row1 = set("qwertyuiop")
    row2 = set("asdfghjkl")
    row3 = set("zxcvbnm")

    def is_same_row(word: str) -> bool:
        word_set = set(word.lower())
        return word_set.issubset(row1) or word_set.issubset(row2) or word_set.issubset(row3)

    # 过滤出符合条件的单词
    return [word for word in words if is_same_row(word)]


# 自动生成Solution类（无需手动编写）
Solution = create_solution(keyboard_row)