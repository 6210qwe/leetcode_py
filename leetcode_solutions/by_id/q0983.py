# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 983
标题: Validate Stack Sequences
难度: medium
链接: https://leetcode.cn/problems/validate-stack-sequences/
题目类型: 栈、数组、模拟
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
946. 验证栈序列 - 给定 pushed 和 popped 两个序列，每个序列中的 值都不重复，只有当它们可能是在最初空栈上进行的推入 push 和弹出 pop 操作序列的结果时，返回 true；否则，返回 false 。 示例 1： 输入：pushed = [1,2,3,4,5], popped = [4,5,3,2,1] 输出：true 解释：我们可以按以下顺序执行： push(1), push(2), push(3), push(4), pop() -> 4, push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1 示例 2： 输入：pushed = [1,2,3,4,5], popped = [4,3,5,1,2] 输出：false 解释：1 不能在 2 之前弹出。 提示： * 1 <= pushed.length <= 1000 * 0 <= pushed[i] <= 1000 * pushed 的所有元素 互不相同 * popped.length == pushed.length * popped 是 pushed 的一个排列
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用一个辅助栈来模拟 push 和 pop 操作。

算法步骤:
1. 初始化一个空栈 `stack` 和一个指针 `i` 指向 `popped` 序列的第一个元素。
2. 遍历 `pushed` 序列：
   - 将当前元素压入 `stack`。
   - 检查 `stack` 的顶部元素是否与 `popped` 序列的当前元素相同，如果相同则弹出 `stack` 的顶部元素，并将 `i` 向后移动一位。
3. 如果遍历结束后 `stack` 为空，则返回 `True`，否则返回 `False`。

关键点:
- 使用一个辅助栈来模拟操作。
- 通过比较 `stack` 的顶部元素和 `popped` 序列的当前元素来决定是否弹出。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是 `pushed` 或 `popped` 的长度。每个元素最多只会被压入和弹出一次。
空间复杂度: O(n)，辅助栈的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def validate_stack_sequences(pushed: List[int], popped: List[int]) -> bool:
    """
    函数式接口 - 验证栈序列
    """
    stack = []
    i = 0
    for num in pushed:
        stack.append(num)
        while stack and stack[-1] == popped[i]:
            stack.pop()
            i += 1
    return not stack


Solution = create_solution(validate_stack_sequences)