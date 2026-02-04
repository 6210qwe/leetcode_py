# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1397
标题: Search Suggestions System
难度: medium
链接: https://leetcode.cn/problems/search-suggestions-system/
题目类型: 字典树、数组、字符串、二分查找、排序、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1268. 搜索推荐系统 - 给你一个产品数组 products 和一个字符串 searchWord ，products 数组中每个产品都是一个字符串。 请你设计一个推荐系统，在依次输入单词 searchWord 的每一个字母后，推荐 products 数组中前缀与 searchWord 相同的最多三个产品。如果前缀相同的可推荐产品超过三个，请按字典序返回最小的三个。 请你以二维列表的形式，返回在输入 searchWord 每个字母后相应的推荐产品的列表。 示例 1： 输入：products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse" 输出：[ ["mobile","moneypot","monitor"], ["mobile","moneypot","monitor"], ["mouse","mousepad"], ["mouse","mousepad"], ["mouse","mousepad"] ] 解释：按字典序排序后的产品列表是 ["mobile","moneypot","monitor","mouse","mousepad"] 输入 m 和 mo，由于所有产品的前缀都相同，所以系统返回字典序最小的三个产品 ["mobile","moneypot","monitor"] 输入 mou， mous 和 mouse 后系统都返回 ["mouse","mousepad"] 示例 2： 输入：products = ["havana"], searchWord = "havana" 输出：[["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]] 示例 3： 输入：products = ["bags","baggage","banner","box","cloths"], searchWord = "bags" 输出：[["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]] 示例 4： 输入：products = ["havana"], searchWord = "tatiana" 输出：[[],[],[],[],[],[],[]] 提示： * 1 <= products.length <= 1000 * 1 <= Σ products[i].length <= 2 * 10^4 * products[i] 中所有的字符都是小写英文字母。 * 1 <= searchWord.length <= 1000 * searchWord 中所有字符都是小写英文字母。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用排序和二分查找来高效地找到前缀匹配的产品。

算法步骤:
1. 对产品列表进行排序。
2. 对于 searchWord 的每个前缀，使用二分查找找到第一个匹配的索引。
3. 从该索引开始，收集最多三个前缀匹配的产品。

关键点:
- 排序后的列表可以利用二分查找快速定位前缀匹配的起始位置。
- 收集结果时，只需遍历最多三个产品。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n + m * log n)，其中 n 是 products 的长度，m 是 searchWord 的长度。排序的时间复杂度是 O(n log n)，每次二分查找的时间复杂度是 O(log n)，总共进行 m 次二分查找。
空间复杂度: O(1)，除了输入和输出外，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def suggested_products(products: List[str], search_word: str) -> List[List[str]]:
    """
    函数式接口 - 实现搜索建议系统
    """
    # 对产品列表进行排序
    products.sort()

    def binary_search(left: int, right: int, prefix: str) -> int:
        while left < right:
            mid = (left + right) // 2
            if products[mid] < prefix:
                left = mid + 1
            else:
                right = mid
        return left

    result = []
    prefix = ""
    left = 0
    for char in search_word:
        prefix += char
        left = binary_search(left, len(products), prefix)
        suggestions = []
        for i in range(left, min(left + 3, len(products))):
            if products[i].startswith(prefix):
                suggestions.append(products[i])
        result.append(suggestions)

    return result


Solution = create_solution(suggested_products)