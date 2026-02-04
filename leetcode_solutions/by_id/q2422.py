# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2422
标题: Query Kth Smallest Trimmed Number
难度: medium
链接: https://leetcode.cn/problems/query-kth-smallest-trimmed-number/
题目类型: 数组、字符串、分治、快速选择、基数排序、排序、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2343. 裁剪数字后查询第 K 小的数字 - 给你一个下标从 0 开始的字符串数组 nums ，其中每个字符串 长度相等 且只包含数字。 再给你一个下标从 0 开始的二维整数数组 queries ，其中 queries[i] = [ki, trimi] 。对于每个 queries[i] ，你需要： * 将 nums 中每个数字 裁剪 到剩下 最右边 trimi 个数位。 * 在裁剪过后的数字中，找到 nums 中第 ki 小数字对应的 下标 。如果两个裁剪后数字一样大，那么下标 更小 的数字视为更小的数字。 * 将 nums 中每个数字恢复到原本字符串。 请你返回一个长度与 queries 相等的数组 answer，其中 answer[i]是第 i 次查询的结果。 提示： * 裁剪到剩下最右边 x 个数位的意思是不断删除最左边的数位，直到剩下 x 个数位。 * nums 中的字符串可能会有前导 0 。 示例 1： 输入：nums = ["102","473","251","814"], queries = [[1,1],[2,3],[4,2],[1,2]] 输出：[2,2,1,0] 解释： 1. 裁剪到只剩 1 个数位后，nums = ["2","3","1","4"] 。最小的数字是 1 ，下标为 2 。 2. 裁剪到剩 3 个数位后，nums 没有变化。第 2 小的数字是 251 ，下标为 2 。 3. 裁剪到剩 2 个数位后，nums = ["02","73","51","14"] 。第 4 小的数字是 73 ，下标为 1 。 4. 裁剪到剩 2 个数位后，最小数字是 2 ，下标为 0 。 注意，裁剪后数字 "02" 值为 2 。 示例 2： 输入：nums = ["24","37","96","04"], queries = [[2,1],[2,2]] 输出：[3,0] 解释： 1. 裁剪到剩 1 个数位，nums = ["4","7","6","4"] 。第 2 小的数字是 4 ，下标为 3 。 有两个 4 ，下标为 0 的 4 视为小于下标为 3 的 4 。 2. 裁剪到剩 2 个数位，nums 不变。第二小的数字是 24 ，下标为 0 。 提示： * 1 <= nums.length <= 100 * 1 <= nums[i].length <= 100 * nums[i] 只包含数字。 * 所有 nums[i].length 的长度 相同 。 * 1 <= queries.length <= 100 * queries[i].length == 2 * 1 <= ki <= nums.length * 1 <= trimi <= nums[0].length 进阶：你能使用 基数排序算法 解决此问题吗？这种解法的复杂度又是多少？
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用基数排序对裁剪后的数字进行排序，然后找到第 k 小的数字。

算法步骤:
1. 对于每个查询，裁剪 nums 中的每个数字。
2. 使用基数排序对裁剪后的数字进行排序。
3. 找到第 k 小的数字并返回其下标。

关键点:
- 使用基数排序可以在 O(n) 时间内完成排序，其中 n 是 nums 的长度。
- 通过裁剪后的数字进行排序，可以确保找到第 k 小的数字。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m)，其中 n 是 nums 的长度，m 是每个数字的长度。
空间复杂度: O(n + m)，用于存储裁剪后的数字和基数排序的辅助数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def solution_function_name(nums: List[str], queries: List[List[int]]) -> List[int]:
    def radix_sort(arr, max_len):
        for exp in range(max_len - 1, -1, -1):
            count = [0] * 10
            output = [None] * len(arr)
            
            for num in arr:
                digit = int(num[exp])
                count[digit] += 1
            
            for i in range(1, 10):
                count[i] += count[i - 1]
            
            for i in range(len(arr) - 1, -1, -1):
                digit = int(arr[i][exp])
                output[count[digit] - 1] = arr[i]
                count[digit] -= 1
            
            arr[:] = output[:]
    
    def get_trimmed_nums(nums, trim):
        return [num[-trim:] for num in nums]
    
    def find_kth_smallest(trimmed_nums, k):
        radix_sort(trimmed_nums, len(trimmed_nums[0]))
        return trimmed_nums[k - 1]
    
    results = []
    for k, trim in queries:
        trimmed_nums = get_trimmed_nums(nums, trim)
        sorted_nums = sorted(enumerate(trimmed_nums), key=lambda x: (x[1], x[0]))
        results.append(sorted_nums[k - 1][0])
    
    return results

Solution = create_solution(solution_function_name)