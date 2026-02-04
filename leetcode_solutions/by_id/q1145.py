# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1145
标题: Number of Submatrices That Sum to Target
难度: hard
链接: https://leetcode.cn/problems/number-of-submatrices-that-sum-to-target/
题目类型: 数组、哈希表、矩阵、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1074. 元素和为目标值的子矩阵数量 - 给出矩阵 matrix 和目标值 target，返回元素总和等于目标值的非空子矩阵的数量。 子矩阵 x1, y1, x2, y2 是满足 x1 <= x <= x2 且 y1 <= y <= y2 的所有单元 matrix[x][y] 的集合。 如果 (x1, y1, x2, y2) 和 (x1', y1', x2', y2') 两个子矩阵中部分坐标不同（如：x1 != x1'），那么这两个子矩阵也不同。 示例 1： [https://assets.leetcode.com/uploads/2020/09/02/mate1.jpg] 输入：matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0 输出：4 解释：四个只含 0 的 1x1 子矩阵。 示例 2： 输入：matrix = [[1,-1],[-1,1]], target = 0 输出：5 解释：两个 1x2 子矩阵，加上两个 2x1 子矩阵，再加上一个 2x2 子矩阵。 示例 3： 输入：matrix = [[904]], target = 0 输出：0 提示： * 1 <= matrix.length <= 100 * 1 <= matrix[0].length <= 100 * -1000 <= matrix[i][j] <= 1000 * -10^8 <= target <= 10^8
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用前缀和与哈希表来优化计算子矩阵的和。

算法步骤:
1. 对于每一行，计算从该行开始的所有行的前缀和。
2. 对于每一列，使用哈希表记录前缀和出现的次数，并计算当前列的前缀和。
3. 通过哈希表查找是否存在某个前缀和，使得当前前缀和减去该前缀和等于目标值。

关键点:
- 使用前缀和可以快速计算任意子矩阵的和。
- 使用哈希表记录前缀和出现的次数，可以在 O(1) 时间内查找是否存在某个前缀和。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n^2)，其中 m 是矩阵的行数，n 是矩阵的列数。
空间复杂度: O(n)，用于存储每一列的前缀和。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def numSubmatrixSumTarget(matrix: List[List[int]], target: int) -> int:
    def count_subarrays(nums: List[int], target: int) -> int:
        count, cur_sum = 0, 0
        prefix_sums = {0: 1}
        
        for num in nums:
            cur_sum += num
            if cur_sum - target in prefix_sums:
                count += prefix_sums[cur_sum - target]
            prefix_sums[cur_sum] = prefix_sums.get(cur_sum, 0) + 1
        
        return count
    
    m, n = len(matrix), len(matrix[0])
    result = 0
    
    for top in range(m):
        row_sums = [0] * n
        for bottom in range(top, m):
            for col in range(n):
                row_sums[col] += matrix[bottom][col]
            result += count_subarrays(row_sums, target)
    
    return result

Solution = create_solution(numSubmatrixSumTarget)