# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2390
标题: Naming a Company
难度: hard
链接: https://leetcode.cn/problems/naming-a-company/
题目类型: 位运算、数组、哈希表、字符串、枚举
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2306. 公司命名 - 给你一个字符串数组 ideas 表示在公司命名过程中使用的名字列表。公司命名流程如下： 1. 从 ideas 中选择 2 个 不同 名字，称为 ideaA 和 ideaB 。 2. 交换 ideaA 和 ideaB 的首字母。 3. 如果得到的两个新名字 都 不在 ideas 中，那么 ideaA ideaB（串联 ideaA 和 ideaB ，中间用一个空格分隔）是一个有效的公司名字。 4. 否则，不是一个有效的名字。 返回 不同 且有效的公司名字的数目。 示例 1： 输入：ideas = ["coffee","donuts","time","toffee"] 输出：6 解释：下面列出一些有效的选择方案： - ("coffee", "donuts")：对应的公司名字是 "doffee conuts" 。 - ("donuts", "coffee")：对应的公司名字是 "conuts doffee" 。 - ("donuts", "time")：对应的公司名字是 "tonuts dime" 。 - ("donuts", "toffee")：对应的公司名字是 "tonuts doffee" 。 - ("time", "donuts")：对应的公司名字是 "dime tonuts" 。 - ("toffee", "donuts")：对应的公司名字是 "doffee tonuts" 。 因此，总共有 6 个不同的公司名字。 下面列出一些无效的选择方案： - ("coffee", "time")：在原数组中存在交换后形成的名字 "toffee" 。 - ("time", "toffee")：在原数组中存在交换后形成的两个名字。 - ("coffee", "toffee")：在原数组中存在交换后形成的两个名字。 示例 2： 输入：ideas = ["lack","back"] 输出：0 解释：不存在有效的选择方案。因此，返回 0 。 提示： * 2 <= ideas.length <= 5 * 104 * 1 <= ideas[i].length <= 10 * ideas[i] 由小写英文字母组成 * ideas 中的所有字符串 互不相同
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表和计数来统计每个首字母后的尾部字符串，并通过双重循环计算有效组合。

算法步骤:
1. 创建一个包含26个集合的列表，每个集合存储以某个字母开头的字符串的尾部。
2. 遍历ideas数组，将每个idea的尾部加入对应首字母的集合中。
3. 双重循环遍历所有可能的首字母对 (i, j)，计算它们之间的有效组合数量。
4. 累加所有有效组合的数量并返回结果。

关键点:
- 使用集合来存储每个首字母后的尾部字符串，以便快速查找。
- 通过双重循环计算每对首字母的有效组合数量，避免重复计算。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * 26^2) = O(n)，其中n是ideas的长度。
空间复杂度: O(n)，用于存储尾部字符串的集合。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def distinct_names(ideas: List[str]) -> int:
    """
    函数式接口 - 计算不同且有效的公司名字的数目
    """
    # 初始化一个包含26个集合的列表
    suffixes = [set() for _ in range(26)]
    
    # 将每个idea的尾部加入对应首字母的集合中
    for idea in ideas:
        suffixes[ord(idea[0]) - ord('a')].add(idea[1:])
    
    # 计算有效组合数量
    result = 0
    for i in range(26):
        for j in range(i + 1, 26):
            common = len(suffixes[i] & suffixes[j])
            result += 2 * (len(suffixes[i]) - common) * (len(suffixes[j]) - common)
    
    return result


Solution = create_solution(distinct_names)