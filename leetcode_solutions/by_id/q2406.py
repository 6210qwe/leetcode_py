# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2406
标题: Decode the Message
难度: easy
链接: https://leetcode.cn/problems/decode-the-message/
题目类型: 哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2325. 解密消息 - 给你字符串 key 和 message ，分别表示一个加密密钥和一段加密消息。解密 message 的步骤如下： 1. 使用 key 中 26 个英文小写字母第一次出现的顺序作为替换表中的字母 顺序 。 2. 将替换表与普通英文字母表对齐，形成对照表。 3. 按照对照表 替换 message 中的每个字母。 4. 空格 ' ' 保持不变。 * 例如，key = "happy boy"（实际的加密密钥会包含字母表中每个字母 至少一次），据此，可以得到部分对照表（'h' -> 'a'、'a' -> 'b'、'p' -> 'c'、'y' -> 'd'、'b' -> 'e'、'o' -> 'f'）。 返回解密后的消息。 示例 1： [https://assets.leetcode.com/uploads/2022/05/08/ex1new4.jpg] 输入：key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv" 输出："this is a secret" 解释：对照表如上图所示。 提取 "the quick brown fox jumps over the lazy dog" 中每个字母的首次出现可以得到替换表。 示例 2： [https://assets.leetcode.com/uploads/2022/05/08/ex2new.jpg] 输入：key = "eljuxhpwnyrdgtqkviszcfmabo", message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb" 输出："the five boxing wizards jump quickly" 解释：对照表如上图所示。 提取 "eljuxhpwnyrdgtqkviszcfmabo" 中每个字母的首次出现可以得到替换表。 提示： * 26 <= key.length <= 2000 * key 由小写英文字母及 ' ' 组成 * key 包含英文字母表中每个字符（'a' 到 'z'）至少一次 * 1 <= message.length <= 2000 * message 由小写英文字母和 ' ' 组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: [TODO]

算法步骤:
1. [TODO]
2. [TODO]

关键点:
- [TODO]
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O([TODO])
空间复杂度: O([TODO])
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(params):
    """
    函数式接口 - [TODO] 实现
    """
    # TODO: 实现最优解法
    pass


Solution = create_solution(solution_function_name)
