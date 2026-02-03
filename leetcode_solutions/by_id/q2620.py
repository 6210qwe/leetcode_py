# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2620
标题: Find Consecutive Integers from a Data Stream
难度: medium
链接: https://leetcode.cn/problems/find-consecutive-integers-from-a-data-stream/
题目类型: 设计、队列、哈希表、计数、数据流
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2526. 找到数据流中的连续整数 - 给你一个整数数据流，请你实现一个数据结构，检查数据流中最后 k 个整数是否 等于 给定值 value 。 请你实现 DataStream 类： * DataStream(int value, int k) 用两个整数 value 和 k 初始化一个空的整数数据流。 * boolean consec(int num) 将 num 添加到整数数据流。如果后 k 个整数都等于 value ，返回 true ，否则返回 false 。如果少于 k 个整数，条件不满足，所以也返回 false 。 示例 1： 输入： ["DataStream", "consec", "consec", "consec", "consec"] [[4, 3], [4], [4], [4], [3]] 输出： [null, false, false, true, false] 解释： DataStream dataStream = new DataStream(4, 3); // value = 4, k = 3 dataStream.consec(4); // 数据流中只有 1 个整数，所以返回 False 。 dataStream.consec(4); // 数据流中只有 2 个整数 // 由于 2 小于 k ，返回 False 。 dataStream.consec(4); // 数据流最后 3 个整数都等于 value， 所以返回 True 。 dataStream.consec(3); // 最后 k 个整数分别是 [4,4,3] 。 // 由于 3 不等于 value ，返回 False 。 提示： * 1 <= value, num <= 109 * 1 <= k <= 105 * 至多调用 consec 次数为 105 次。
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
