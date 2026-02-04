# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1381
标题: Maximum Score Words Formed by Letters
难度: hard
链接: https://leetcode.cn/problems/maximum-score-words-formed-by-letters/
题目类型: 位运算、数组、哈希表、字符串、动态规划、回溯、状态压缩、计数
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1255. 得分最高的单词集合 - 你将会得到一份单词表 words，一个字母表 letters （可能会有重复字母），以及每个字母对应的得分情况表 score。 请你帮忙计算玩家在单词拼写游戏中所能获得的「最高得分」：能够由 letters 里的字母拼写出的 任意 属于 words 单词子集中，分数最高的单词集合的得分。 单词拼写游戏的规则概述如下： * 玩家需要用字母表 letters 里的字母来拼写单词表 words 中的单词。 * 可以只使用字母表 letters 中的部分字母，但是每个字母最多被使用一次。 * 单词表 words 中每个单词只能计分（使用）一次。 * 根据字母得分情况表score，字母 'a', 'b', 'c', ... , 'z' 对应的得分分别为 score[0], score[1], ..., score[25]。 * 本场游戏的「得分」是指：玩家所拼写出的单词集合里包含的所有字母的得分之和。 示例 1： 输入：words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0] 输出：23 解释： 字母得分为 a=1, c=9, d=5, g=3, o=2 使用给定的字母表 letters，我们可以拼写单词 "dad" (5+1+5)和 "good" (3+2+2+5)，得分为 23 。 而单词 "dad" 和 "dog" 只能得到 21 分。 示例 2： 输入：words = ["xxxz","ax","bx","cx"], letters = ["z","a","b","c","x","x","x"], score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10] 输出：27 解释： 字母得分为 a=4, b=4, c=4, x=5, z=10 使用给定的字母表 letters，我们可以组成单词 "ax" (4+5)， "bx" (4+5) 和 "cx" (4+5) ，总得分为 27 。 单词 "xxxz" 的得分仅为 25 。 示例 3： 输入：words = ["leetcode"], letters = ["l","e","t","c","o","d"], score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0] 输出：0 解释： 字母 "e" 在字母表 letters 中只出现了一次，所以无法组成单词表 words 中的单词。 提示： * 1 <= words.length <= 14 * 1 <= words[i].length <= 15 * 1 <= letters.length <= 100 * letters[i].length == 1 * score.length == 26 * 0 <= score[i] <= 10 * words[i] 和 letters[i] 只包含小写的英文字母。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用回溯法来尝试所有可能的单词组合，并计算每个组合的得分。通过剪枝来减少不必要的计算。

算法步骤:
1. 初始化字母计数器，记录字母表中每个字母的数量。
2. 定义一个递归函数，用于尝试每个单词是否可以加入当前组合。
3. 在递归函数中，更新字母计数器，并计算当前组合的得分。
4. 如果当前组合的得分大于已知的最大得分，则更新最大得分。
5. 递归调用，尝试下一个单词。
6. 回溯时，恢复字母计数器的状态。

关键点:
- 使用回溯法来尝试所有可能的单词组合。
- 通过剪枝来减少不必要的计算，提高效率。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(2^n)，其中 n 是 words 的长度。最坏情况下，我们需要尝试所有可能的单词组合。
空间复杂度: O(n)，递归调用栈的深度最多为 n。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from collections import Counter

def max_score_words(words: List[str], letters: List[str], score: List[int]) -> int:
    def backtrack(index, current_letters, current_score):
        nonlocal max_score
        if index == len(words):
            max_score = max(max_score, current_score)
            return
        
        # 不选择当前单词
        backtrack(index + 1, current_letters, current_score)
        
        # 选择当前单词
        word = words[index]
        word_count = Counter(word)
        if all(current_letters[char] >= word_count[char] for char in word_count):
            for char in word_count:
                current_letters[char] -= word_count[char]
            word_score = sum(score[ord(char) - ord('a')] * word_count[char] for char in word_count)
            backtrack(index + 1, current_letters, current_score + word_score)
            for char in word_count:
                current_letters[char] += word_count[char]

    letter_count = Counter(letters)
    max_score = 0
    backtrack(0, letter_count, 0)
    return max_score

Solution = create_solution(max_score_words)