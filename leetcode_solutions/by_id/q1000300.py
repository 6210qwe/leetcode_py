# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000300
标题: 单词接龙
难度: hard
链接: https://leetcode.cn/problems/om3reC/
题目类型: 广度优先搜索、哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 108. 单词接龙 - 在字典（单词列表） wordList 中，从单词 beginWord 和 endWord 的 转换序列 是一个按下述规格形成的序列： * 序列中第一个单词是 beginWord 。 * 序列中最后一个单词是 endWord 。 * 每次转换只能改变一个字母。 * 转换过程中的中间单词必须是字典 wordList 中的单词。 给定两个长度相同但内容不同的单词 beginWord 和 endWord 和一个字典 wordList ，找到从 beginWord 到 endWord 的 最短转换序列 中的 单词数目 。如果不存在这样的转换序列，返回 0。 示例 1： 输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"] 输出：5 解释：一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog", 返回它的长度 5。 示例 2： 输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"] 输出：0 解释：endWord "cog" 不在字典中，所以无法进行转换。 提示： * 1 <= beginWord.length <= 10 * endWord.length == beginWord.length * 1 <= wordList.length <= 5000 * wordList[i].length == beginWord.length * beginWord、endWord 和 wordList[i] 由小写英文字母组成 * beginWord != endWord * wordList 中的所有字符串 互不相同 注意：本题与主站 127 题相同： https://leetcode.cn/problems/word-ladder/ [https://leetcode.cn/problems/word-ladder/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用双向广度优先搜索（BFS）来找到从 beginWord 到 endWord 的最短路径。

算法步骤:
1. 初始化两个队列，分别从 beginWord 和 endWord 开始进行 BFS。
2. 使用两个集合分别记录从 beginWord 和 endWord 出发已经访问过的单词。
3. 在每一步中，选择当前较小的队列进行扩展，生成所有可能的下一个单词，并检查这些单词是否在另一个方向的已访问集合中。
4. 如果找到交集，则说明找到了最短路径，返回路径长度。
5. 如果两个队列都为空且没有找到交集，则返回 0。

关键点:
- 双向 BFS 可以显著减少搜索空间，提高效率。
- 使用通配符来生成所有可能的下一个单词。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(N * M^2)，其中 N 是 wordList 的长度，M 是单词的长度。每个单词最多生成 M 个新单词，每个新单词需要 O(M) 时间来生成和检查。
空间复杂度: O(N * M)，用于存储队列和已访问的单词集合。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def ladder_length(begin_word: str, end_word: str, word_list: List[str]) -> int:
    if end_word not in word_list:
        return 0

    word_set = set(word_list)
    front_queue, back_queue = {begin_word}, {end_word}
    visited_front, visited_back = {begin_word}, {end_word}
    steps = 1

    while front_queue and back_queue:
        if len(front_queue) > len(back_queue):
            front_queue, back_queue = back_queue, front_queue
            visited_front, visited_back = visited_back, visited_front

        next_level = set()
        for word in front_queue:
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in back_queue:
                        return steps + 1
                    if new_word in word_set and new_word not in visited_front:
                        next_level.add(new_word)
                        visited_front.add(new_word)

        front_queue = next_level
        steps += 1

    return 0


Solution = create_solution(ladder_length)