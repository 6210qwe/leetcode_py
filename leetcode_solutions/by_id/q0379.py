# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 379
标题: Design Phone Directory
难度: medium
链接: https://leetcode.cn/problems/design-phone-directory/
题目类型: 设计、队列、数组、哈希表、链表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
379. 电话目录管理系统 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 队列维护可用号码，布尔数组记录是否已占用。

算法步骤:
1. 初始化时，将 [0, maxNumbers-1] 所有号码入队列 `free`，并用布尔数组 `used` 标记均为未使用。
2. get:
   - 若队列为空，返回 -1；否则从队首取出一个号码，将其标记为已使用并返回。
3. check(number): 在下标范围内时，返回 `not used[number]`。
4. release(number): 若号码在下标范围内且当前为已使用，则将其标记为未使用并重新加入队列末尾。

关键点:
- 通过队列保证 get 总是返回尚未分配的号码，且号码最终会被循环利用。
- `used` 数组避免重复释放和重复分配同一号码。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: get/check/release 均为 O(1)。
空间复杂度: O(N)，N 为 maxNumbers，需要存储队列和布尔数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


class PhoneDirectory:
    """
    电话目录管理系统：支持获取、检查和释放号码。

    使用队列存储可用号码集合，布尔数组标记占用状态。
    """

    def __init__(self, maxNumbers: int):
        from collections import deque

        self.free = deque(range(maxNumbers))
        self.used = [False] * maxNumbers

    def get(self) -> int:
        if not self.free:
            return -1
        num = self.free.popleft()
        self.used[num] = True
        return num

    def check(self, number: int) -> bool:
        return 0 <= number < len(self.used) and not self.used[number]

    def release(self, number: int) -> None:
        if 0 <= number < len(self.used) and self.used[number]:
            self.used[number] = False
            self.free.append(number)


def design_phone_directory(maxNumbers: int) -> PhoneDirectory:
    """
    函数式接口 - 返回 PhoneDirectory 实例，便于在测试中进行方法调用。
    """
    return PhoneDirectory(maxNumbers)


# 自动生成Solution类（无需手动编写）
Solution = create_solution(design_phone_directory)
