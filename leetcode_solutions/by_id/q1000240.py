# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000240
标题: 分割回文串
难度: medium
链接: https://leetcode.cn/problems/M99OJA/
题目类型: 深度优先搜索、广度优先搜索、图、哈希表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 086. 分割回文串 - 给定一个字符串 s ，请将 s 分割成一些子串，使每个子串都是 回文串 ，返回 s 所有可能的分割方案。 回文串 是正着读和反着读都一样的字符串。 示例 1： 输入：s = "google" 输出：[["g","o","o","g","l","e"],["g","oo","g","l","e"],["goog","l","e"]] 示例 2： 输入：s = "aab" 输出：[["a","a","b"],["aa","b"]] 示例 3： 输入：s = "a" 输出：[["a"]] 提示： * 1 <= s.length <= 16 * s 仅由小写英文字母组成 注意：本题与主站 131 题相同： https://leetcode.cn/problems/palindrome-partitioning/ [https://leetcode.cn/problems/palindrome-partitioning/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 回溯 + 预处理回文表

算法步骤:
1. 预处理一个二维布尔数组 is_pal[i][j]，表示 s[i:j+1] 是否为回文：
   - 从后往前枚举 i，从 i 到末尾枚举 j
   - is_pal[i][j] = (s[i] == s[j]) 且 (j - i < 2 或 is_pal[i+1][j-1])
2. 使用回溯函数 dfs(start, path)：
   - 若 start == len(s)，将 path 加入结果
   - 从 end = start 到 len(s)-1：
       * 若 is_pal[start][end] 为 True，将 s[start:end+1] 加入 path，递归 dfs(end+1, path)，回溯时弹出
3. 返回所有收集到的 path

关键点:
- 预处理回文表可将回文判断从 O(n) 降为 O(1)，整体复杂度降低
- 回溯遍历所有可能的分割点组合
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2 + C) - 预处理回文 O(n^2)，C 为所有结果长度总和
空间复杂度: O(n^2) - 存储回文表；递归栈 O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def partition(s: str) -> List[List[str]]:
    """
    函数式接口 - 分割回文串
    """
    n = len(s)
    is_pal = [[False] * n for _ in range(n)]

    # 预处理回文表
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if s[i] == s[j] and (j - i < 2 or is_pal[i + 1][j - 1]):
                is_pal[i][j] = True

    res: List[List[str]] = []
    path: List[str] = []

    def dfs(start: int) -> None:
        if start == n:
            res.append(path[:])
            return
        for end in range(start, n):
            if is_pal[start][end]:
                path.append(s[start:end + 1])
                dfs(end + 1)
                path.pop()

    dfs(0)
    return res


Solution = create_solution(partition)
