# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2098
标题: All the Pairs With the Maximum Number of Common Followers
难度: medium
链接: https://leetcode.cn/problems/all-the-pairs-with-the-maximum-number-of-common-followers/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1951. 查询具有最多共同关注者的所有两两结对组 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用集合来存储每个用户的关注者列表，并通过集合的交集操作来计算两个用户之间的共同关注者数量。然后遍历所有可能的用户对，找到具有最多共同关注者的用户对。

算法步骤:
1. 创建一个字典，键为用户ID，值为该用户的关注者集合。
2. 遍历所有可能的用户对，计算它们的共同关注者数量。
3. 记录具有最多共同关注者的用户对。

关键点:
- 使用集合来存储关注者列表，以便快速计算交集。
- 通过遍历所有可能的用户对来找到具有最多共同关注者的用户对。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2 * m)，其中 n 是用户的数量，m 是每个用户的平均关注者数量。因为我们需要遍历所有用户对，并且每次计算交集的时间复杂度是 O(m)。
空间复杂度: O(n * m)，用于存储每个用户的关注者集合。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def find_pairs_with_max_common_followers(followers: List[List[int]]) -> List[List[int]]:
    """
    函数式接口 - 找到具有最多共同关注者的所有两两结对组
    """
    # 创建一个字典，键为用户ID，值为该用户的关注者集合
    user_followers = {i: set(followers[i]) for i in range(len(followers))}
    
    max_common_followers = 0
    result = []
    
    # 遍历所有可能的用户对
    for i in range(len(followers)):
        for j in range(i + 1, len(followers)):
            common_followers = user_followers[i] & user_followers[j]
            num_common_followers = len(common_followers)
            
            if num_common_followers > max_common_followers:
                max_common_followers = num_common_followers
                result = [[i, j]]
            elif num_common_followers == max_common_followers:
                result.append([i, j])
    
    return result

Solution = create_solution(find_pairs_with_max_common_followers)