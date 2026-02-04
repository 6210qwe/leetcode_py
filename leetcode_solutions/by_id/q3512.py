# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3512
标题: Bitwise User Permissions Analysis
难度: medium
链接: https://leetcode.cn/problems/bitwise-user-permissions-analysis/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3204. 按位用户权限分析 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用位运算来解析用户的权限。

算法步骤:
1. 将每个用户的权限位转换为二进制字符串。
2. 通过遍历二进制字符串，确定每个权限位的状态（0 或 1）。
3. 根据权限位的状态，生成相应的权限列表。

关键点:
- 使用位运算和字符串操作来解析权限。
- 通过遍历二进制字符串来确定每个权限位的状态。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * k)，其中 n 是用户数量，k 是权限位的数量。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def solution_function_name(users: List[int], permissions: List[str]) -> List[List[str]]:
    """
    函数式接口 - 解析用户的权限

    :param users: 用户的权限位列表
    :param permissions: 权限名称列表
    :return: 每个用户的权限列表
    """
    result = []
    for user in users:
        binary_str = bin(user)[2:].zfill(len(permissions))
        user_permissions = [permissions[i] for i, bit in enumerate(binary_str) if bit == '1']
        result.append(user_permissions)
    return result

Solution = create_solution(solution_function_name)