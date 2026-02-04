# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2393
标题: Match Substring After Replacement
难度: hard
链接: https://leetcode.cn/problems/match-substring-after-replacement/
题目类型: 数组、哈希表、字符串、字符串匹配
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2301. 替换字符后匹配 - 给你两个字符串 s 和 sub 。同时给你一个二维字符数组 mappings ，其中 mappings[i] = [oldi, newi] 表示你可以将 sub 中任意数目的 oldi 字符替换为 newi 。sub 中每个字符 不能 被替换超过一次。 如果使用 mappings 替换 0 个或者若干个字符，可以将 sub 变成 s 的一个子字符串，请你返回 true，否则返回 false 。 一个 子字符串 是字符串中连续非空的字符序列。 示例 1： 输入：s = "fool3e7bar", sub = "leet", mappings = [["e","3"],["t","7"],["t","8"]] 输出：true 解释：将 sub 中第一个 'e' 用 '3' 替换，将 't' 用 '7' 替换。 现在 sub = "l3e7" ，它是 s 的子字符串，所以我们返回 true 。 示例 2： 输入：s = "fooleetbar", sub = "f00l", mappings = [["o","0"]] 输出：false 解释：字符串 "f00l" 不是 s 的子串且没有可以进行的修改。 注意我们不能用 'o' 替换 '0' 。 示例 3： 输入：s = "Fool33tbaR", sub = "leetd", mappings = [["e","3"],["t","7"],["t","8"],["d","b"],["p","b"]] 输出：true 解释：将 sub 里第一个和第二个 'e' 用 '3' 替换，用 'b' 替换 sub 里的 'd' 。 得到 sub = "l33tb" ，它是 s 的子字符串，所以我们返回 true 。 提示： * 1 <= sub.length <= s.length <= 5000 * 0 <= mappings.length <= 1000 * mappings[i].length == 2 * oldi != newi * s 和 sub 只包含大写和小写英文字母和数字。 * oldi 和 newi 是大写、小写字母或者是个数字。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表记录每个字符可以替换成的字符集合，然后通过滑动窗口检查 sub 是否可以通过替换变成 s 的子字符串。

算法步骤:
1. 构建一个哈希表，记录每个字符可以替换成的字符集合。
2. 使用滑动窗口遍历 s，检查 sub 是否可以通过替换变成 s 的子字符串。
3. 对于每个窗口位置，逐字符检查 sub 和 s 的对应字符是否相同或可以通过映射替换。

关键点:
- 使用哈希表高效记录字符替换关系。
- 通过滑动窗口减少重复计算。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m)，其中 n 是 s 的长度，m 是 sub 的长度。
空间复杂度: O(k)，其中 k 是 mappings 的长度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def can_match_substring(s: str, sub: str, mappings: List[List[str]]) -> bool:
    # 构建字符替换哈希表
    char_map = {}
    for old_char, new_char in mappings:
        if old_char not in char_map:
            char_map[old_char] = set()
        char_map[old_char].add(new_char)

    # 滑动窗口检查
    n, m = len(s), len(sub)
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if s[i + j] != sub[j]:
                if sub[j] not in char_map or s[i + j] not in char_map[sub[j]]:
                    match = False
                    break
        if match:
            return True
    return False


Solution = create_solution(can_match_substring)