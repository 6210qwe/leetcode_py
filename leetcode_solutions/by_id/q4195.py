# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 4195
标题: Find Users with High Token Usage
难度: easy
链接: https://leetcode.cn/problems/find-users-with-high-token-usage/
题目类型: 其他
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3793. 查找高 tokens 使用量的用户 - 表：prompts +-------------+---------+ | Column Name | Type | +-------------+---------+ | user_id | int | | prompt | varchar | | tokens | int | +-------------+---------+ (user_id, prompt) 是这张表的主键（值互不相同）。 每一行表示一个用户提交给 AI 系统的提示词以及所消耗的 token 数量。 根据下列要求编写一个解决方案来分析 AI 提示词的使用模式： * 对每一个用户，计算他们提交的 提示词的总数。 * 对每个用户，计算 每个提示词所使用的平均 token 数（舍入到 2 位小数）。 * 仅包含 至少提交了 3 个提示词 的用户。 * 仅包含那些 至少提交过一个提示词 且该提示词的 tokens 数量 超过 自己平均 token 使用量的用户。 返回结果表按 平均 token 数 降序 排序，然后按 user_id 升序 排序。 结果格式如下所示。 示例： 输入： prompts 表： +---------+--------------------------+--------+ | user_id | prompt | tokens | +---------+--------------------------+--------+ | 1 | Write a blog outline | 120 | | 1 | Generate SQL query | 80 | | 1 | Summarize an article | 200 | | 2 | Create resume bullet | 60 | | 2 | Improve LinkedIn bio | 70 | | 3 | Explain neural networks | 300 | | 3 | Generate interview Q&A | 250 | | 3 | Write cover letter | 180 | | 3 | Optimize Python code | 220 | +---------+--------------------------+--------+ 输出： +---------+---------------+------------+ | user_id | prompt_count | avg_tokens | +---------+---------------+------------+ | 3 | 4 | 237.5 | | 1 | 3 | 133.33 | +---------+---------------+------------+ 解释： * 用户 1： * 总提示词数 = 3 * 平均 token 数 = (120 + 80 + 200) / 3 = 133.33 * 有一个提示词为 200 个 token，这超过了平均值 * 包含在结果中 * 用户 2: * 总提示词数 = 2（少于所需的最小值） * 从结果中排除 * 用户 3: * 总提示词数 = 4 * 平均 token 数 = (300 + 250 + 180 + 220) / 4 = 237.5 * 有包含 300 和 250 个 token 的提示词，都大于平均数 * 包含在结果中 结果表按 avg_tokens 降序排序，然后按 user_id 升序排序。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想:
1. 计算每个用户的提示词总数和平均 token 数。
2. 过滤出至少提交了 3 个提示词的用户。
3. 过滤出至少有一个提示词的 token 数超过平均 token 数的用户。
4. 按平均 token 数降序和 user_id 升序排序。

算法步骤:
1. 使用 Pandas 库读取数据。
2. 计算每个用户的提示词总数和平均 token 数。
3. 过滤出符合条件的用户。
4. 按要求排序并返回结果。

关键点:
- 使用 Pandas 库进行数据处理。
- 确保过滤条件正确。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是 prompts 表的行数。主要时间开销在于排序操作。
空间复杂度: O(n)，需要存储中间结果。
"""

# ============================================================================
# 代码实现
# ============================================================================

import pandas as pd


def solution(prompts: pd.DataFrame) -> pd.DataFrame:
    """
    函数式接口 - 实现查找高 tokens 使用量的用户
    """
    # 计算每个用户的提示词总数和平均 token 数
    user_stats = prompts.groupby('user_id').agg(
        prompt_count=('prompt', 'count'),
        total_tokens=('tokens', 'sum')
    ).reset_index()
    user_stats['avg_tokens'] = (user_stats['total_tokens'] / user_stats['prompt_count']).round(2)

    # 过滤出至少提交了 3 个提示词的用户
    user_stats = user_stats[user_stats['prompt_count'] >= 3]

    # 过滤出至少有一个提示词的 token 数超过平均 token 数的用户
    filtered_users = []
    for user_id in user_stats['user_id']:
        user_prompts = prompts[prompts['user_id'] == user_id]
        if any(user_prompts['tokens'] > user_stats.loc[user_stats['user_id'] == user_id, 'avg_tokens'].values[0]):
            filtered_users.append(user_id)
    user_stats = user_stats[user_stats['user_id'].isin(filtered_users)]

    # 按平均 token 数降序和 user_id 升序排序
    result = user_stats.sort_values(by=['avg_tokens', 'user_id'], ascending=[False, True])

    return result[['user_id', 'prompt_count', 'avg_tokens']]


Solution = create_solution(solution)