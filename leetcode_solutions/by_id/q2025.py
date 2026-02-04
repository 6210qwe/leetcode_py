# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2025
标题: Redistribute Characters to Make All Strings Equal
难度: easy
链接: https://leetcode.cn/problems/redistribute-characters-to-make-all-strings-equal/
题目类型: 哈希表、字符串、计数
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1897. 重新分配字符使所有字符串都相等 - 给你一个字符串数组 words（下标 从 0 开始 计数）。 在一步操作中，需先选出两个 不同 下标 i 和 j，其中 words[i] 是一个非空字符串，接着将 words[i] 中的 任一 字符移动到 words[j] 中的 任一 位置上。 如果执行任意步操作可以使 words 中的每个字符串都相等，返回 true ；否则，返回 false 。 示例 1： 输入：words = ["abc","aabc","bc"] 输出：true 解释：将 words[1] 中的第一个 'a' 移动到 words[2] 的最前面。 使 words[1] = "abc" 且 words[2] = "abc" 。 所有字符串都等于 "abc" ，所以返回 true 。 示例 2： 输入：words = ["ab","a"] 输出：false 解释：执行操作无法使所有字符串都相等。 提示： * 1 <= words.length <= 100 * 1 <= words[i].length <= 100 * words[i] 由小写英文字母组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表统计每个字符的总出现次数，然后检查每个字符的出现次数是否能被字符串的数量整除。

算法步骤:
1. 初始化一个哈希表 `char_count` 来记录每个字符的总出现次数。
2. 遍历每个字符串，更新 `char_count`。
3. 检查每个字符的出现次数是否能被字符串的数量整除，如果不能则返回 False，否则返回 True。

关键点:
- 使用哈希表来统计字符出现次数。
- 检查字符出现次数是否能被字符串数量整除。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m)，其中 n 是字符串数组的长度，m 是每个字符串的平均长度。
空间复杂度: O(1)，因为字符集是固定的（26个小写字母）。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def can_redistribute_characters(words: List[str]) -> bool:
    """
    函数式接口 - 判断是否可以通过重新分配字符使所有字符串都相等
    """
    from collections import Counter
    
    # 统计所有字符的总出现次数
    char_count = Counter()
    for word in words:
        char_count += Counter(word)
    
    # 检查每个字符的出现次数是否能被字符串的数量整除
    num_words = len(words)
    for count in char_count.values():
        if count % num_words != 0:
            return False
    
    return True


Solution = create_solution(can_redistribute_characters)