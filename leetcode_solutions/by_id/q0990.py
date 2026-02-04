# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 990
标题: Verifying an Alien Dictionary
难度: easy
链接: https://leetcode.cn/problems/verifying-an-alien-dictionary/
题目类型: 数组、哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
953. 验证外星语词典 - 某种外星语也使用英文小写字母，但可能顺序 order 不同。字母表的顺序（order）是一些小写字母的排列。 给定一组用外星语书写的单词 words，以及其字母表的顺序 order，只有当给定的单词在这种外星语中按字典序排列时，返回 true；否则，返回 false。 示例 1： 输入：words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz" 输出：true 解释：在该语言的字母表中，'h' 位于 'l' 之前，所以单词序列是按字典序排列的。 示例 2： 输入：words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz" 输出：false 解释：在该语言的字母表中，'d' 位于 'l' 之后，那么 words[0] > words[1]，因此单词序列不是按字典序排列的。 示例 3： 输入：words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz" 输出：false 解释：当前三个字符 "app" 匹配时，第二个字符串相对短一些，然后根据词典编纂规则 "apple" > "app"，因为 'l' > '∅'，其中 '∅' 是空白字符，定义为比任何其他字符都小（更多信息https://baike.baidu.com/item/%E5%AD%97%E5%85%B8%E5%BA%8F）。 提示： * 1 <= words.length <= 100 * 1 <= words[i].length <= 20 * order.length == 26 * 在 words[i] 和 order 中的所有字符都是英文小写字母。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用一个映射表来存储外星语字母表的顺序，然后逐对比较相邻单词是否按字典序排列。

算法步骤:
1. 创建一个映射表，将外星语字母表中的每个字母映射到其对应的索引。
2. 逐对比较相邻单词，检查它们是否按字典序排列。
3. 如果发现不满足字典序的情况，返回 False；否则，返回 True。

关键点:
- 使用映射表来快速查找每个字母的顺序。
- 逐对比较相邻单词，确保整个列表按字典序排列。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m)，其中 n 是单词的数量，m 是单词的最大长度。
空间复杂度: O(1)，映射表的大小固定为 26。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def is_alien_sorted(words: List[str], order: str) -> bool:
    """
    函数式接口 - 判断给定的单词列表是否按外星语字母表的顺序排列
    """
    # 创建映射表
    order_index = {char: idx for idx, char in enumerate(order)}

    # 逐对比较相邻单词
    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]
        for j in range(min(len(word1), len(word2))):
            if word1[j] != word2[j]:
                if order_index[word1[j]] > order_index[word2[j]]:
                    return False
                break
        else:
            # 如果所有字符都相同，但 word1 比 word2 长，则不满足字典序
            if len(word1) > len(word2):
                return False

    return True


Solution = create_solution(is_alien_sorted)