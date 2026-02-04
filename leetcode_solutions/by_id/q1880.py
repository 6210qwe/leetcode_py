# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1880
标题: Largest Merge Of Two Strings
难度: medium
链接: https://leetcode.cn/problems/largest-merge-of-two-strings/
题目类型: 贪心、双指针、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1754. 构造字典序最大的合并字符串 - 给你两个字符串 word1 和 word2 。你需要按下述方式构造一个新字符串 merge ：如果 word1 或 word2 非空，选择 下面选项之一 继续操作： * 如果 word1 非空，将 word1 中的第一个字符附加到 merge 的末尾，并将其从 word1 中移除。 * 例如，word1 = "abc" 且 merge = "dv" ，在执行此选项操作之后，word1 = "bc" ，同时 merge = "dva" 。 * 如果 word2 非空，将 word2 中的第一个字符附加到 merge 的末尾，并将其从 word2 中移除。 * 例如，word2 = "abc" 且 merge = "" ，在执行此选项操作之后，word2 = "bc" ，同时 merge = "a" 。 返回你可以构造的字典序 最大 的合并字符串 merge 。 长度相同的两个字符串 a 和 b 比较字典序大小，如果在 a 和 b 出现不同的第一个位置，a 中字符在字母表中的出现顺序位于 b 中相应字符之后，就认为字符串 a 按字典序比字符串 b 更大。例如，"abcd" 按字典序比 "abcc" 更大，因为两个字符串出现不同的第一个位置是第四个字符，而 d 在字母表中的出现顺序位于 c 之后。 示例 1： 输入：word1 = "cabaa", word2 = "bcaaa" 输出："cbcabaaaaa" 解释：构造字典序最大的合并字符串，可行的一种方法如下所示： - 从 word1 中取第一个字符：merge = "c"，word1 = "abaa"，word2 = "bcaaa" - 从 word2 中取第一个字符：merge = "cb"，word1 = "abaa"，word2 = "caaa" - 从 word2 中取第一个字符：merge = "cbc"，word1 = "abaa"，word2 = "aaa" - 从 word1 中取第一个字符：merge = "cbca"，word1 = "baa"，word2 = "aaa" - 从 word1 中取第一个字符：merge = "cbcab"，word1 = "aa"，word2 = "aaa" - 将 word1 和 word2 中剩下的 5 个 a 附加到 merge 的末尾。 示例 2： 输入：word1 = "abcabc", word2 = "abdcaba" 输出："abdcabcabcaba" 提示： * 1 <= word1.length, word2.length <= 3000 * word1 和 word2 仅由小写英文组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法，每次选择当前剩余部分字典序较大的字符串的首字符加入结果。

算法步骤:
1. 初始化两个指针 i 和 j 分别指向 word1 和 word2 的起始位置。
2. 比较 word1[i:] 和 word2[j:] 的字典序，选择较大的那个字符串的首字符加入结果。
3. 移动相应的指针。
4. 重复步骤 2 和 3，直到其中一个字符串被完全处理。
5. 将另一个字符串的剩余部分直接加入结果。

关键点:
- 每次选择当前剩余部分字典序较大的字符串的首字符，确保最终结果是字典序最大的。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 和 m 分别是 word1 和 word2 的长度。每次比较和移动指针的操作都是 O(1)。
空间复杂度: O(n + m)，用于存储结果字符串。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def largest_merge(word1: str, word2: str) -> str:
    """
    函数式接口 - 实现构造字典序最大的合并字符串
    """
    i, j = 0, 0
    merge = []
    
    while i < len(word1) and j < len(word2):
        if word1[i:] > word2[j:]:
            merge.append(word1[i])
            i += 1
        else:
            merge.append(word2[j])
            j += 1
    
    # 将剩余部分加入结果
    merge.extend(word1[i:])
    merge.extend(word2[j:])
    
    return ''.join(merge)


Solution = create_solution(largest_merge)