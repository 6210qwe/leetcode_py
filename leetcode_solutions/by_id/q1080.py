# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1080
标题: Camelcase Matching
难度: medium
链接: https://leetcode.cn/problems/camelcase-matching/
题目类型: 字典树、数组、双指针、字符串、字符串匹配
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1023. 驼峰式匹配 - 给你一个字符串数组 queries，和一个表示模式的字符串 pattern，请你返回一个布尔数组 answer 。只有在待查项 queries[i] 与模式串 pattern 匹配时， answer[i] 才为 true，否则为 false。 如果可以将 小写字母 插入模式串 pattern 得到待查询项 queries[i]，那么待查询项与给定模式串匹配。您可以在模式串中的任何位置插入字符，也可以选择不插入任何字符。 示例 1： 输入：queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB" 输出：[true,false,true,true,false] 示例： "FooBar" 可以这样生成："F" + "oo" + "B" + "ar"。 "FootBall" 可以这样生成："F" + "oot" + "B" + "all". "FrameBuffer" 可以这样生成："F" + "rame" + "B" + "uffer". 示例 2： 输入：queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa" 输出：[true,false,true,false,false] 解释： "FooBar" 可以这样生成："Fo" + "o" + "Ba" + "r". "FootBall" 可以这样生成："Fo" + "ot" + "Ba" + "ll". 示例 3： 输入：queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBaT" 输出：[false,true,false,false,false] 解释： "FooBarTest" 可以这样生成："Fo" + "o" + "Ba" + "r" + "T" + "est". 提示： * 1 <= pattern.length, queries.length <= 100 * 1 <= queries[i].length <= 100 * queries[i] 和 pattern 由英文字母组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用双指针方法来匹配每个查询字符串和模式字符串。

算法步骤:
1. 对于每个查询字符串，使用两个指针分别遍历查询字符串和模式字符串。
2. 如果查询字符串的当前字符是大写字母且不等于模式字符串的当前字符，则返回 False。
3. 如果查询字符串的当前字符是大写字母且等于模式字符串的当前字符，则同时移动两个指针。
4. 如果查询字符串的当前字符是小写字母，则只移动查询字符串的指针。
5. 最后，检查模式字符串的指针是否已经遍历完所有字符。

关键点:
- 使用双指针方法来匹配字符串。
- 重点在于处理大写字母的匹配。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m)，其中 n 是 queries 的长度，m 是每个查询字符串的平均长度。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def camelMatch(queries: List[str], pattern: str) -> List[bool]:
    def is_match(query: str, pattern: str) -> bool:
        p_idx, q_idx = 0, 0
        while q_idx < len(query):
            if p_idx < len(pattern) and query[q_idx] == pattern[p_idx]:
                p_idx += 1
            elif query[q_idx].isupper():
                return False
            q_idx += 1
        return p_idx == len(pattern)

    return [is_match(query, pattern) for query in queries]

Solution = create_solution(camelMatch)