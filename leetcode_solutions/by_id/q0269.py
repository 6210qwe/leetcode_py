# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 269
标题: Alien Dictionary
难度: hard
链接: https://leetcode.cn/problems/alien-dictionary/
题目类型: 深度优先搜索、广度优先搜索、图、拓扑排序、数组、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
269. 火星词典 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 拓扑排序，根据单词顺序构建有向图

算法步骤:
1. 比较相邻单词，找到第一个不同的字符，建立边
2. 构建有向图和入度数组
3. 使用拓扑排序得到字母顺序

关键点:
- 拓扑排序
- 检测环
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n*k) - n为单词数，k为平均长度
空间复杂度: O(1) - 最多26个字母
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from collections import defaultdict, deque
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def alien_order(words: List[str]) -> str:
    """
    函数式接口 - 火星词典
    
    实现思路:
    拓扑排序：根据单词顺序构建有向图。
    
    Args:
        words: 单词数组
        
    Returns:
        字母顺序，如果无效返回空字符串
        
    Example:
        >>> alien_order(["wrt","wrf","er","ett","rftt"])
        'wertf'
    """
    # 构建图和入度
    graph = defaultdict(set)
    in_degree = defaultdict(int)
    
    # 初始化所有字符
    for word in words:
        for char in word:
            in_degree[char] = 0
    
    # 比较相邻单词，建立边
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        
        # 检查前缀情况
        if len(w1) > len(w2) and w1.startswith(w2):
            return ""
        
        for j in range(min(len(w1), len(w2))):
            if w1[j] != w2[j]:
                if w2[j] not in graph[w1[j]]:
                    graph[w1[j]].add(w2[j])
                    in_degree[w2[j]] += 1
                break
    
    # 拓扑排序
    queue = deque([char for char in in_degree if in_degree[char] == 0])
    result = []
    
    while queue:
        char = queue.popleft()
        result.append(char)
        
        for neighbor in graph[char]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # 检查是否有环
    if len(result) != len(in_degree):
        return ""
    
    return ''.join(result)


# 自动生成Solution类（无需手动编写）
Solution = create_solution(alien_order)
