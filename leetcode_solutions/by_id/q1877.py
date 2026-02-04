# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1877
标题: Find Followers Count
难度: easy
链接: https://leetcode.cn/problems/find-followers-count/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1729. 求关注者的数量 - 表： Followers +-------------+------+ | Column Name | Type | +-------------+------+ | user_id | int | | follower_id | int | +-------------+------+ (user_id, follower_id) 是这个表的主键（具有唯一值的列的组合）。 该表包含一个关注关系中关注者和用户的编号，其中关注者关注用户。 编写解决方案，对于每一个用户，返回该用户的关注者数量。 按 user_id 的顺序返回结果表。 查询结果的格式如下示例所示。 示例 1： 输入： Followers 表： +---------+-------------+ | user_id | follower_id | +---------+-------------+ | 0 | 1 | | 1 | 0 | | 2 | 0 | | 2 | 1 | +---------+-------------+ 输出： +---------+----------------+ | user_id | followers_count| +---------+----------------+ | 0 | 1 | | 1 | 1 | | 2 | 2 | +---------+----------------+ 解释： 0 的关注者有 {1} 1 的关注者有 {0} 2 的关注者有 {0,1}
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来统计每个用户的关注者数量。

算法步骤:
1. 使用 GROUP BY 对 user_id 进行分组。
2. 使用 COUNT 函数统计每个 user_id 的 follower_id 数量。
3. 按 user_id 排序结果。

关键点:
- 使用 GROUP BY 和 COUNT 函数来统计每个用户的关注者数量。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是 Followers 表的行数。GROUP BY 和 ORDER BY 操作的时间复杂度为 O(n log n)。
空间复杂度: O(1)，查询操作不需要额外的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(followers: List[List[int]]) -> List[List[int]]:
    """
    函数式接口 - 实现
    """
    from collections import defaultdict
    from operator import itemgetter
    
    # 统计每个用户的关注者数量
    followers_count = defaultdict(int)
    for user_id, follower_id in followers:
        followers_count[user_id] += 1
    
    # 按 user_id 排序并生成结果
    result = [[user_id, count] for user_id, count in sorted(followers_count.items(), key=itemgetter(0))]
    
    return result


Solution = create_solution(solution_function_name)