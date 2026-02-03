# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 373
标题: Find K Pairs with Smallest Sums
难度: medium
链接: https://leetcode.cn/problems/find-k-pairs-with-smallest-sums/
题目类型: 数组、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
373. 查找和最小的 K 对数字 - 给定两个以 非递减顺序排列 的整数数组 nums1 和 nums2 , 以及一个整数 k 。 定义一对值 (u,v)，其中第一个元素来自 nums1，第二个元素来自 nums2 。 请找到和最小的 k 个数对 (u1,v1), (u2,v2) ... (uk,vk) 。 示例 1: 输入: nums1 = [1,7,11], nums2 = [2,4,6], k = 3 输出: [[1,2],[1,4],[1,6]] 解释: 返回序列中的前 3 对数： [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6] 示例 2: 输入: nums1 = [1,1,2], nums2 = [1,2,3], k = 2 输出: [[1,1],[1,1]] 解释: 返回序列中的前 2 对数： [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3] 提示: * 1 <= nums1.length, nums2.length <= 105 * -109 <= nums1[i], nums2[i] <= 109 * nums1 和 nums2 均为 升序排列 * 1 <= k <= 104 * k <= nums1.length * nums2.length
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 两个有序数组的「按和排序的笛卡尔积」前 k 小，用最小堆进行多路归并，只扩展必要的状态

算法步骤:
1. 由于 nums1、nums2 均为非递减序列，固定 nums1[i] 后，与 nums2 所有元素配对得到的一列和是递增的。
2. 初始时，将 (nums1[0] + nums2[0], i=0, j=0) 压入最小堆，表示当前最小的一对。
3. 每次从堆中弹出当前最小和对应的下标 (i, j)，将 (nums1[i], nums2[j]) 计入答案。
4. 为避免重复并做到「按列扩展」：
   - 若 j+1 仍在范围内，则把 (nums1[i] + nums2[j+1], i, j+1) 加入堆。
   - 若 j == 0 且 i+1 在范围内，则把 (nums1[i+1] + nums2[0], i+1, 0) 加入堆，确保每行只在 j=0 时被引入一次。
5. 重复弹出和扩展过程，直到取满 k 个数对或堆为空。

关键点:
- 利用两数组递增性质，将所有可能对 (i, j) 看成按行、按列有序的「矩阵」，用堆做类似 Dijkstra 的扩展。
- 用「只在 j=0 时引入新行」的技巧，避免对同一对 (i, j) 重复入堆。
- 注意 k 可能大于两数组乘积，实际返回的对数不超过 len(nums1) * len(nums2)。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(k log k) - 最多弹出 k 次，每次堆操作为 O(log k) 级别。
空间复杂度: O(k) - 堆中至多维护与已弹出元素数量同阶的状态。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
import heapq
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def find_k_pairs_with_smallest_sums(nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    """
    给定两个有序数组，返回和最小的 k 对数对。

    使用最小堆按行、按列扩展 (i, j) 对，只访问必要的前 k 个状态。
    """
    res: List[List[int]] = []
    if not nums1 or not nums2 or k <= 0:
        return res

    n1, n2 = len(nums1), len(nums2)
    k = min(k, n1 * n2)

    heap: list[tuple[int, int, int]] = []  # (sum, i, j)
    # 初始化第一列
    for i in range(min(n1, k)):
        heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

    while heap and len(res) < k:
        _, i, j = heapq.heappop(heap)
        res.append([nums1[i], nums2[j]])
        if j + 1 < n2:
            heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))

    return res


# 自动生成Solution类（无需手动编写）
Solution = create_solution(find_k_pairs_with_smallest_sums)
