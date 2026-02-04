# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1473
标题: Find the Longest Substring Containing Vowels in Even Counts
难度: medium
链接: https://leetcode.cn/problems/find-the-longest-substring-containing-vowels-in-even-counts/
题目类型: 位运算、哈希表、字符串、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1371. 每个元音包含偶数次的最长子字符串 - 给你一个字符串 s ，请你返回满足以下条件的最长子字符串的长度：每个元音字母，即 'a'，'e'，'i'，'o'，'u' ，在子字符串中都恰好出现了偶数次。 示例 1： 输入：s = "eleetminicoworoep" 输出：13 解释：最长子字符串是 "leetminicowor" ，它包含 e，i，o 各 2 个，以及 0 个 a，u 。 示例 2： 输入：s = "leetcodeisgreat" 输出：5 解释：最长子字符串是 "leetc" ，其中包含 2 个 e 。 示例 3： 输入：s = "bcbcbc" 输出：6 解释：这个示例中，字符串 "bcbcbc" 本身就是最长的，因为所有的元音 a，e，i，o，u 都出现了 0 次。 提示： * 1 <= s.length <= 5 x 10^5 * s 只包含小写英文字母。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用位运算和哈希表来记录每个元音字母的奇偶状态，并利用前缀和的思想找到最长的符合条件的子字符串。

算法步骤:
1. 初始化一个哈希表 `state_map`，用于存储每个状态第一次出现的位置，初始状态为 0。
2. 遍历字符串 `s`，使用一个整数 `state` 来表示当前元音字母的奇偶状态。
3. 对于每个字符，更新 `state` 的值。
4. 如果 `state` 已经在 `state_map` 中出现过，则计算当前索引与 `state` 第一次出现的索引之间的距离，并更新最大长度。
5. 如果 `state` 没有在 `state_map` 中出现过，则将其加入 `state_map`。

关键点:
- 使用位运算来表示元音字母的奇偶状态。
- 利用哈希表记录每个状态第一次出现的位置。
- 通过前缀和的思想找到最长的符合条件的子字符串。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是字符串 `s` 的长度。
空间复杂度: O(1)，状态 `state` 的取值范围是 0 到 31，因此哈希表的大小是常数级的。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def find_the_longest_substring(s: str) -> int:
    """
    函数式接口 - 返回满足每个元音字母在子字符串中都恰好出现了偶数次的最长子字符串的长度
    """
    # 哈希表记录每个状态第一次出现的位置
    state_map = {0: -1}
    state = 0
    max_length = 0
    
    # 位运算掩码
    mask_a = 1 << 0
    mask_e = 1 << 1
    mask_i = 1 << 2
    mask_o = 1 << 3
    mask_u = 1 << 4
    
    for i, char in enumerate(s):
        if char == 'a':
            state ^= mask_a
        elif char == 'e':
            state ^= mask_e
        elif char == 'i':
            state ^= mask_i
        elif char == 'o':
            state ^= mask_o
        elif char == 'u':
            state ^= mask_u
        
        if state in state_map:
            max_length = max(max_length, i - state_map[state])
        else:
            state_map[state] = i
    
    return max_length


Solution = create_solution(find_the_longest_substring)