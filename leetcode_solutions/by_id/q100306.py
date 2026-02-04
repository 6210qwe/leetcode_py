# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100306
标题: 验证图书取出顺序
难度: medium
链接: https://leetcode.cn/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof/
题目类型: 栈、数组、模拟
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 148. 验证图书取出顺序 - 现在图书馆有一堆图书需要放入书架，并且图书馆的书架是一种特殊的数据结构，只能按照 一定 的顺序 放入 和 拿取 书籍。 给定一个表示图书放入顺序的整数序列 putIn，请判断序列 takeOut 是否为按照正确的顺序拿取书籍的操作序列。你可以假设放入书架的所有书籍编号都不相同。 示例 1： 输入：putIn = [6,7,8,9,10,11], takeOut = [9,11,10,8,7,6] 输出：true 解释：我们可以按以下操作放入并拿取书籍： push(6), push(7), push(8), push(9), pop() -> 9, push(10), push(11),pop() -> 11,pop() -> 10, pop() -> 8, pop() -> 7, pop() -> 6 示例 2： 输入：putIn = [6,7,8,9,10,11], takeOut = [11,9,8,10,6,7] 输出：false 解释：6 不能在 7 之前取出。 提示： * 0 <= putIn.length == takeOut.length <= 1000 * 0 <= putIn[i], takeOut < 1000 * putIn 是 takeOut 的排列。 注意：本题与主站 946 题相同：https://leetcode.cn/problems/validate-stack-sequences/ [https://leetcode.cn/problems/validate-stack-sequences/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用一个辅助栈来模拟图书的放入和取出过程。

算法步骤:
1. 初始化一个空栈 `stack` 和一个指针 `j` 指向 `takeOut` 序列的第一个元素。
2. 遍历 `putIn` 序列：
   - 将当前元素压入栈中。
   - 如果栈顶元素等于 `takeOut[j]`，则弹出栈顶元素并将 `j` 向后移动一位。
   - 重复上述操作直到栈为空或栈顶元素不等于 `takeOut[j]`。
3. 如果遍历完 `putIn` 序列后，栈为空，则说明 `takeOut` 是有效的取出序列。

关键点:
- 使用辅助栈模拟图书的放入和取出过程。
- 通过比较栈顶元素和 `takeOut` 序列中的元素来判断是否可以弹出。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是 `putIn` 序列的长度。每个元素最多只会被压入和弹出栈一次。
空间复杂度: O(n)，辅助栈的空间复杂度为 O(n)。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def validate_book_sequence(put_in: List[int], take_out: List[int]) -> bool:
    """
    函数式接口 - 验证图书取出顺序
    """
    stack = []
    j = 0
    for num in put_in:
        stack.append(num)
        while stack and stack[-1] == take_out[j]:
            stack.pop()
            j += 1
    return not stack


Solution = create_solution(validate_book_sequence)