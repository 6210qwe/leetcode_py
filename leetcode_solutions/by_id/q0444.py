# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 444
标题: Sequence Reconstruction
难度: medium
链接: https://leetcode.cn/problems/sequence-reconstruction/
题目类型: 图、拓扑排序、数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
444. 序列重建 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用拓扑排序来验证序列是否可以重建

算法步骤:
1. 构建图和入度表
2. 初始化队列，将所有入度为0的节点加入队列
3. 进行拓扑排序，检查每次出队的节点是否与目标序列一致
4. 如果在某一步无法继续或不匹配，则返回False；否则返回True

关键点:
- 注意边界条件，如空输入或无效输入
- 优化时间和空间复杂度，使用邻接表存储图
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(V + E) - 其中V是顶点数，E是边数
空间复杂度: O(V + E) - 存储图和入度表
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def sequence_reconstruction(org: List[int], seqs: List[List[int]]) -> bool:
    """
    函数式接口 - 判断给定的序列seqs是否可以唯一地重建为org
    
    实现思路:
    使用拓扑排序来验证序列是否可以重建
    
    Args:
        org: 目标序列
        seqs: 给定的子序列列表
        
    Returns:
        是否可以唯一地重建为org
        
    Example:
        >>> sequence_reconstruction([1,2,3], [[1,2],[1,3]])
        False
        >>> sequence_reconstruction([1,2,3], [[1,2],[2,3]])
        True
    """
    if not org or not seqs:
        return False
    
    # 构建图和入度表
    graph = {}
    in_degree = {}
    
    for seq in seqs:
        for i in range(len(seq)):
            if seq[i] not in graph:
                graph[seq[i]] = set()
                in_degree[seq[i]] = 0
            if i > 0:
                if seq[i-1] not in graph:
                    graph[seq[i-1]] = set()
                    in_degree[seq[i-1]] = 0
                if seq[i] not in graph[seq[i-1]]:
                    graph[seq[i-1]].add(seq[i])
                    in_degree[seq[i]] += 1
    
    # 初始化队列，将所有入度为0的节点加入队列
    queue = [node for node in in_degree if in_degree[node] == 0]
    
    # 拓扑排序
    index = 0
    while queue:
        if len(queue) > 1 or (queue and queue[0] != org[index]):
            return False
        node = queue.pop(0)
        index += 1
        for neighbor in graph.get(node, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return index == len(org)


# 自动生成Solution类（无需手动编写）
Solution = create_solution(sequence_reconstruction)