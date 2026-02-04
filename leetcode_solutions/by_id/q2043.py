# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2043
标题: Cyclically Rotating a Grid
难度: medium
链接: https://leetcode.cn/problems/cyclically-rotating-a-grid/
题目类型: 数组、矩阵、模拟
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1914. 循环轮转矩阵 - 给你一个大小为 m x n 的整数矩阵 grid ，其中 m 和 n 都是 偶数 ；另给你一个整数 k 。 矩阵由若干层组成，如下图所示，每种颜色代表一层： [https://assets.leetcode.com/uploads/2021/06/10/ringofgrid.png] 矩阵的循环轮转是通过分别循环轮转矩阵中的每一层完成的。在对某一层进行一次循环旋转操作时，层中的每一个元素将会取代其 逆时针 方向的相邻元素。轮转示例如下： [https://assets.leetcode.com/uploads/2021/06/22/explanation_grid.jpg] 返回执行 k 次循环轮转操作后的矩阵。 示例 1： [https://assets.leetcode.com/uploads/2021/06/19/rod2.png] 输入：grid = [[40,10],[30,20]], k = 1 输出：[[10,20],[40,30]] 解释：上图展示了矩阵在执行循环轮转操作时每一步的状态。 示例 2： [https://assets.leetcode.com/uploads/2021/06/10/ringofgrid5.png] [https://assets.leetcode.com/uploads/2021/06/10/ringofgrid6.png] [https://assets.leetcode.com/uploads/2021/06/10/ringofgrid7.png] 输入：grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], k = 2 输出：[[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]] 解释：上图展示了矩阵在执行循环轮转操作时每一步的状态。 提示： * m == grid.length * n == grid[i].length * 2 <= m, n <= 50 * m 和 n 都是 偶数 * 1 <= grid[i][j] <= 5000 * 1 <= k <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 对每一层进行逆时针旋转，利用取模运算来简化多次旋转的操作。

算法步骤:
1. 确定矩阵的层数。
2. 对每一层进行逆时针旋转 k 次。
3. 将旋转后的值重新放回原矩阵中。

关键点:
- 通过取模运算简化多次旋转的操作。
- 逐层处理矩阵，确保每一层的旋转独立进行。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n)，其中 m 和 n 分别是矩阵的行数和列数。每个元素最多被访问和移动一次。
空间复杂度: O(1)，除了输入和输出外，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def rotate_layer(layer: List[int], k: int) -> List[int]:
    """
    逆时针旋转一层 k 次
    """
    n = len(layer)
    k = k % n  # 取模以简化多次旋转
    return layer[k:] + layer[:k]

def get_layer(grid: List[List[int]], layer: int) -> List[int]:
    """
    获取第 layer 层的所有元素
    """
    top = grid[layer][layer:-layer]
    right = [grid[i][-layer-1] for i in range(layer, len(grid)-layer)]
    bottom = grid[-layer-1][layer:-layer][::-1]
    left = [grid[i][layer] for i in range(len(grid)-layer-1, layer, -1)]
    return top + right[1:] + bottom + left[1:]

def set_layer(grid: List[List[int]], layer: int, new_layer: List[int]):
    """
    将新一层的元素放回原矩阵
    """
    n = len(new_layer)
    top = new_layer[:len(grid[layer])-2*layer]
    right = new_layer[len(top):len(top)+len(grid)-2*(layer+1)]
    bottom = new_layer[len(top)+len(right):len(top)+len(right)+len(grid)-2*(layer+1)][::-1]
    left = new_layer[len(top)+len(right)+len(bottom):]

    for j in range(layer, len(grid[layer])-layer):
        grid[layer][j] = top[j-layer]
    for i in range(layer+1, len(grid)-layer):
        grid[i][-layer-1] = right[i-(layer+1)]
    for j in range(len(grid[layer])-layer-2, layer-1, -1):
        grid[-layer-1][j] = bottom[len(grid[layer])-layer-2-j]
    for i in range(len(grid)-layer-2, layer, -1):
        grid[i][layer] = left[len(grid)-layer-2-i]

def solution_function_name(grid: List[List[int]], k: int) -> List[List[int]]:
    """
    函数式接口 - 实现最优解法
    """
    m, n = len(grid), len(grid[0])
    layers = min(m, n) // 2
    
    for layer in range(layers):
        current_layer = get_layer(grid, layer)
        rotated_layer = rotate_layer(current_layer, k)
        set_layer(grid, layer, rotated_layer)
    
    return grid

Solution = create_solution(solution_function_name)