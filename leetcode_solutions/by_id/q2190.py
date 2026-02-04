# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2190
标题: Count Common Words With One Occurrence
难度: easy
链接: https://leetcode.cn/problems/count-common-words-with-one-occurrence/
题目类型: 数组、哈希表、字符串、计数
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2085. 统计出现过一次的公共字符串 - 给你两个字符串数组 words1 和 words2 ，请你返回在两个字符串数组中 都恰好出现一次 的字符串的数目。 示例 1： 输入：words1 = ["leetcode","is","amazing","as","is"], words2 = ["amazing","leetcode","is"] 输出：2 解释： - "leetcode" 在两个数组中都恰好出现一次，计入答案。 - "amazing" 在两个数组中都恰好出现一次，计入答案。 - "is" 在两个数组中都出现过，但在 words1 中出现了 2 次，不计入答案。 - "as" 在 words1 中出现了一次，但是在 words2 中没有出现过，不计入答案。 所以，有 2 个字符串在两个数组中都恰好出现了一次。 示例 2： 输入：words1 = ["b","bb","bbb"], words2 = ["a","aa","aaa"] 输出：0 解释：没有字符串在两个数组中都恰好出现一次。 示例 3： 输入：words1 = ["a","ab"], words2 = ["a","a","a","ab"] 输出：1 解释：唯一在两个数组中都出现一次的字符串是 "ab" 。 提示： * 1 <= words1.length, words2.length <= 1000 * 1 <= words1[i].length, words2[j].length <= 30 * words1[i] 和 words2[j] 都只包含小写英文字母。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表统计每个字符串在两个数组中的出现次数，然后找出在两个数组中都恰好出现一次的字符串。

算法步骤:
1. 创建两个字典，分别统计 words1 和 words2 中每个字符串的出现次数。
2. 遍历第一个字典，检查每个字符串是否在第二个字典中也恰好出现一次。
3. 统计满足条件的字符串数量并返回。

关键点:
- 使用哈希表进行高效计数。
- 只遍历一次字典即可找到所有满足条件的字符串。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是 words1 的长度，m 是 words2 的长度。
空间复杂度: O(n + m)，用于存储两个字典。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def count_common_words_with_one_occurrence(words1: List[str], words2: List[str]) -> int:
    """
    函数式接口 - 统计在两个字符串数组中都恰好出现一次的字符串的数目
    """
    # 统计 words1 中每个字符串的出现次数
    count1 = {}
    for word in words1:
        count1[word] = count1.get(word, 0) + 1

    # 统计 words2 中每个字符串的出现次数
    count2 = {}
    for word in words2:
        count2[word] = count2.get(word, 0) + 1

    # 统计在两个数组中都恰好出现一次的字符串数量
    common_count = 0
    for word, count in count1.items():
        if count == 1 and count2.get(word, 0) == 1:
            common_count += 1

    return common_count


Solution = create_solution(count_common_words_with_one_occurrence)