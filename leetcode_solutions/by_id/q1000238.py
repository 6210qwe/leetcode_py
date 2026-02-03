# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000238
标题: 括号生成
难度: medium
链接: https://leetcode.cn/problems/IDBivT/
题目类型: 字符串、动态规划、回溯
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 085. 括号生成 - 正整数 n 代表生成括号的对数，请设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。 示例 1： 输入：n = 3 输出：["((()))","(()())","(())()","()(())","()()()"] 示例 2： 输入：n = 1 输出：["()"] 提示： * 1 <= n <= 8 注意：本题与主站 22 题相同： https://leetcode.cn/problems/generate-parentheses/ [https://leetcode.cn/problems/generate-parentheses/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 回溯生成所有合法括号串

算法步骤:
1. 使用回溯函数 dfs(path, open_cnt, close_cnt)：
   - path 为当前构造的字符串
   - open_cnt 为已经使用的 '(' 数量
   - close_cnt 为已经使用的 ')' 数量
2. 终止条件：当 path 长度为 2 * n 时，将 path 加入答案
3. 递归扩展：
   - 若 open_cnt < n，可以再添加 '('
   - 若 close_cnt < open_cnt，可以添加 ')'
4. 初始调用 dfs("", 0, 0)

关键点:
- 任何前缀中，')' 数量不能超过 '(' 数量
- 最终 '(' 和 ')' 数量都为 n
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(C_n) 级别，C_n 为第 n 个卡特兰数（解的数量）
空间复杂度: O(n) - 递归深度与当前路径
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def generate_parenthesis(n: int) -> List[str]:
    """
    函数式接口 - 括号生成
    """
    res: List[str] = []

    def dfs(path: str, open_cnt: int, close_cnt: int) -> None:
        if len(path) == 2 * n:
            res.append(path)
            return
        if open_cnt < n:
            dfs(path + "(", open_cnt + 1, close_cnt)
        if close_cnt < open_cnt:
            dfs(path + ")", open_cnt, close_cnt + 1)

    dfs("", 0, 0)
    return res


Solution = create_solution(generate_parenthesis)
