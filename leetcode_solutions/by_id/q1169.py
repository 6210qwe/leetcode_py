# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1169
标题: Largest Values From Labels
难度: medium
链接: https://leetcode.cn/problems/largest-values-from-labels/
题目类型: 贪心、数组、哈希表、计数、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1090. 受标签影响的最大值 - 以两个整数数组 values 和 labels 给定 n 个项的值和标签，并且给出两个整数 numWanted 和 useLimit 。 你的任务是从这些项中找到一个值的和 最大 的子集使得： * 项的数量 最多 为 numWanted。 * 相同标签的项的数量 最多 为 useLimit。 返回最大的和。 示例 1： 输入：values = [5,4,3,2,1], labels = [1,1,2,2,3], numWanted = 3, useLimit = 1 输出：9 解释： 选择的子集是第一个、第三个和第五个项，其值之和为 5 + 3 + 1。 示例 2： 输入：values = [5,4,3,2,1], labels = [1,3,3,3,2], numWanted = 3, useLimit = 2 输出：12 解释： 选择的子集是第一个、第二个和第三个项，其值之和为 5 + 4 + 3。 示例 3： 输入：values = [9,8,8,7,6], labels = [0,0,0,1,1], numWanted = 3, useLimit = 1 输出：16 解释： 选择的子集是第一个和第四个项，其值之和为 9 + 7。 提示： * n == values.length == labels.length * 1 <= n <= 2 * 104 * 0 <= values[i], labels[i] <= 2 * 104 * 1 <= numWanted, useLimit <= n
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法，优先选择值最大的项，同时保证每个标签的使用次数不超过 useLimit。

算法步骤:
1. 将 values 和 labels 结合成一个列表，每个元素是一个 (value, label) 对。
2. 按照 value 从大到小对这个列表进行排序。
3. 使用一个字典来记录每个标签已经使用的次数。
4. 遍历排序后的列表，选择符合条件的项，直到选满 numWanted 个项或遍历完所有项。
5. 计算并返回所选项的值的总和。

关键点:
- 优先选择值最大的项，确保总和最大。
- 使用字典记录每个标签的使用次数，确保不超过 useLimit。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是 values 和 labels 的长度。排序操作的时间复杂度为 O(n log n)，遍历操作的时间复杂度为 O(n)。
空间复杂度: O(n)，需要额外的空间存储结合后的列表和标签使用次数的字典。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def largestValsFromLabels(values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
    """
    函数式接口 - 实现最优解法
    """
    # 将 values 和 labels 结合成一个列表
    items = list(zip(values, labels))
    
    # 按照 value 从大到小对这个列表进行排序
    items.sort(key=lambda x: -x[0])
    
    # 使用一个字典来记录每个标签已经使用的次数
    label_count = {}
    
    # 初始化结果变量
    result = 0
    selected_count = 0
    
    # 遍历排序后的列表
    for value, label in items:
        if selected_count >= numWanted:
            break
        
        # 检查当前标签是否超过 useLimit
        if label_count.get(label, 0) < useLimit:
            result += value
            label_count[label] = label_count.get(label, 0) + 1
            selected_count += 1
    
    return result

Solution = create_solution(largestValsFromLabels)