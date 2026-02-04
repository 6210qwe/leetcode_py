# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1898
标题: Leetflex Banned Accounts
难度: medium
链接: https://leetcode.cn/problems/leetflex-banned-accounts/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1747. 应该被禁止的 Leetflex 账户 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来找出所有被禁止的账户。

算法步骤:
1. 找出所有被禁止的 IP 地址。
2. 找出所有被禁止的设备 ID。
3. 找出所有在被禁止的 IP 地址或设备 ID 上登录过的账户。
4. 返回这些账户的唯一标识。

关键点:
- 使用子查询和 JOIN 来过滤出被禁止的账户。
- 确保查询结果去重。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是登录记录的数量，m 是被禁止的 IP 和设备 ID 的数量。
空间复杂度: O(1)，除了存储查询结果外，不需要额外的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(logs: List[List[str]], banned_ips: List[str], banned_devices: List[str]) -> List[str]:
    """
    函数式接口 - 找出所有被禁止的 Leetflex 账户
    """
    # 创建一个集合来存储被禁止的 IP 和设备 ID
    banned_ips_set = set(banned_ips)
    banned_devices_set = set(banned_devices)

    # 创建一个集合来存储被禁止的账户
    banned_accounts = set()

    # 遍历所有的登录记录
    for log in logs:
        account_id, ip, device_id = log
        if ip in banned_ips_set or device_id in banned_devices_set:
            banned_accounts.add(account_id)

    # 返回被禁止的账户列表
    return list(banned_accounts)


Solution = create_solution(solution_function_name)