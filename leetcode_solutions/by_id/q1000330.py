# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000330
标题: 键值映射
难度: medium
链接: https://leetcode.cn/problems/z1R5dt/
题目类型: 设计、字典树、哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 066. 键值映射 - 实现一个 MapSum 类，支持两个方法，insert 和 sum： * MapSum() 初始化 MapSum 对象 * void insert(String key, int val) 插入 key-val 键值对，字符串表示键 key ，整数表示值 val 。如果键 key 已经存在，那么原来的键值对将被替代成新的键值对。 * int sum(string prefix) 返回所有以该前缀 prefix 开头的键 key 的值的总和。 示例： 输入： inputs = ["MapSum", "insert", "sum", "insert", "sum"] inputs = [[], ["apple", 3], ["ap"], ["app", 2], ["ap"]] 输出： [null, null, 3, null, 5] 解释： MapSum mapSum = new MapSum(); mapSum.insert("apple", 3); mapSum.sum("ap"); // return 3 (apple = 3) mapSum.insert("app", 2); mapSum.sum("ap"); // return 5 (apple + app = 3 + 2 = 5) 提示： * 1 <= key.length, prefix.length <= 50 * key 和 prefix 仅由小写英文字母组成 * 1 <= val <= 1000 * 最多调用 50 次 insert 和 sum 注意：本题与主站 677 题相同： https://leetcode.cn/problems/map-sum-pairs/ [https://leetcode.cn/problems/map-sum-pairs/]
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
