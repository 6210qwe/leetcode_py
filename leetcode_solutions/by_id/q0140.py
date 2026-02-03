# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 140
标题: Word Break II
难度: hard
链接: https://leetcode.cn/problems/word-break-ii/
题目类型: 字典树、记忆化搜索、数组、哈希表、字符串、动态规划、回溯
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
140. 单词拆分 II - 给定一个字符串 s 和一个字符串字典 wordDict ，在字符串 s 中增加空格来构建一个句子，使得句子中所有的单词都在词典中。以任意顺序 返回所有这些可能的句子。 注意：词典中的同一个单词可能在分段中被重复使用多次。 示例 1： 输入:s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"] 输出:["cats and dog","cat sand dog"] 示例 2： 输入:s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"] 输出:["pine apple pen apple","pineapple pen apple","pine applepen apple"] 解释: 注意你可以重复使用字典中的单词。 示例 3： 输入:s = "catsandog", wordDict = ["cats","dog","sand","and","cat"] 输出:[] 提示： * 1 <= s.length <= 20 * 1 <= wordDict.length <= 1000 * 1 <= wordDict[i].length <= 10 * s 和 wordDict[i] 仅有小写英文字母组成 * wordDict 中所有字符串都 不同
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用回溯和记忆化搜索，找出所有可能的拆分方式

算法步骤:
1. 使用记忆化搜索避免重复计算
2. 对于每个位置，尝试所有可能的单词
3. 如果当前子串在字典中，递归处理剩余部分
4. 合并所有可能的拆分结果

关键点:
- 使用记忆化优化性能
- 时间复杂度O(2^n)，空间复杂度O(2^n)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(2^n) - 最坏情况下需要尝试所有可能的拆分
空间复杂度: O(2^n) - 存储所有可能的拆分结果
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Dict
from leetcode_solutions.utils.solution import create_solution


def word_break_ii(s: str, wordDict: List[str]) -> List[str]:
    """
    函数式接口 - 找出所有可能的单词拆分方式
    
    实现思路:
    使用回溯和记忆化搜索，找出所有可能的拆分方式。
    
    Args:
        s: 待拆分的字符串
        wordDict: 单词字典
        
    Returns:
        所有可能的拆分句子列表
        
    Example:
        >>> word_break_ii("catsanddog", ["cat","cats","and","sand","dog"])
        ['cats and dog', 'cat sand dog']
    """
    word_set = set(wordDict)
    memo: Dict[str, List[str]] = {}
    
    def backtrack(substring: str) -> List[str]:
        if substring in memo:
            return memo[substring]
        
        if not substring:
            return [""]
        
        result = []
        for i in range(1, len(substring) + 1):
            word = substring[:i]
            if word in word_set:
                rest = backtrack(substring[i:])
                for r in rest:
                    if r:
                        result.append(word + " " + r)
                    else:
                        result.append(word)
        
        memo[substring] = result
        return result
    
    return backtrack(s)


# 自动生成Solution类（无需手动编写）
Solution = create_solution(word_break_ii)
