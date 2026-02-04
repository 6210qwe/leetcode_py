# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 973
标题: Stamping The Sequence
难度: hard
链接: https://leetcode.cn/problems/stamping-the-sequence/
题目类型: 栈、贪心、队列、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
936. 戳印序列 - 你想要用小写字母组成一个目标字符串 target。 开始的时候，序列由 target.length 个 '?' 记号组成。而你有一个小写字母印章 stamp。 在每个回合，你可以将印章放在序列上，并将序列中的每个字母替换为印章上的相应字母。你最多可以进行 10 * target.length 个回合。 举个例子，如果初始序列为 "?????"，而你的印章 stamp 是 "abc"，那么在第一回合，你可以得到 "abc??"、"?abc?"、"??abc"。（请注意，印章必须完全包含在序列的边界内才能盖下去。） 如果可以印出序列，那么返回一个数组，该数组由每个回合中被印下的最左边字母的索引组成。如果不能印出序列，就返回一个空数组。 例如，如果序列是 "ababc"，印章是 "abc"，那么我们就可以返回与操作 "?????" -> "abc??" -> "ababc" 相对应的答案 [0, 2]； 另外，如果可以印出序列，那么需要保证可以在 10 * target.length 个回合内完成。任何超过此数字的答案将不被接受。 示例 1： 输入：stamp = "abc", target = "ababc" 输出：[0,2] （[1,0,2] 以及其他一些可能的结果也将作为答案被接受） 示例 2： 输入：stamp = "abca", target = "aabcaca" 输出：[3,0,1] 提示： 1. 1 <= stamp.length <= target.length <= 1000 2. stamp 和 target 只包含小写字母。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法，从后往前逐步替换 target 中的字符，直到所有字符都被替换为 '?'。

算法步骤:
1. 定义一个辅助函数 `can_replace`，用于判断是否可以在某个位置替换印章。
2. 初始化一个列表 `res` 用于存储每次替换的位置。
3. 使用一个循环，不断尝试替换 target 中的字符，直到无法再替换为止。
4. 如果最终 target 全部变为 '?'，则返回结果 `res` 的逆序，否则返回空列表。

关键点:
- 从后往前替换，确保每次替换都是最优的。
- 使用贪心策略，尽可能多地替换字符。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m)，其中 n 是 target 的长度，m 是 stamp 的长度。每次替换操作的时间复杂度是 O(m)，最多进行 10 * n 次替换。
空间复杂度: O(n)，用于存储结果和中间状态。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List


def can_replace(target: str, stamp: str, start: int) -> bool:
    """
    判断是否可以在 target 的 start 位置替换 stamp。
    """
    for i in range(len(stamp)):
        if target[start + i] != '?' and target[start + i] != stamp[i]:
            return False
    return True


def move_stamp(target: str, stamp: str, res: List[int]) -> str:
    """
    尝试在 target 中找到可以替换 stamp 的位置，并进行替换。
    """
    new_target = list(target)
    found = False
    for i in range(len(target) - len(stamp) + 1):
        if can_replace(target, stamp, i):
            found = True
            res.append(i)
            for j in range(len(stamp)):
                new_target[i + j] = '?'
    return ''.join(new_target), found


def solution_function_name(stamp: str, target: str) -> List[int]:
    """
    函数式接口 - 实现戳印序列
    """
    res = []
    max_turns = 10 * len(target)
    turns = 0
    
    while turns < max_turns:
        target, found = move_stamp(target, stamp, res)
        if not found:
            break
        turns += 1
    
    if target == '?' * len(target):
        return res[::-1]
    else:
        return []


Solution = create_solution(solution_function_name)