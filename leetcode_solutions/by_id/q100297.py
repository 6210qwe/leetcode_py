# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100297
标题: 模糊搜索验证
难度: hard
链接: https://leetcode.cn/problems/zheng-ze-biao-da-shi-pi-pei-lcof/
题目类型: 递归、字符串、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 137. 模糊搜索验证 - 请设计一个程序来支持用户在文本编辑器中的模糊搜索功能。用户输入内容中可能使用到如下两种通配符： * '.' 匹配任意单个字符。 * '*' 匹配零个或多个前面的那一个元素。 请返回用户输入内容 input 所有字符是否可以匹配原文字符串 article。 示例 1： 输入：article = "aa", input = "a" 输出：false 解释："a" 无法匹配 "aa" 整个字符串。 示例 2： 输入：article = "aa", input = "a*" 输出：true 解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。 示例 3： 输入：article = "ab", input = ".*" 输出：true 解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。 提示： * 1 <= article.length <= 20 * 1 <= input.length <= 20 * article 只包含从 a-z 的小写字母。 * input 只包含从 a-z 的小写字母，以及字符 . 和 * 。 * 保证每次出现字符 * 时，前面都匹配到有效的字符 注意：本题与主站 10 题相同：https://leetcode.cn/problems/regular-expression-matching/ [https://leetcode.cn/problems/regular-expression-matching/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来解决正则表达式的匹配问题。

算法步骤:
1. 初始化一个二维数组 dp，其中 dp[i][j] 表示 s 的前 i 个字符和 p 的前 j 个字符是否匹配。
2. 设置初始条件 dp[0][0] = True，表示空字符串和空模式是匹配的。
3. 处理模式中的 '*' 字符，更新 dp 数组。
4. 根据当前字符和模式字符进行状态转移。
5. 返回 dp[len(s)][len(p)] 的值。

关键点:
- 使用动态规划避免了递归的重复计算。
- 通过状态转移方程处理不同情况下的匹配。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n)，其中 m 是 article 的长度，n 是 input 的长度。
空间复杂度: O(m * n)，用于存储 dp 数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def is_match(article: str, input: str) -> bool:
    """
    函数式接口 - 判断 article 是否匹配 input
    """
    m, n = len(article), len(input)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True

    # 处理 input 中的 '*' 字符
    for j in range(1, n + 1):
        if input[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if input[j - 1] == article[i - 1] or input[j - 1] == '.':
                dp[i][j] = dp[i - 1][j - 1]
            elif input[j - 1] == '*':
                dp[i][j] = dp[i][j - 2]
                if input[j - 2] == article[i - 1] or input[j - 2] == '.':
                    dp[i][j] = dp[i][j] or dp[i - 1][j]

    return dp[m][n]


Solution = create_solution(is_match)