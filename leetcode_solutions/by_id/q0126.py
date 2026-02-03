# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 126
标题: Word Ladder II
难度: hard
链接: https://leetcode.cn/problems/word-ladder-ii/
题目类型: 广度优先搜索、哈希表、字符串、回溯
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
126. 单词接龙 II - 按字典 wordList 完成从单词 beginWord 到单词 endWord 转化，一个表示此过程的 转换序列 是形式上像 beginWord -> s1 -> s2 -> ... -> sk 这样的单词序列，并满足： * 每对相邻的单词之间仅有单个字母不同。 * 转换过程中的每个单词 si（1 <= i <= k）必须是字典 wordList 中的单词。注意，beginWord 不必是字典 wordList 中的单词。 * sk == endWord 给你两个单词 beginWord 和 endWord ，以及一个字典 wordList 。请你找出并返回所有从 beginWord 到 endWord 的 最短转换序列 ，如果不存在这样的转换序列，返回一个空列表。每个序列都应该以单词列表 [beginWord, s1, s2, ..., sk] 的形式返回。 示例 1： 输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"] 输出：[["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]] 解释：存在 2 种最短的转换序列： "hit" -> "hot" -> "dot" -> "dog" -> "cog" "hit" -> "hot" -> "lot" -> "log" -> "cog" 示例 2： 输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"] 输出：[] 解释：endWord "cog" 不在字典 wordList 中，所以不存在符合要求的转换序列。 提示： * 1 <= beginWord.length <= 5 * endWord.length == beginWord.length * 1 <= wordList.length <= 500 * wordList[i].length == beginWord.length * beginWord、endWord 和 wordList[i] 由小写英文字母组成 * beginWord != endWord * wordList 中的所有单词 互不相同
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: BFS构建图，然后DFS回溯找所有最短路径

算法步骤:
1. 使用BFS找到从beginWord到endWord的最短距离，并构建图
2. 使用DFS回溯，从endWord开始，找到所有最短路径
3. 使用字典存储每个单词的下一层单词列表

关键点:
- BFS构建图+DFS回溯
- 时间复杂度O(n*L*26)，空间复杂度O(n*L)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n*L*26) - n为单词数量，L为单词长度
空间复杂度: O(n*L) - 图的空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from collections import defaultdict, deque
from leetcode_solutions.utils.solution import create_solution


def word_ladder_ii(beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    """
    函数式接口 - 单词接龙II
    
    实现思路:
    BFS构建图，然后DFS回溯找所有最短路径。
    
    Args:
        beginWord: 起始单词
        endWord: 结束单词
        wordList: 单词字典
        
    Returns:
        所有从beginWord到endWord的最短转换序列
        
    Example:
        >>> word_ladder_ii("hit", "cog", ["hot","dot","dog","lot","log","cog"])
        [['hit', 'hot', 'dot', 'dog', 'cog'], ['hit', 'hot', 'lot', 'log', 'cog']]
    """
    if endWord not in wordList:
        return []
    
    wordSet = set(wordList)
    wordSet.add(beginWord)
    
    # BFS构建图
    graph = defaultdict(list)
    distance = {beginWord: 0}
    queue = deque([beginWord])
    
    while queue:
        current = queue.popleft()
        if current == endWord:
            break
        
        for i in range(len(current)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = current[:i] + c + current[i+1:]
                if next_word in wordSet:
                    if next_word not in distance:
                        distance[next_word] = distance[current] + 1
                        queue.append(next_word)
                    if distance[next_word] == distance[current] + 1:
                        graph[next_word].append(current)
    
    # DFS回溯找所有最短路径
    result = []
    
    def dfs(word: str, path: List[str]):
        if word == beginWord:
            result.append(path[::-1])
            return
        
        for prev_word in graph[word]:
            dfs(prev_word, path + [prev_word])
    
    if endWord in distance:
        dfs(endWord, [endWord])
    
    return result


# 自动生成Solution类（无需手动编写）
Solution = create_solution(word_ladder_ii)
