# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2186
标题: Count Vowel Substrings of a String
难度: easy
链接: https://leetcode.cn/problems/count-vowel-substrings-of-a-string/
题目类型: 哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2062. 统计字符串中的元音子字符串 - 子字符串 是字符串中的一个连续（非空）的字符序列。 元音子字符串 是 仅 由元音（'a'、'e'、'i'、'o' 和 'u'）组成的一个子字符串，且必须包含 全部五种 元音。 给你一个字符串 word ，统计并返回 word 中 元音子字符串的数目 。 示例 1： 输入：word = "aeiouu" 输出：2 解释：下面列出 word 中的元音子字符串（斜体加粗部分）： - "aeiouu" - "aeiouu" 示例 2： 输入：word = "unicornarihan" 输出：0 解释：word 中不含 5 种元音，所以也不会存在元音子字符串。 示例 3： 输入：word = "cuaieuouac" 输出：7 解释：下面列出 word 中的元音子字符串（斜体加粗部分）： - "cuaieuouac" - "cuaieuouac" - "cuaieuouac" - "cuaieuouac" - "cuaieuouac" - "cuaieuouac" - "cuaieuouac" 示例 4： 输入：word = "bbaeixoubb" 输出：0 解释：所有包含全部五种元音的子字符串都含有辅音，所以不存在元音子字符串。 提示： * 1 <= word.length <= 100 * word 仅由小写英文字母组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滑动窗口来找到所有包含五个元音的子字符串。

算法步骤:
1. 初始化两个指针 `left` 和 `right`，分别表示当前窗口的左右边界。
2. 使用一个集合 `vowels` 来存储当前窗口内的元音。
3. 遍历字符串 `word`，使用 `right` 指针扩展窗口，直到窗口内包含所有五个元音。
4. 如果窗口内包含所有五个元音，则将 `left` 指针向右移动，直到窗口内不再包含所有五个元音，并记录满足条件的子字符串数量。
5. 重复步骤 3 和 4，直到遍历完整个字符串。

关键点:
- 使用滑动窗口来高效地找到所有包含五个元音的子字符串。
- 通过移动 `left` 指针来缩小窗口，确保每个子字符串都被正确计数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是字符串 `word` 的长度。每个字符最多被访问两次（一次由 `right` 指针，一次由 `left` 指针）。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def count_vowel_substrings(word: str) -> int:
    """
    函数式接口 - 统计字符串中的元音子字符串
    """
    vowels = set('aeiou')
    n = len(word)
    count = 0
    
    for left in range(n):
        if word[left] not in vowels:
            continue
        current_vowels = set()
        for right in range(left, n):
            if word[right] in vowels:
                current_vowels.add(word[right])
                if current_vowels == vowels:
                    count += 1
            else:
                break
    
    return count


Solution = create_solution(count_vowel_substrings)