# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1297
标题: Maximum Number of Balloons
难度: easy
链接: https://leetcode.cn/problems/maximum-number-of-balloons/
题目类型: 哈希表、字符串、计数
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1189. “气球” 的最大数量 - 给你一个字符串 text，你需要使用 text 中的字母来拼凑尽可能多的单词 "balloon"（气球）。 字符串 text 中的每个字母最多只能被使用一次。请你返回最多可以拼凑出多少个单词 "balloon"。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/09/14/1536_ex1_upd.jpeg] 输入：text = "nlaebolko" 输出：1 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/09/14/1536_ex2_upd.jpeg] 输入：text = "loonbalxballpoon" 输出：2 示例 3： 输入：text = "leetcode" 输出：0 提示： * 1 <= text.length <= 104 * text 全部由小写英文字母组成 注意：本题与 2287. 重排字符形成目标字符串 [https://leetcode.cn/problems/rearrange-characters-to-make-target-string/] 相同。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 计算给定字符串中每个字符的出现次数，然后根据 "balloon" 中每个字符的出现次数来确定最多可以拼凑出多少个 "balloon"。

算法步骤:
1. 统计字符串 text 中每个字符的出现次数。
2. 统计 "balloon" 中每个字符的出现次数。
3. 计算每个字符在 text 中的出现次数与 "balloon" 中的出现次数的最小倍数。

关键点:
- 使用字典来统计字符出现次数。
- 特别处理 "l" 和 "o" 这两个字符，因为它们在 "balloon" 中出现两次。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是字符串 text 的长度。我们需要遍历整个字符串来统计字符出现次数。
空间复杂度: O(1)，因为字符集是固定的（只有 26 个小写字母），所以字典的大小是常数级别的。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def max_number_of_balloons(text: str) -> int:
    """
    函数式接口 - 计算最多可以拼凑出多少个 "balloon"
    """
    # 统计 "balloon" 中每个字符的出现次数
    balloon_count = {"b": 1, "a": 1, "l": 2, "o": 2, "n": 1}
    
    # 统计 text 中每个字符的出现次数
    text_count = {}
    for char in text:
        if char in balloon_count:
            text_count[char] = text_count.get(char, 0) + 1
    
    # 计算最多可以拼凑出多少个 "balloon"
    min_count = float('inf')
    for char, count in balloon_count.items():
        if char not in text_count or text_count[char] < count:
            return 0
        min_count = min(min_count, text_count[char] // count)
    
    return min_count


Solution = create_solution(max_number_of_balloons)