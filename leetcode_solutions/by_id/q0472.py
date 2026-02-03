# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 472
标题: Concatenated Words
难度: hard
链接: https://leetcode.cn/problems/concatenated-words/
题目类型: 深度优先搜索、字典树、数组、字符串、动态规划、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
472. 连接词 - 给你一个 不含重复 单词的字符串数组 words ，请你找出并返回 words 中的所有 连接词 。 连接词 定义为：一个完全由给定数组中的至少两个较短单词（不一定是不同的两个单词）组成的字符串。 示例 1： 输入：words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"] 输出：["catsdogcats","dogcatsdog","ratcatdogcat"] 解释："catsdogcats" 由 "cats", "dog" 和 "cats" 组成; "dogcatsdog" 由 "dog", "cats" 和 "dog" 组成; "ratcatdogcat" 由 "rat", "cat", "dog" 和 "cat" 组成。 示例 2： 输入：words = ["cat","dog","catdog"] 输出：["catdog"] 提示： * 1 <= words.length <= 104 * 1 <= words[i].length <= 30 * words[i] 仅由小写英文字母组成。 * words 中的所有字符串都是 唯一 的。 * 1 <= sum(words[i].length) <= 105
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 动态规划+字典树，判断单词是否由其他单词组成

算法步骤:
1. 按长度排序单词
2. 对每个单词，使用DP判断是否能由更短的单词组成
3. 使用集合存储已处理的单词，加速查找

关键点:
- DP判断单词分解
- 时间复杂度O(n*L^2)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n*L^2) - n为单词数，L为平均长度
空间复杂度: O(n*L) - 存储单词集合
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def concatenated_words(words: List[str]) -> List[str]:
    """
    函数式接口 - 连接词
    
    实现思路:
    动态规划：判断单词是否能由其他更短的单词组成。
    
    Args:
        words: 单词数组
        
    Returns:
        所有连接词
        
    Example:
        >>> concatenated_words(["cat","cats","catsdogcats","dog","dogcatsdog"])
        ['catsdogcats', 'dogcatsdog']
    """
    # 按长度排序
    words.sort(key=len)
    word_set = set()
    result = []
    
    for word in words:
        if not word:
            continue
        
        # DP判断word是否能由word_set中的单词组成
        dp = [False] * (len(word) + 1)
        dp[0] = True
        
        for i in range(1, len(word) + 1):
            for j in range(i):
                if dp[j] and word[j:i] in word_set:
                    dp[i] = True
                    break
        
        if dp[len(word)]:
            result.append(word)
        
        word_set.add(word)
    
    return result


# 自动生成Solution类（无需手动编写）
Solution = create_solution(concatenated_words)
