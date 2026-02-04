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
核心思想: 使用哈希表构建替换表，并根据替换表解码消息。

算法步骤:
1. 构建替换表：遍历 key 字符串，记录每个字母第一次出现的位置，并将其映射到对应的普通英文字母。
2. 解码消息：遍历 message 字符串，根据替换表将每个字母替换为对应的普通英文字母，空格保持不变。

关键点:
- 使用字典来存储替换表，确保快速查找。
- 只记录每个字母第一次出现的位置，避免重复。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是 key 的长度，m 是 message 的长度。构建替换表的时间复杂度为 O(n)，解码消息的时间复杂度为 O(m)。
空间复杂度: O(1)，替换表的大小固定为 26 个字母。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def decode_message(key: str, message: str) -> str:
    """
    解密消息
    """
    # 构建替换表
    replacement_table = {}
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    idx = 0
    
    for char in key:
        if char not in replacement_table and char != ' ':
            replacement_table[char] = alphabet[idx]
            idx += 1
            if idx == 26:
                break
    
    # 解码消息
    decoded_message = ''
    for char in message:
        if char == ' ':
            decoded_message += ' '
        else:
            decoded_message += replacement_table[char]
    
    return decoded_message


Solution = create_solution(decode_message)