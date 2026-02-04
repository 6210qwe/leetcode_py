# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1108
标题: Analyze User Website Visit Pattern
难度: medium
链接: https://leetcode.cn/problems/analyze-user-website-visit-pattern/
题目类型: 数组、哈希表、字符串、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1152. 用户网站访问行为分析 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用三重循环生成所有可能的三元组，并使用哈希表记录每个用户的访问顺序。最后统计出现次数最多的三元组。

算法步骤:
1. 使用一个字典 `user_visits` 记录每个用户的访问序列。
2. 对每个用户的访问序列进行排序。
3. 使用三重循环生成所有可能的三元组，并使用哈希表 `triplets_count` 记录每个三元组的出现次数。
4. 找到出现次数最多的三元组。

关键点:
- 对每个用户的访问序列进行排序以确保三元组的一致性。
- 使用哈希表记录三元组的出现次数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m^3)，其中 n 是用户的数量，m 是每个用户访问的网站数量。
空间复杂度: O(n * m^3)，用于存储所有可能的三元组及其计数。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from collections import defaultdict

def solution_function_name(username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
    """
    函数式接口 - 实现最优解法
    """
    # 创建一个字典来存储每个用户的访问记录
    user_visits = defaultdict(list)
    
    # 将访问记录按用户分组
    for i in range(len(username)):
        user_visits[username[i]].append((timestamp[i], website[i]))
    
    # 对每个用户的访问记录按时间戳排序
    for user in user_visits:
        user_visits[user].sort()
    
    # 生成所有可能的三元组并记录其出现次数
    triplets_count = defaultdict(int)
    for user, visits in user_visits.items():
        for i in range(len(visits) - 2):
            for j in range(i + 1, len(visits) - 1):
                for k in range(j + 1, len(visits)):
                    triplet = (visits[i][1], visits[j][1], visits[k][1])
                    triplets_count[triplet] += 1
    
    # 找到出现次数最多的三元组
    max_count = 0
    result_triplet = None
    for triplet, count in triplets_count.items():
        if count > max_count or (count == max_count and triplet < result_triplet):
            max_count = count
            result_triplet = triplet
    
    return list(result_triplet)

Solution = create_solution(solution_function_name)