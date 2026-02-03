# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1775
标题: Design an Ordered Stream
难度: easy
链接: https://leetcode.cn/problems/design-an-ordered-stream/
题目类型: 设计、数组、哈希表、数据流
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1656. 设计有序流 - 有 n 个 (id, value) 对，其中 id 是 1 到 n 之间的一个整数，value 是一个字符串。不存在 id 相同的两个 (id, value) 对。 设计一个流，以 任意 顺序获取 n 个 (id, value) 对，并在多次调用时 按 id 递增的顺序 返回一些值。 实现 OrderedStream 类： * OrderedStream(int n) 构造一个能接收 n 个值的流，并将当前指针 ptr 设为 1 。 * String[] insert(int id, String value) 向流中存储新的 (id, value) 对。存储后： * 如果流存储有 id = ptr 的 (id, value) 对，则找出从 id = ptr 开始的 最长 id 连续递增序列 ，并 按顺序 返回与这些 id 关联的值的列表。然后，将 ptr 更新为最后那个 id + 1 。 * 否则，返回一个空列表。 示例： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/11/15/q1.gif] 输入 ["OrderedStream", "insert", "insert", "insert", "insert", "insert"] [[5], [3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"], [4, "ddddd"]] 输出 [null, [], ["aaaaa"], ["bbbbb", "ccccc"], [], ["ddddd", "eeeee"]] 解释 OrderedStream os= new OrderedStream(5); os.insert(3, "ccccc"); // 插入 (3, "ccccc")，返回 [] os.insert(1, "aaaaa"); // 插入 (1, "aaaaa")，返回 ["aaaaa"] os.insert(2, "bbbbb"); // 插入 (2, "bbbbb")，返回 ["bbbbb", "ccccc"] os.insert(5, "eeeee"); // 插入 (5, "eeeee")，返回 [] os.insert(4, "ddddd"); // 插入 (4, "ddddd")，返回 ["ddddd", "eeeee"] 提示： * 1 <= n <= 1000 * 1 <= id <= n * value.length == 5 * value 仅由小写字母组成 * 每次调用 insert 都会使用一个唯一的 id * 恰好调用 n 次 insert
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: [TODO]

算法步骤:
1. [TODO]
2. [TODO]

关键点:
- [TODO]
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O([TODO])
空间复杂度: O([TODO])
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(params):
    """
    函数式接口 - [TODO] 实现
    """
    # TODO: 实现最优解法
    pass


Solution = create_solution(solution_function_name)
