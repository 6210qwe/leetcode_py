# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 926
标题: Find and Replace Pattern
难度: medium
链接: https://leetcode.cn/problems/find-and-replace-pattern/
题目类型: 数组、哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
890. 查找和替换模式 - 你有一个单词列表 words 和一个模式 pattern，你想知道 words 中的哪些单词与模式匹配。 如果存在字母的排列 p ，使得将模式中的每个字母 x 替换为 p(x) 之后，我们就得到了所需的单词，那么单词与模式是匹配的。 （回想一下，字母的排列是从字母到字母的双射：每个字母映射到另一个字母，没有两个字母映射到同一个字母。） 返回 words 中与给定模式匹配的单词列表。 你可以按任何顺序返回答案。 示例： 输入：words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb" 输出：["mee","aqq"] 解释： "mee" 与模式匹配，因为存在排列 {a -> m, b -> e, ...}。 "ccc" 与模式不匹配，因为 {a -> c, b -> c, ...} 不是排列。 因为 a 和 b 映射到同一个字母。 提示： * 1 <= pattern.length <= 20 * 1 <= words.length <= 50 * words[i].length == pattern.length * pattern 和 words[i] 只包含小写英文字母。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用双射来检查每个单词是否与模式匹配。

算法步骤:
1. 对于每个单词，创建两个字典来记录从单词到模式和从模式到单词的映射。
2. 遍历单词和模式的字符，检查当前字符是否已经存在于映射中：
   - 如果存在，检查映射是否一致。
   - 如果不存在，建立新的映射关系。
3. 如果所有字符都匹配，则将该单词加入结果列表。

关键点:
- 使用两个字典来确保双向映射的一致性。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m)，其中 n 是 words 的长度，m 是 pattern 的长度。
空间复杂度: O(m)，用于存储映射关系。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def find_and_replace_pattern(words: List[str], pattern: str) -> List[str]:
    """
    函数式接口 - 查找与模式匹配的单词列表
    """
    def matches(word: str, pattern: str) -> bool:
        if len(word) != len(pattern):
            return False
        
        word_to_pattern = {}
        pattern_to_word = {}
        
        for w_char, p_char in zip(word, pattern):
            if w_char in word_to_pattern:
                if word_to_pattern[w_char] != p_char:
                    return False
            else:
                word_to_pattern[w_char] = p_char
            
            if p_char in pattern_to_word:
                if pattern_to_word[p_char] != w_char:
                    return False
            else:
                pattern_to_word[p_char] = w_char
        
        return True
    
    return [word for word in words if matches(word, pattern)]


Solution = create_solution(find_and_replace_pattern)