# -*- coding:utf-8 -*-
"""
LeetCode题解包
支持按题号、难度、题型、周赛等多维度导入最优Python解法
"""

__version__ = '0.1.0'

# 导出元数据查询函数
from leetcode_solutions.metadata import (
    PROBLEM_METADATA,
    get_problems_by_difficulty,
    get_problems_by_topic,
    get_problems_by_contest,
    get_problem_info,
    get_premium_problems,
    get_interview_problems,
    get_all_topics,
    get_all_contests,
)

# 导出工具类
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode

# 导出分类模块（方便用户导入）
# 注意：这些模块需要用户通过完整路径导入，如 from leetcode_solutions.by_id import q0001
# 这里不直接导入，避免循环导入问题

__all__ = [
    # 版本信息
    '__version__',
    # 元数据查询
    'PROBLEM_METADATA',
    'get_problems_by_difficulty',
    'get_problems_by_topic',
    'get_problems_by_contest',
    'get_problem_info',
    'get_premium_problems',
    'get_interview_problems',
    'get_all_topics',
    'get_all_contests',
    # 工具类
    'ListNode',
    'TreeNode',
    # 分类模块
    'by_id',
    'by_difficulty',
    'by_topic',
    'by_contest',
]

