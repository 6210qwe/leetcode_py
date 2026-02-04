# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1190
标题: Smallest Common Region
难度: medium
链接: https://leetcode.cn/problems/smallest-common-region/
题目类型: 树、深度优先搜索、广度优先搜索、数组、哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1257. 最小公共区域 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表存储每个区域的父节点，然后通过并查集的思想找到两个区域的最小公共祖先。

算法步骤:
1. 构建一个字典 `parent`，其中键是区域名，值是其父区域名。
2. 对于每个查询，从两个区域开始向上查找，直到找到它们的最小公共祖先。

关键点:
- 使用哈希表记录每个区域的父节点。
- 通过路径压缩优化查找过程。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是 regions 的长度，m 是 queries 的长度。
空间复杂度: O(n)，用于存储父节点关系。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional

def find(parent, region):
    if parent[region] != region:
        parent[region] = find(parent, parent[region])
    return parent[region]

def smallest_common_region(regions: List[List[str]], queries: List[List[str]]) -> List[str]:
    """
    找到每对区域的最小公共区域。
    """
    # 构建父节点字典
    parent = {}
    for region_list in regions:
        for i in range(1, len(region_list)):
            parent[region_list[i]] = region_list[0]
    
    # 处理每个查询
    result = []
    for query in queries:
        region1, region2 = query
        while region1 != region2:
            if region1 in parent and region2 in parent:
                if region1 == parent[region2]:
                    break
                if region2 == parent[region1]:
                    region1, region2 = region2, region1
                else:
                    region1 = parent[region1]
                    region2 = parent[region2]
            else:
                break
        result.append(region1)
    return result

Solution = create_solution(smallest_common_region)