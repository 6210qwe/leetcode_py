# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 992
标题: Delete Columns to Make Sorted II
难度: medium
链接: https://leetcode.cn/problems/delete-columns-to-make-sorted-ii/
题目类型: 贪心、数组、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
955. 删列造序 II - 给定由 n 个字符串组成的数组 strs，其中每个字符串长度相等。 选取一个删除索引序列，对于 strs 中的每个字符串，删除对应每个索引处的字符。 比如，有 strs = ["abcdef", "uvwxyz"]，删除索引序列 {0, 2, 3}，删除后 strs 为["bef", "vyz"]。 假设，我们选择了一组删除索引 answer，那么在执行删除操作之后，最终得到的数组的元素是按 字典序（strs[0] <= strs[1] <= strs[2] ... <= strs[n - 1]）排列的，然后请你返回 answer.length 的最小可能值。 示例 1： 输入：strs = ["ca","bb","ac"] 输出：1 解释： 删除第一列后，strs = ["a", "b", "c"]。 现在 strs 中元素是按字典排列的 (即，strs[0] <= strs[1] <= strs[2])。 我们至少需要进行 1 次删除，因为最初 strs 不是按字典序排列的，所以答案是 1。 示例 2： 输入：strs = ["xc","yb","za"] 输出：0 解释： strs 的列已经是按字典序排列了，所以我们不需要删除任何东西。 注意 strs 的行不需要按字典序排列。 也就是说，strs[0][0] <= strs[0][1] <= ... 不一定成立。 示例 3： 输入：strs = ["zyx","wvu","tsr"] 输出：3 解释： 我们必须删掉每一列。 提示： * n == strs.length * 1 <= n <= 100 * 1 <= strs[i].length <= 100 * strs[i] 由小写英文字母组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过贪心算法逐列检查是否需要删除。如果某列使得当前字符串不满足字典序，则该列必须删除。

算法步骤:
1. 初始化一个布尔列表 `keep`，表示每列是否保留。
2. 遍历每一列，检查当前列是否需要删除。
3. 如果当前列需要删除，则更新 `keep` 列表。
4. 返回需要删除的列数。

关键点:
- 使用布尔列表 `keep` 来记录每列是否保留。
- 逐列检查并更新 `keep` 列表。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n)，其中 m 是字符串的长度，n 是字符串的数量。
空间复杂度: O(m)，用于存储布尔列表 `keep`。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def min_deletion_size(strs: List[str]) -> int:
    """
    函数式接口 - 计算需要删除的最小列数以使字符串数组按字典序排列
    """
    if not strs:
        return 0

    m, n = len(strs), len(strs[0])
    keep = [True] * n

    for j in range(n):
        if not keep[j]:
            continue
        for i in range(1, m):
            if strs[i][j] < strs[i - 1][j]:
                keep[j] = False
                break
        if not keep[j]:
            for k in range(j + 1, n):
                if keep[k]:
                    for i in range(1, m):
                        if strs[i][k] < strs[i - 1][k]:
                            keep[k] = False
                            break

    return n - sum(keep)


Solution = create_solution(min_deletion_size)