# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1017
标题: Odd Even Jump
难度: hard
链接: https://leetcode.cn/problems/odd-even-jump/
题目类型: 栈、数组、动态规划、有序集合、排序、单调栈
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
975. 奇偶跳 - 给定一个整数数组 arr，你可以从某一起始索引出发，跳跃一定次数。在你跳跃的过程中，第 1、3、5... 次跳跃称为奇数跳跃，而第 2、4、6... 次跳跃称为偶数跳跃。 你可以按以下方式从索引 i 向后跳转到索引 j（其中 i < j）： * 在进行奇数跳跃时（如，第 1，3，5... 次跳跃），你将会跳到索引 j，使得 arr[i] <= arr[j]，且 arr[j] 的值尽可能小。如果存在多个这样的索引 j，你只能跳到满足要求的最小索引 j 上。 * 在进行偶数跳跃时（如，第 2，4，6... 次跳跃），你将会跳到索引 j，使得 arr[i] >= arr[j]，且 arr[j] 的值尽可能大。如果存在多个这样的索引 j，你只能跳到满足要求的最小索引 j 上。 * （对于某些索引 i，可能无法进行合乎要求的跳跃。） 如果从某一索引开始跳跃一定次数（可能是 0 次或多次），就可以到达数组的末尾（索引 arr.length - 1），那么该索引就会被认为是好的起始索引。 返回好的起始索引的数量。 示例 1： 输入：[10,13,12,14,15] 输出：2 解释： 从起始索引 i = 0 出发，我们可以跳到 i = 2，（因为 arr[2] 是 arr[1]，arr[2]，arr[3]，arr[4] 中大于或等于 arr[0] 的最小值），然后我们就无法继续跳下去了。 从起始索引 i = 1 和 i = 2 出发，我们可以跳到 i = 3，然后我们就无法继续跳下去了。 从起始索引 i = 3 出发，我们可以跳到 i = 4，到达数组末尾。 从起始索引 i = 4 出发，我们已经到达数组末尾。 总之，我们可以从 2 个不同的起始索引（i = 3, i = 4）出发，通过一定数量的跳跃到达数组末尾。 示例 2： 输入：[2,3,1,1,4] 输出：3 解释： 从起始索引 i=0 出发，我们依次可以跳到 i = 1，i = 2，i = 3： 在我们的第一次跳跃（奇数）中，我们先跳到 i = 1，因为 arr[1] 是（arr[1]，arr[2]，arr[3]，arr[4]）中大于或等于 arr[0] 的最小值。 在我们的第二次跳跃（偶数）中，我们从 i = 1 跳到 i = 2，因为 arr[2] 是（arr[2]，arr[3]，arr[4]）中小于或等于 arr[1] 的最大值。arr[3] 也是最大的值，但 2 是一个较小的索引，所以我们只能跳到 i = 2，而不能跳到 i = 3。 在我们的第三次跳跃（奇数）中，我们从 i = 2 跳到 i = 3，因为 arr[3] 是（arr[3]，arr[4]）中大于或等于 arr[2] 的最小值。 我们不能从 i = 3 跳到 i = 4，所以起始索引 i = 0 不是好的起始索引。 类似地，我们可以推断： 从起始索引 i = 1 出发， 我们跳到 i = 4，这样我们就到达数组末尾。 从起始索引 i = 2 出发， 我们跳到 i = 3，然后我们就不能再跳了。 从起始索引 i = 3 出发， 我们跳到 i = 4，这样我们就到达数组末尾。 从起始索引 i = 4 出发，我们已经到达数组末尾。 总之，我们可以从 3 个不同的起始索引（i = 1, i = 3, i = 4）出发，通过一定数量的跳跃到达数组末尾。 示例 3： 输入：[5,1,3,4,2] 输出：3 解释： 我们可以从起始索引 1，2，4 出发到达数组末尾。 提示： 1. 1 <= arr.length <= 20000 2. 0 <= arr[i] < 100000
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划和单调栈来解决这个问题。

算法步骤:
1. 使用一个有序映射 (OrderedDict) 来存储每个元素的索引。
2. 对于每个元素，找到其奇数跳跃和偶数跳跃的目标索引。
3. 使用动态规划数组 dp 来记录从每个索引出发是否可以到达数组末尾。
4. 从数组末尾向前遍历，更新 dp 数组。
5. 最后统计 dp 数组中可以从奇数跳跃到达末尾的索引数量。

关键点:
- 使用有序映射来高效找到奇数跳跃和偶数跳跃的目标索引。
- 动态规划数组 dp 用于记录从每个索引出发是否可以到达数组末尾。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是数组的长度。排序操作的时间复杂度为 O(n log n)，后续的遍历操作为 O(n)。
空间复杂度: O(n)，需要额外的空间来存储有序映射和动态规划数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution
import bisect


def odd_even_jumps(arr: List[int]) -> int:
    n = len(arr)
    if n == 1:
        return 1

    # 用于存储每个元素的索引
    index_map = {}
    for i, num in enumerate(arr):
        if num not in index_map:
            index_map[num] = []
        index_map[num].append(i)

    # 用于存储奇数跳跃和偶数跳跃的目标索引
    odd_next = [None] * n
    even_next = [None] * n

    # 用于存储当前处理的元素
    sorted_nums = sorted(index_map.keys())

    # 用于存储当前处理的元素的索引
    index_stack = []

    # 找到奇数跳跃的目标索引
    for num in sorted_nums:
        indices = index_map[num]
        for index in indices:
            pos = bisect.bisect_left(index_stack, index)
            if pos < len(index_stack):
                odd_next[index] = index_stack[pos]
        index_stack.extend(indices)

    # 清空索引栈
    index_stack.clear()

    # 找到偶数跳跃的目标索引
    for num in reversed(sorted_nums):
        indices = index_map[num]
        for index in indices:
            pos = bisect.bisect_left(index_stack, index)
            if pos < len(index_stack):
                even_next[index] = index_stack[pos]
        index_stack.extend(indices)

    # 动态规划数组
    dp_odd = [False] * n
    dp_even = [False] * n
    dp_odd[-1] = True
    dp_even[-1] = True

    # 从数组末尾向前遍历
    for i in range(n - 2, -1, -1):
        if odd_next[i] is not None:
            dp_odd[i] = dp_even[odd_next[i]]
        if even_next[i] is not None:
            dp_even[i] = dp_odd[even_next[i]]

    # 统计可以从奇数跳跃到达末尾的索引数量
    return sum(dp_odd)


Solution = create_solution(odd_even_jumps)