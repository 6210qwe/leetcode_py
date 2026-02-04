# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000030
标题: Word Transformer LCCI
难度: medium
链接: https://leetcode.cn/problems/word-transformer-lcci/
题目类型: 广度优先搜索、哈希表、字符串、回溯
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
面试题 17.22. 单词转换 - 给定字典中的两个词，长度相等。写一个方法，把一个词转换成另一个词， 但是一次只能改变一个字符。每一步得到的新词都必须能在字典中找到。 编写一个程序，返回一个可能的转换序列。如有多个可能的转换序列，你可以返回任何一个。 示例 1： 输入： beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"] 输出： ["hit","hot","dot","lot","log","cog"] 示例 2： 输入： beginWord = "hit" endWord = "cog" wordList = ["hot","dot","dog","lot","log"] 输出：[] 解释：endWord "cog" 不在字典中，所以不存在符合要求的转换序列。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用广度优先搜索（BFS）来找到从 beginWord 到 endWord 的最短路径。为了优化搜索过程，我们使用一个预处理步骤来构建每个单词的通用模式（例如，将 "hot" 转换为 "*ot"、"h*t" 和 "ho*"），并将这些模式映射到具有相同模式的单词列表。

算法步骤:
1. 将 wordList 转换为集合以实现 O(1) 查找。
2. 如果 endWord 不在 wordList 中，直接返回空列表。
3. 构建一个模式到单词的映射，以便快速查找可以转换的单词。
4. 使用 BFS 进行搜索，记录每个单词的前驱节点以便重建路径。
5. 如果找到 endWord，则通过前驱节点重建路径并返回。

关键点:
- 使用通用模式来优化查找可以转换的单词。
- 使用 BFS 来找到最短路径。
- 记录前驱节点以便重建路径。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(N * M^2)，其中 N 是 wordList 的长度，M 是单词的长度。构建模式映射需要 O(N * M^2) 时间，BFS 搜索的时间复杂度也是 O(N * M^2)。
空间复杂度: O(N * M^2)，用于存储模式映射和 BFS 队列。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from collections import defaultdict, deque


def find_ladders(begin_word: str, end_word: str, word_list: List[str]) -> List[str]:
    if end_word not in word_list:
        return []

    word_set = set(word_list)
    pattern_map = defaultdict(list)

    # 构建模式映射
    for word in word_list:
        for i in range(len(word)):
            pattern = word[:i] + "*" + word[i+1:]
            pattern_map[pattern].append(word)

    # BFS 初始化
    queue = deque([(begin_word, [begin_word])])
    visited = set([begin_word])

    while queue:
        current_word, path = queue.popleft()
        if current_word == end_word:
            return path

        for i in range(len(current_word)):
            pattern = current_word[:i] + "*" + current_word[i+1:]
            for next_word in pattern_map[pattern]:
                if next_word not in visited:
                    visited.add(next_word)
                    queue.append((next_word, path + [next_word]))

    return []


Solution = create_solution(find_ladders)