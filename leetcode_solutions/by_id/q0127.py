# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 127
标题: Word Ladder
难度: hard
链接: https://leetcode.cn/problems/word-ladder/
题目类型: 广度优先搜索、哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
127. 单词接龙 - 字典 wordList 中从单词 beginWord 到 endWord 的 转换序列 是一个按下述规格形成的序列 beginWord -> s1 -> s2 -> ... -> sk： * 每一对相邻的单词只差一个字母。 * 对于 1 <= i <= k 时，每个 si 都在 wordList 中。注意， beginWord 不需要在 wordList 中。 * sk == endWord 给你两个单词 beginWord 和 endWord 和一个字典 wordList ，返回 从 beginWord 到 endWord 的 最短转换序列 中的 单词数目 。如果不存在这样的转换序列，返回 0 。 示例 1： 输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"] 输出：5 解释：一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog", 返回它的长度 5。 示例 2： 输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"] 输出：0 解释：endWord "cog" 不在字典中，所以无法进行转换。 提示： * 1 <= beginWord.length <= 10 * endWord.length == beginWord.length * 1 <= wordList.length <= 5000 * wordList[i].length == beginWord.length * beginWord、endWord 和 wordList[i] 由小写英文字母组成 * beginWord != endWord * wordList 中的所有字符串 互不相同
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用BFS找到最短路径，每次改变一个字母

算法步骤:
1. 将wordList转换为集合提高查找效率
2. 使用BFS，从beginWord开始
3. 对于每个单词，尝试改变每个位置的字母
4. 如果新单词在字典中且未访问过，加入队列
5. 找到endWord时返回步数

关键点:
- 使用BFS保证最短路径
- 时间复杂度O(M*N)，M为单词长度，N为字典大小
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(M*N) - M为单词长度，N为字典大小
空间复杂度: O(N) - 队列和集合空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from collections import deque
from leetcode_solutions.utils.solution import create_solution


def word_ladder(beginWord: str, endWord: str, wordList: List[str]) -> int:
    """
    函数式接口 - 单词接龙最短路径
    
    实现思路:
    使用BFS找到从beginWord到endWord的最短转换序列。
    
    Args:
        beginWord: 起始单词
        endWord: 结束单词
        wordList: 单词字典
        
    Returns:
        最短转换序列的单词数目，如果不存在返回0
        
    Example:
        >>> word_ladder("hit", "cog", ["hot","dot","dog","lot","log","cog"])
        5
    """
    word_set = set(wordList)
    if endWord not in word_set:
        return 0
    
    queue = deque([(beginWord, 1)])
    visited = {beginWord}
    
    while queue:
        word, steps = queue.popleft()
        
        if word == endWord:
            return steps
        
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + c + word[i+1:]
                
                if new_word in word_set and new_word not in visited:
                    visited.add(new_word)
                    queue.append((new_word, steps + 1))
    
    return 0


# 自动生成Solution类（无需手动编写）
Solution = create_solution(word_ladder)
