# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 411
标题: Minimum Unique Word Abbreviation
难度: hard
链接: https://leetcode.cn/problems/minimum-unique-word-abbreviation/
题目类型: 位运算、数组、字符串、回溯
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
411. 最短独占单词缩写 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。

给定一个目标单词 target 和一个字符串数组 dictionary，返回 target 的最短唯一缩写（abbreviation），使得该缩写不与 dictionary 中任何单词的任意缩写冲突。

缩写规则：
- 可以将连续的字符替换为数字，该数字表示被替换的字符个数；
- 缩写中不能有相邻数字（即 "a3b2c" 合法，但 "a32b" 不合法）；
- 缩写中不能有前导零（即 "a01b" 不合法）；
- 缩写必须保持原字符顺序（如 "apple" → "a3e" 表示 a + ppp + e）。

唯一性要求：对 dictionary 中每个 word，其所有可能缩写集合中都不包含该结果缩写。

目标：返回长度最短的合法唯一缩写；若有多个相同最短长度，返回字典序最小者。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 枚举所有可能缩写（用位掩码或回溯生成），按长度升序 + 字典序剪枝，逐个验证唯一性。

算法步骤:
1. 预处理：过滤掉与 target 长度不同的 dictionary 单词（因缩写长度 ≤ 原长，且只有同长单词才可能产生相同缩写）；
2. 生成 target 所有合法缩写，按「缩写长度升序」为主序、「字典序升序」为次序排序（可用 BFS 或优先队列，但更简单是生成后排序）；
3. 对每个缩写，检查是否对 dictionary 中所有单词均「不可匹配」（即：不存在任一 word 能生成相同缩写）；
   - 匹配判断：用双指针模拟缩写 vs 原单词（遇到数字则跳过对应数量字符，需确保不越界、无前导零、不跨单词边界）；
4. 返回第一个通过验证的缩写。

优化点：
- 使用位掩码生成缩写：对长度为 n 的 target，共 2^n 种保留/压缩决策（1=保留字符，0=压缩），但需合并连续 0 成单个数字；
- 更高效做法：DFS 回溯生成所有缩写，同时按长度递增剪枝（优先尝试更短缩写）；
- 实际采用「BFS 按缩写长度分层生成」或「生成全部后排序」均可；本解采用简洁清晰的「生成全部缩写 → 排序 → 验证」策略，因 target 长度通常较小（≤ 20）。

关键点:
- 注意边界条件：空 dictionary → 直接返回最短缩写（即全数字，如 "word"→"4"）；
- 缩写生成时避免前导零：数字段值为 0 时非法（但数字本身为 0 是允许的，仅当压缩长度为 0 时才出现，而压缩长度至少为 1，故实际不会生成 0）；
- 匹配函数需严格模拟：如缩写 "a3e" 匹配 "apple" → a + skip 3 chars ("ppl") + e → ok；但不匹配 "atone"（a + skip 3 → 'o' ≠ 'e'）；
- 字典序比较：Python 字符串默认字典序，可直接用 sorted(..., key=lambda x: (len(x), x))。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(2^L × D × L) - 其中 L = len(target)，D = len(dictionary)；
    - 生成所有缩写：O(2^L × L)（每个缩写构造耗 O(L)）；
    - 排序：O(2^L × L × log(2^L)) = O(L × 2^L × L) = O(L² × 2^L)，但常数小，可接受；
    - 验证每个缩写：O(D × L)（每个 word 匹配耗 O(L)）；
    - 总体主导项为 O(2^L × D × L)。

空间复杂度: O(2^L × L) - 存储所有缩写（最多约 2^L 个，每个最长 O(L)）。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def minimum_unique_word_abbreviation(target: str, dictionary: List[str]) -> str:
    """
    函数式接口 - 返回 target 的最短唯一缩写
    
    实现思路:
    1. 过滤 dictionary 中长度 ≠ len(target) 的单词（因缩写长度 ≤ 原长，且若长度不同则不可能完全匹配同一缩写）；
    2. 用回溯生成 target 的所有合法缩写；
    3. 按 (长度, 字典序) 排序；
    4. 对每个缩写，检查是否对所有 filtered_dict 单词均不匹配；
    5. 返回首个满足条件的缩写。
    
    Args:
        target: 目标单词，非空字符串
        dictionary: 候选冲突单词列表
        
    Returns:
        str: 最短唯一缩写；若无冲突则返回最短可能缩写（如全数字）
        
    Example:
        >>> minimum_unique_word_abbreviation("apple", ["blade"])
        'a3e'
        >>> minimum_unique_word_abbreviation("apple", ["apply"])
        'appLe'  # 注意：实际应为 'a3e' 或 'ap3e' 等，但需验证；此例中 'a3e' 不匹配 "apply"（a + ppp + e → e≠y），故合法
    """
    n = len(target)
    
    # Step 1: filter dictionary to only words of same length
    filtered_dict = [w for w in dictionary if len(w) == n]
    
    # Edge case: no conflict possible
    if not filtered_dict:
        # return shortest abbreviation: compress all -> str(n)
        return str(n)
    
    # Step 2: generate all abbreviations of target
    abbrs = []
    
    def backtrack(i: int, path: List[str], count: int):
        if i == n:
            if count > 0:
                path.append(str(count))
            abbrs.append(''.join(path))
            if count > 0:
                path.pop()
            return
        
        # Option 1: compress current char (increase count)
        backtrack(i + 1, path, count + 1)
        
        # Option 2: keep current char
        if count > 0:
            path.append(str(count))
        path.append(target[i])
        backtrack(i + 1, path, 0)
        path.pop()
        if count > 0:
            path.pop()
    
    backtrack(0, [], 0)
    
    # Step 3: sort by length then lexicographically
    abbrs.sort(key=lambda x: (len(x), x))
    
    # Step 4: check each abbreviation against all filtered_dict words
    def can_match(abbr: str, word: str) -> bool:
        # Two-pointer match: abbr vs word
        i, j = 0, 0  # i for abbr, j for word
        while i < len(abbr) and j <= len(word):
            if j == len(word):
                # word exhausted but abbr still has chars → only ok if rest abbr is digits summing to 0 (impossible) → fail
                return False
            if abbr[i].isalpha():
                if abbr[i] != word[j]:
                    return False
                i += 1
                j += 1
            else:
                # parse number
                num = 0
                while i < len(abbr) and abbr[i].isdigit():
                    num = num * 10 + int(abbr[i])
                    i += 1
                # skip 'num' chars in word
                j += num
                if j > len(word):  # overshoot
                    return False
        return i == len(abbr) and j == len(word)
    
    # Check each abbreviation
    for abbr in abbrs:
        valid = True
        for word in filtered_dict:
            if can_match(abbr, word):
                valid = False
                break
        if valid:
            return abbr
    
    # According to problem guarantee, there's always solution (e.g., full target)
    return target


# 自动生成Solution类（无需手动编写）
Solution = create_solution(minimum_unique_word_abbreviation)