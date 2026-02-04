# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1360
标题: Maximum Length of a Concatenated String with Unique Characters
难度: medium
链接: https://leetcode.cn/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
题目类型: 位运算、数组、字符串、回溯
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1239. 串联字符串的最大长度 - 给定一个字符串数组 arr，字符串 s 是将 arr 的含有 不同字母 的 子序列 字符串 连接 所得的字符串。 请返回所有可行解 s 中最长长度。 子序列 是一种可以从另一个数组派生而来的数组，通过删除某些元素或不删除元素而不改变其余元素的顺序。 示例 1： 输入：arr = ["un","iq","ue"] 输出：4 解释：所有可能的串联组合是： - "" - "un" - "iq" - "ue" - "uniq" ("un" + "iq") - "ique" ("iq" + "ue") 最大长度为 4。 示例 2： 输入：arr = ["cha","r","act","ers"] 输出：6 解释：可能的解答有 "chaers" 和 "acters"。 示例 3： 输入：arr = ["abcdefghijklmnopqrstuvwxyz"] 输出：26 提示： * 1 <= arr.length <= 16 * 1 <= arr[i].length <= 26 * arr[i] 中只含有小写英文字母
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用回溯法来生成所有可能的字符串组合，并使用位掩码来检查字符是否重复。

算法步骤:
1. 初始化最大长度为 0。
2. 定义一个递归函数 `backtrack`，参数包括当前索引、当前字符串和当前字符集的位掩码。
3. 在递归函数中，遍历从当前索引到数组末尾的所有字符串：
   - 如果当前字符串与已选字符集没有重复字符，则更新最大长度，并继续递归。
   - 否则，跳过当前字符串。
4. 返回最大长度。

关键点:
- 使用位掩码来高效地检查字符是否重复。
- 回溯法确保所有可能的组合都被考虑。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(2^n)，其中 n 是数组 arr 的长度。最坏情况下需要检查所有子集。
空间复杂度: O(n)，递归调用栈的深度最多为 n。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def max_length(arr: List[str]) -> int:
    """
    函数式接口 - 返回串联字符串的最大长度
    """
    def backtrack(index: int, current: str, bitmask: int) -> None:
        nonlocal max_len
        max_len = max(max_len, len(current))
        
        for i in range(index, len(arr)):
            if (bitmask & bitmasks[i]) == 0:
                backtrack(i + 1, current + arr[i], bitmask | bitmasks[i])
    
    max_len = 0
    bitmasks = []
    
    for s in arr:
        mask = 0
        for c in s:
            idx = ord(c) - ord('a')
            if (mask >> idx) & 1:
                mask = 0
                break
            mask |= 1 << idx
        bitmasks.append(mask)
    
    backtrack(0, "", 0)
    return max_len


Solution = create_solution(max_length)