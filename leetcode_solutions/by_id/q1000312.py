# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000312
标题: 火星词典
难度: hard
链接: https://leetcode.cn/problems/Jf1JuT/
题目类型: 深度优先搜索、广度优先搜索、图、拓扑排序、数组、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 114. 火星词典 - 现有一种使用英语字母的外星文语言，这门语言的字母顺序与英语顺序不同。 给定一个字符串列表 words ，作为这门语言的词典，words 中的字符串已经 按这门新语言的字母顺序进行了排序 。 请你根据该词典还原出此语言中已知的字母顺序，并 按字母递增顺序 排列。若不存在合法字母顺序，返回 "" 。若存在多种可能的合法字母顺序，返回其中 任意一种 顺序即可。 字符串 s 字典顺序小于 字符串 t 有两种情况： * 在第一个不同字母处，如果 s 中的字母在这门外星语言的字母顺序中位于 t 中字母之前，那么 s 的字典顺序小于 t 。 * 如果前面 min(s.length, t.length) 字母都相同，那么 s.length < t.length 时，s 的字典顺序也小于 t 。 示例 1： 输入：words = ["wrt","wrf","er","ett","rftt"] 输出："wertf" 示例 2： 输入：words = ["z","x"] 输出："zx" 示例 3： 输入：words = ["z","x","z"] 输出："" 解释：不存在合法字母顺序，因此返回 ""。 提示： * 1 <= words.length <= 100 * 1 <= words[i].length <= 100 * words[i] 仅由小写英文字母组成 注意：本题与主站 269 题相同： https://leetcode.cn/problems/alien-dictionary/ [https://leetcode.cn/problems/alien-dictionary/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用拓扑排序来确定字母的顺序。

算法步骤:
1. 构建有向图和入度表。
2. 初始化队列，将入度为0的节点加入队列。
3. 进行拓扑排序，依次处理队列中的节点。
4. 如果最终结果包含所有字母，则返回结果；否则返回空字符串。

关键点:
- 通过比较相邻单词来构建图。
- 使用拓扑排序来确定字母顺序。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(C + V + E)，其中 C 是字符总数，V 是字母数量（最多 26），E 是边的数量。
空间复杂度: O(V + E)，用于存储图和入度表。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from collections import defaultdict, deque


def solution_function_name(words: List[str]) -> str:
    """
    函数式接口 - 根据词典还原出此语言中已知的字母顺序
    """
    # 构建有向图和入度表
    graph = defaultdict(set)
    in_degree = {char: 0 for word in words for char in word}
    
    # 通过比较相邻单词来构建图
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        min_len = min(len(w1), len(w2))
        if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
            return ""
        for j in range(min_len):
            if w1[j] != w2[j]:
                if w2[j] not in graph[w1[j]]:
                    graph[w1[j]].add(w2[j])
                    in_degree[w2[j]] += 1
                break
    
    # 初始化队列，将入度为0的节点加入队列
    queue = deque([char for char in in_degree if in_degree[char] == 0])
    result = []
    
    # 进行拓扑排序
    while queue:
        char = queue.popleft()
        result.append(char)
        for neighbor in graph[char]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # 如果最终结果包含所有字母，则返回结果；否则返回空字符串
    if len(result) == len(in_degree):
        return ''.join(result)
    else:
        return ""

Solution = create_solution(solution_function_name)