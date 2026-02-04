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
核心思想: 使用滑动窗口和哈希表来记录字符的最新位置，以找到最长的无重复字符子串。

算法步骤:
1. 初始化两个指针 left 和 right 作为滑动窗口的左右边界，以及一个哈希表 char_index_map 来存储字符及其最新位置。
2. 遍历字符串，用 right 指针扩展窗口。
3. 如果当前字符已经在哈希表中存在且其位置在当前窗口内，则移动 left 指针到该字符的下一个位置。
4. 更新哈希表中当前字符的位置。
5. 记录当前窗口的最大长度。

关键点:
- 使用哈希表记录字符的最新位置，以便快速判断是否需要移动 left 指针。
- 滑动窗口的动态调整确保了每个字符只被处理一次。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是字符串的长度。每个字符最多被处理两次（一次右移 right 指针，一次左移 left 指针）。
空间复杂度: O(min(m, n))，其中 m 是字符集的大小，n 是字符串的长度。哈希表的大小最多为字符集的大小。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(arr: str) -> int:
    """
    函数式接口 - 返回最长无重复字符子串的长度
    """
    if not arr:
        return 0

    left, right = 0, 0
    char_index_map = {}
    max_length = 0

    while right < len(arr):
        if arr[right] in char_index_map and char_index_map[arr[right]] >= left:
            left = char_index_map[arr[right]] + 1
        char_index_map[arr[right]] = right
        max_length = max(max_length, right - left + 1)
        right += 1

    return max_length


Solution = create_solution(solution_function_name)