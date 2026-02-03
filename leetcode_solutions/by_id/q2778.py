# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2778
标题: Frequency Tracker
难度: medium
链接: https://leetcode.cn/problems/frequency-tracker/
题目类型: 设计、哈希表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2671. 频率跟踪器 - 请你设计并实现一个能够对其中的值进行跟踪的数据结构，并支持对频率相关查询进行应答。 实现 FrequencyTracker 类： * FrequencyTracker()：使用一个空数组初始化 FrequencyTracker 对象。 * void add(int number)：添加一个 number 到数据结构中。 * void deleteOne(int number)：从数据结构中删除一个 number 。数据结构 可能不包含 number ，在这种情况下不删除任何内容。 * bool hasFrequency(int frequency): 如果数据结构中存在出现 frequency 次的数字，则返回 true，否则返回 false。 示例 1： 输入 ["FrequencyTracker", "add", "add", "hasFrequency"] [[], [3], [3], [2]] 输出 [null, null, null, true] 解释 FrequencyTracker frequencyTracker = new FrequencyTracker(); frequencyTracker.add(3); // 数据结构现在包含 [3] frequencyTracker.add(3); // 数据结构现在包含 [3, 3] frequencyTracker.hasFrequency(2); // 返回 true ，因为 3 出现 2 次 示例 2： 输入 ["FrequencyTracker", "add", "deleteOne", "hasFrequency"] [[], [1], [1], [1]] 输出 [null, null, null, false] 解释 FrequencyTracker frequencyTracker = new FrequencyTracker(); frequencyTracker.add(1); // 数据结构现在包含 [1] frequencyTracker.deleteOne(1); // 数据结构现在为空 [] frequencyTracker.hasFrequency(1); // 返回 false ，因为数据结构为空 示例 3： 输入 ["FrequencyTracker", "hasFrequency", "add", "hasFrequency"] [[], [2], [3], [1]] 输出 [null, false, null, true] 解释 FrequencyTracker frequencyTracker = new FrequencyTracker(); frequencyTracker.hasFrequency(2); // 返回 false ，因为数据结构为空 frequencyTracker.add(3); // 数据结构现在包含 [3] frequencyTracker.hasFrequency(1); // 返回 true ，因为 3 出现 1 次 提示： * 1 <= number <= 105 * 1 <= frequency <= 105 * 最多调用 add、deleteOne 和 hasFrequency 共计 2 * 105 次
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
