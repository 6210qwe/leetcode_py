# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 757
标题: Pyramid Transition Matrix
难度: medium
链接: https://leetcode.cn/problems/pyramid-transition-matrix/
题目类型: 位运算、哈希表、字符串、回溯
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
756. 金字塔转换矩阵 - 你正在把积木堆成金字塔。每个块都有一个颜色，用一个字母表示。每一行的块比它下面的行 少一个块 ，并且居中。 为了使金字塔美观，只有特定的 三角形图案 是允许的。一个三角形的图案由 两个块 和叠在上面的 单个块 组成。模式是以三个字母字符串的列表形式 allowed 给出的，其中模式的前两个字符分别表示左右底部块，第三个字符表示顶部块。 * 例如，"ABC" 表示一个三角形图案，其中一个 “C” 块堆叠在一个 'A' 块(左)和一个 'B' 块(右)之上。请注意，这与 "BAC" 不同，"B" 在左下角，"A" 在右下角。 你从作为单个字符串给出的底部的一排积木 bottom 开始，必须 将其作为金字塔的底部。 在给定 bottom 和 allowed 的情况下，如果你能一直构建到金字塔顶部，使金字塔中的 每个三角形图案 都是在 allowed 中的，则返回 true ，否则返回 false 。 示例 1： [https://assets.leetcode.com/uploads/2021/08/26/pyramid1-grid.jpg] 输入：bottom = "BCD", allowed = ["BCC","CDE","CEA","FFF"] 输出：true 解释：允许的三角形图案显示在右边。 从最底层(第 3 层)开始，我们可以在第 2 层构建“CE”，然后在第 1 层构建“A”。 金字塔中有三种三角形图案，分别是 “BCC”、“CDE” 和 “CEA”。都是允许的。 示例 2： [https://assets.leetcode.com/uploads/2021/08/26/pyramid2-grid.jpg] 输入：bottom = "AAAA", allowed = ["AAB","AAC","BCD","BBE","DEF"] 输出：false 解释：允许的三角形图案显示在右边。 从最底层(即第 4 层)开始，创造第 3 层有多种方法，但如果尝试所有可能性，你便会在创造第 1 层前陷入困境。 提示： * 2 <= bottom.length <= 6 * 0 <= allowed.length <= 216 * allowed[i].length == 3 * 所有输入字符串中的字母来自集合 {'A', 'B', 'C', 'D', 'E', 'F'}。 * allowed 中所有值都是 唯一的
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用回溯法来构建金字塔，通过递归尝试每一种可能的上层组合。

算法步骤:
1. 构建一个字典，将 allowed 中的每一个三元组映射到一个字典中，方便快速查找。
2. 定义一个递归函数，用于构建金字塔的每一层。
3. 从底部开始，逐层向上构建，直到构建到顶层。
4. 在每一步中，检查当前层的所有可能的上一层组合，如果可以构建成功，则继续递归构建上一层。
5. 如果构建到顶层，则返回 True；否则，返回 False。

关键点:
- 使用字典来存储 allowed 三元组，以实现快速查找。
- 使用递归和回溯来尝试所有可能的上层组合。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(2^n)，其中 n 是 bottom 的长度。因为每一步都有最多 2 种选择。
空间复杂度: O(n^2)，递归调用栈的深度为 n，每一层的组合数最多为 n。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional

def pyramid_transition(bottom: str, allowed: List[str]) -> bool:
    # 构建字典，将 allowed 中的每一个三元组映射到一个字典中
    mapping = {}
    for a, b, c in allowed:
        if (a, b) not in mapping:
            mapping[(a, b)] = []
        mapping[(a, b)].append(c)

    def can_build(current: str, next_layer: List[str], index: int) -> bool:
        # 如果当前层构建完成，检查是否可以继续构建
        if len(current) == 1:
            return True
        # 如果当前层还没有构建完成
        if index == len(current) - 1:
            return can_build(''.join(next_layer), [], 0)
        # 获取当前两个块可以放置的上层块
        key = (current[index], current[index + 1])
        if key not in mapping:
            return False
        for block in mapping[key]:
            next_layer.append(block)
            if can_build(current, next_layer, index + 1):
                return True
            next_layer.pop()
        return False

    return can_build(bottom, [], 0)

Solution = create_solution(pyramid_transition)