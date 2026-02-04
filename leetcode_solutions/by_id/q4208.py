# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 4208
标题: Find Emotionally Consistent Users
难度: medium
链接: https://leetcode.cn/problems/find-emotionally-consistent-users/
题目类型: 其他
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3808. 寻找情绪一致的用户 - 表：reactions +--------------+---------+ | Column Name | Type | +--------------+---------+ | user_id | int | | content_id | int | | reaction | varchar | +--------------+---------+ (user_id, content_id) 是这张表的主键（值互不相同）。 每一行代表用户对某条内容的反应。 根据以下要求编写一个解决方案，以识别 情绪一致的用户： * 为每个用户统计他们发送的总反应次数。 * 仅包含 至少对 5 个不同内容项 作出反应的用户。 * 如果用户 至少 60% 的反应属于 同一种类型，则认为其 情绪一致。 返回结果表按 reaction_ratio 降序 排序，然后按 user_id 升序 排序。 注意： * reaction_ratio 应该舍入到 2 位小数 结果格式如下所示。 示例： 输入： reactions 表： +---------+------------+----------+ | user_id | content_id | reaction | +---------+------------+----------+ | 1 | 101 | like | | 1 | 102 | like | | 1 | 103 | like | | 1 | 104 | wow | | 1 | 105 | like | | 2 | 201 | like | | 2 | 202 | wow | | 2 | 203 | sad | | 2 | 204 | like | | 2 | 205 | wow | | 3 | 301 | love | | 3 | 302 | love | | 3 | 303 | love | | 3 | 304 | love | | 3 | 305 | love | +---------+------------+----------+ 输出： +---------+-------------------+----------------+ | user_id | dominant_reaction | reaction_ratio | +---------+-------------------+----------------+ | 3 | love | 1.00 | | 1 | like | 0.80 | +---------+-------------------+----------------+ 解释： * 用户 1： * 总反应数 = 5 * 'like' 出现了 4 次 * reaction_ratio = 4 / 5 = 0.80 * 满足 60% 一致的要求 * 用户 2： * 总反应数 = 5 * 出现最多的反应只出现了 2 次 * reaction_ratio = 2 / 5 = 0.40 * 不满足一致的要求 * 用户 3： * 总反应数 = 5 * 'love' 出现了 5 次 * reaction_ratio = 5 / 5 = 1.00 * 满足一致的要求 结果表按 reaction_ratio 降序排序，然后按 user_id 升序排序。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想:
1. 统计每个用户的反应次数和每种反应的出现次数。
2. 筛选出至少对 5 个不同内容项作出反应的用户。
3. 计算每个用户的主导反应及其比例。
4. 过滤出主导反应比例大于等于 60% 的用户。
5. 按照 reaction_ratio 降序排序，然后按 user_id 升序排序。

算法步骤:
1. 使用 Pandas 读取数据。
2. 分组统计每个用户的反应次数和每种反应的出现次数。
3. 筛选出至少对 5 个不同内容项作出反应的用户。
4. 计算每个用户的主导反应及其比例。
5. 过滤出主导反应比例大于等于 60% 的用户。
6. 按照 reaction_ratio 降序排序，然后按 user_id 升序排序。

关键点:
- 使用 Pandas 进行高效的分组和聚合操作。
- 通过分组和聚合计算每个用户的主导反应及其比例。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是 reactions 表的行数。主要的时间开销在于排序操作。
空间复杂度: O(n)，需要存储分组后的数据。
"""

# ============================================================================
# 代码实现
# ============================================================================

import pandas as pd
from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def find_emotionally_consistent_users(reactions: pd.DataFrame) -> pd.DataFrame:
    """
    函数式接口 - 寻找情绪一致的用户
    """
    # 分组统计每个用户的反应次数和每种反应的出现次数
    user_reactions = reactions.groupby(['user_id', 'reaction']).size().reset_index(name='count')
    
    # 统计每个用户的总反应次数
    total_reactions = user_reactions.groupby('user_id')['count'].sum().reset_index(name='total_count')
    
    # 找出每个用户的主导反应
    dominant_reactions = user_reactions.loc[user_reactions.groupby('user_id')['count'].idxmax()]
    
    # 合并主导反应和总反应次数
    result = pd.merge(dominant_reactions, total_reactions, on='user_id')
    
    # 计算反应比例
    result['reaction_ratio'] = (result['count'] / result['total_count']).round(2)
    
    # 筛选出至少对 5 个不同内容项作出反应的用户
    valid_users = reactions.groupby('user_id')['content_id'].nunique().reset_index(name='unique_content_count')
    valid_users = valid_users[valid_users['unique_content_count'] >= 5]
    
    # 过滤出主导反应比例大于等于 60% 的用户
    result = pd.merge(result, valid_users, on='user_id')
    result = result[result['reaction_ratio'] >= 0.6]
    
    # 按照 reaction_ratio 降序排序，然后按 user_id 升序排序
    result = result.sort_values(by=['reaction_ratio', 'user_id'], ascending=[False, True])
    
    # 选择最终的列
    result = result[['user_id', 'reaction', 'reaction_ratio']]
    result.columns = ['user_id', 'dominant_reaction', 'reaction_ratio']
    
    return result


Solution = create_solution(find_emotionally_consistent_users)