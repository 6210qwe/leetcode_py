# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000277
标题: 交错字符串
难度: medium
链接: https://leetcode.cn/problems/IY6buf/
题目类型: 字符串、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 096. 交错字符串 - 给定三个字符串 s1、s2、s3，请判断 s3 能不能由 s1 和 s2 交织（交错） 组成。 两个字符串 s 和 t 交织 的定义与过程如下，其中每个字符串都会被分割成若干 非空 子字符串： * s = s1 + s2 + ... + sn * t = t1 + t2 + ... + tm * |n - m| <= 1 * 交织 是 s1 + t1 + s2 + t2 + s3 + t3 + ... 或者 t1 + s1 + t2 + s2 + t3 + s3 + ... 提示：a + b 意味着字符串 a 和 b 连接。 示例 1： [https://assets.leetcode.com/uploads/2020/09/02/interleave.jpg] 输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac" 输出：true 示例 2： 输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc" 输出：false 示例 3： 输入：s1 = "", s2 = "", s3 = "" 输出：true 提示： * 0 <= s1.length, s2.length <= 100 * 0 <= s3.length <= 200 * s1、s2、和 s3 都由小写英文字母组成 注意：本题与主站 97 题相同： https://leetcode.cn/problems/interleaving-string/ [https://leetcode.cn/problems/interleaving-string/]
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
