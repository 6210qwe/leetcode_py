# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2502
标题: Sort the People
难度: easy
链接: https://leetcode.cn/problems/sort-the-people/
题目类型: 数组、哈希表、字符串、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2418. 按身高排序 - 给你一个字符串数组 names ，和一个由 互不相同 的正整数组成的数组 heights 。两个数组的长度均为 n 。 对于每个下标 i，names[i] 和 heights[i] 表示第 i 个人的名字和身高。 请按身高 降序 顺序返回对应的名字数组 names 。 示例 1： 输入：names = ["Mary","John","Emma"], heights = [180,165,170] 输出：["Mary","Emma","John"] 解释：Mary 最高，接着是 Emma 和 John 。 示例 2： 输入：names = ["Alice","Bob","Bob"], heights = [155,185,150] 输出：["Bob","Alice","Bob"] 解释：第一个 Bob 最高，然后是 Alice 和第二个 Bob 。 提示： * n == names.length == heights.length * 1 <= n <= 103 * 1 <= names[i].length <= 20 * 1 <= heights[i] <= 105 * names[i] 由大小写英文字母组成 * heights 中的所有值互不相同
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用字典将名字和身高关联起来，然后根据身高对名字进行排序。

算法步骤:
1. 创建一个字典，将每个名字与其对应的身高关联起来。
2. 根据身高的降序对字典进行排序。
3. 提取排序后的名字列表。

关键点:
- 使用字典来存储名字和身高的对应关系。
- 使用 Python 的 sorted 函数进行排序。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n) - 排序操作的时间复杂度。
空间复杂度: O(n) - 存储字典的空间复杂度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def sort_people(names: List[str], heights: List[int]) -> List[str]:
    """
    函数式接口 - 按身高降序排序名字
    """
    # 创建一个字典，将每个名字与其对应的身高关联起来
    name_height_map = {heights[i]: names[i] for i in range(len(names))}
    
    # 根据身高的降序对字典进行排序
    sorted_names = [name_height_map[height] for height in sorted(name_height_map.keys(), reverse=True)]
    
    return sorted_names


Solution = create_solution(sort_people)