# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100332
标题: 招式拆解 I
难度: medium
链接: https://leetcode.cn/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/
题目类型: 哈希表、字符串、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 167. 招式拆解 I - 某套连招动作记作序列 arr，其中 arr[i] 为第 i 个招式的名字。请返回 arr 中最多可以出连续不重复的多少个招式。 示例 1： 输入：arr = "dbascDdad" 输出：6 解释：因为连续且最长的招式序列是 "dbascD" 或 "bascDd"，所以其长度为 6。 示例 2： 输入：arr = "KKK" 输出：1 解释：因为无重复字符的最长子串是 "K"，所以其长度为 1。 示例 3： 输入：arr = "pwwkew" 输出：3 解释：因为连续且最长的招式序列是 "wke"，所以其长度为 3。 请注意区分 子串 与 子序列 的概念：你的答案必须是 连续招式 的长度，也就是 子串。而 "pwke" 是一个非连续的 子序列，不是 子串。 提示： * 0 <= arr.length <= 40000 * arr 由英文字母、数字、符号和空格组成。 注意：本题与主站 3 题相同：https://leetcode.cn/problems/longest-substring-without-repeating-characters/ [https://leetcode.cn/problems/longest-substring-without-repeating-characters/]
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
