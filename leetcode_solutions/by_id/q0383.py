# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 383
标题: Ransom Note
难度: easy
链接: https://leetcode.cn/problems/ransom-note/
题目类型: 哈希表、字符串、计数
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
383. 赎金信 - 给你两个字符串：ransomNote 和 magazine ，判断 ransomNote 能不能由 magazine 里面的字符构成。 如果可以，返回 true ；否则返回 false 。 magazine 中的每个字符只能在 ransomNote 中使用一次。 示例 1： 输入：ransomNote = "a", magazine = "b" 输出：false 示例 2： 输入：ransomNote = "aa", magazine = "ab" 输出：false 示例 3： 输入：ransomNote = "aa", magazine = "aab" 输出：true 提示： * 1 <= ransomNote.length, magazine.length <= 105 * ransomNote 和 magazine 由小写英文字母组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 计数比较或哈希表：统计 magazine 中每个字符的出现次数，再用 ransomNote 中的消耗进行检验

算法步骤:
1. 初始化一个长度为 26 的整型数组 cnt（或使用字典/Counter），用于统计 magazine 中各字符的频次。
2. 遍历 magazine，对每个字符 ch 执行 cnt[ch - 'a']++。
3. 再遍历 ransomNote，对于每个字符 ch：
   - 如果 cnt[ch - 'a'] 已经是 0，说明 magazine 中该字符余量不足，立即返回 False；
   - 否则先将 cnt[ch - 'a']--，表示消耗一个字符。
4. 如果顺利遍历完整个 ransomNote 而未提前返回 False，则说明可以构成，返回 True。

关键点:
- 由于只包含小写字母，使用固定长度的数组比哈希表更高效。
- 可以在遍历 ransomNote 前做一个简单剪枝：若 ransomNote 长度大于 magazine，则直接返回 False。
- 注意 magazine 中的字符只能使用一次，每次匹配都要减少计数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m + n) - m 和 n 分别为 ransomNote 和 magazine 的长度，各遍历一次。
空间复杂度: O(1) - 只使用常数大小的计数数组（26 个字母）。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def can_construct(ransomNote: str, magazine: str) -> bool:
    """
    判断 ransomNote 是否可以由 magazine 中的字符构成。

    使用固定长度为 26 的计数数组统计 magazine 中各字符出现次数，
    再依次消耗 ransomNote 中的字符，只要有一种字符不足则返回 False。
    """
    if len(ransomNote) > len(magazine):
        return False

    cnt = [0] * 26
    for ch in magazine:
        cnt[ord(ch) - 97] += 1

    for ch in ransomNote:
        idx = ord(ch) - 97
        if cnt[idx] == 0:
            return False
        cnt[idx] -= 1

    return True


def ransom_note(ransomNote: str, magazine: str) -> bool:
    """
    函数式接口封装，内部调用 can_construct。
    """
    return can_construct(ransomNote, magazine)


# 自动生成Solution类（无需手动编写）
Solution = create_solution(can_construct)
