# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1312
标题: Count Artifacts That Can Be Extracted
难度: medium
链接: https://leetcode.cn/problems/count-artifacts-that-can-be-extracted/
题目类型: 数组、哈希表、模拟
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2201. 统计可以提取的工件 - 存在一个 n x n 大小、下标从 0 开始的网格，网格中埋着一些工件。给你一个整数 n 和一个下标从 0 开始的二维整数数组 artifacts ，artifacts 描述了矩形工件的位置，其中 artifacts[i] = [r1i, c1i, r2i, c2i] 表示第 i 个工件在子网格中的填埋情况： * (r1i, c1i) 是第 i 个工件 左上 单元格的坐标，且 * (r2i, c2i) 是第 i 个工件 右下 单元格的坐标。 你将会挖掘网格中的一些单元格，并清除其中的填埋物。如果单元格中埋着工件的一部分，那么该工件这一部分将会裸露出来。如果一个工件的所有部分都都裸露出来，你就可以提取该工件。 给你一个下标从 0 开始的二维整数数组 dig ，其中 dig[i] = [ri, ci] 表示你将会挖掘单元格 (ri, ci) ，返回你可以提取的工件数目。 生成的测试用例满足： * 不存在重叠的两个工件。 * 每个工件最多只覆盖 4 个单元格。 * dig 中的元素互不相同。 示例 1： [https://assets.leetcode.com/uploads/2019/09/16/untitled-diagram.jpg] 输入：n = 2, artifacts = [[0,0,0,0],[0,1,1,1]], dig = [[0,0],[0,1]] 输出：1 解释： 不同颜色表示不同的工件。挖掘的单元格用 'D' 在网格中进行标记。 有 1 个工件可以提取，即红色工件。 蓝色工件在单元格 (1,1) 的部分尚未裸露出来，所以无法提取该工件。 因此，返回 1 。 示例 2： [https://assets.leetcode.com/uploads/2019/09/16/untitled-diagram-1.jpg] 输入：n = 2, artifacts = [[0,0,0,0],[0,1,1,1]], dig = [[0,0],[0,1],[1,1]] 输出：2 解释：红色工件和蓝色工件的所有部分都裸露出来（用 'D' 标记），都可以提取。因此，返回 2 。 提示： * 1 <= n <= 1000 * 1 <= artifacts.length, dig.length <= min(n2, 105) * artifacts[i].length == 4 * dig[i].length == 2 * 0 <= r1i, c1i, r2i, c2i, ri, ci <= n - 1 * r1i <= r2i * c1i <= c2i * 不存在重叠的两个工件 * 每个工件 最多 只覆盖 4 个单元格 * dig 中的元素互不相同
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用集合来存储已挖掘的单元格，并检查每个工件的所有部分是否都在已挖掘的单元格中。

算法步骤:
1. 将所有已挖掘的单元格存入集合 `dug`。
2. 遍历每个工件，检查其所有部分是否都在 `dug` 集合中。
3. 如果某个工件的所有部分都在 `dug` 集合中，则将其计入可提取的工件数量。

关键点:
- 使用集合来高效地检查单元格是否已被挖掘。
- 遍历每个工件的所有部分，确保所有部分都被挖掘。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(A + D)，其中 A 是 artifacts 的长度，D 是 dig 的长度。我们需要遍历 dig 来构建集合，然后遍历 artifacts 来检查每个工件。
空间复杂度: O(D)，用于存储已挖掘的单元格集合。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def count_artifacts(n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
    """
    函数式接口 - 统计可以提取的工件
    """
    # 将所有已挖掘的单元格存入集合
    dug = set(tuple(cell) for cell in dig)
    
    # 计算可以提取的工件数量
    extractable_count = 0
    
    for artifact in artifacts:
        r1, c1, r2, c2 = artifact
        all_parts_dug = True
        
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                if (r, c) not in dug:
                    all_parts_dug = False
                    break
            if not all_parts_dug:
                break
        
        if all_parts_dug:
            extractable_count += 1
    
    return extractable_count


Solution = create_solution(count_artifacts)