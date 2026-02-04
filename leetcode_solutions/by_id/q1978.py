# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1978
标题: Minimum Adjacent Swaps to Reach the Kth Smallest Number
难度: medium
链接: https://leetcode.cn/problems/minimum-adjacent-swaps-to-reach-the-kth-smallest-number/
题目类型: 贪心、双指针、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1850. 邻位交换的最小次数 - 给你一个表示大整数的字符串 num ，和一个整数 k 。 如果某个整数是 num 中各位数字的一个 排列 且它的 值大于 num ，则称这个整数为 妙数 。可能存在很多妙数，但是只需要关注 值最小 的那些。 * 例如，num = "5489355142" ： * 第 1 个最小妙数是 "5489355214" * 第 2 个最小妙数是 "5489355241" * 第 3 个最小妙数是 "5489355412" * 第 4 个最小妙数是 "5489355421" 返回要得到第 k 个 最小妙数 需要对 num 执行的 相邻位数字交换的最小次数 。 测试用例是按存在第 k 个最小妙数而生成的。 示例 1： 输入：num = "5489355142", k = 4 输出：2 解释：第 4 个最小妙数是 "5489355421" ，要想得到这个数字： - 交换下标 7 和下标 8 对应的位："5489355142" -> "5489355412" - 交换下标 8 和下标 9 对应的位："5489355412" -> "5489355421" 示例 2： 输入：num = "11112", k = 4 输出：4 解释：第 4 个最小妙数是 "21111" ，要想得到这个数字： - 交换下标 3 和下标 4 对应的位："11112" -> "11121" - 交换下标 2 和下标 3 对应的位："11121" -> "11211" - 交换下标 1 和下标 2 对应的位："11211" -> "12111" - 交换下标 0 和下标 1 对应的位："12111" -> "21111" 示例 3： 输入：num = "00123", k = 1 输出：1 解释：第 1 个最小妙数是 "00132" ，要想得到这个数字： - 交换下标 3 和下标 4 对应的位："00123" -> "00132" 提示： * 2 <= num.length <= 1000 * 1 <= k <= 1000 * num 仅由数字组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 next_permutation 算法找到第 k 个最小妙数，然后计算从原始 num 到目标 num 的最小交换次数。

算法步骤:
1. 使用 next_permutation 算法找到第 k 个最小妙数。
2. 计算从原始 num 到目标 num 的最小交换次数。

关键点:
- 使用 next_permutation 算法高效找到第 k 个最小妙数。
- 使用贪心算法计算最小交换次数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2) - next_permutation 算法的时间复杂度为 O(n)，最坏情况下需要调用 k 次，每次交换操作的时间复杂度为 O(n)。
空间复杂度: O(1) - 只使用常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def next_permutation(nums: List[int]) -> None:
    """修改 nums 为下一个排列"""
    n = len(nums)
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    if i >= 0:
        j = n - 1
        while j >= 0 and nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1:] = reversed(nums[i + 1:])


def min_swaps_to_reach_kth_smallest(num: str, k: int) -> int:
    """
    函数式接口 - 计算从原始 num 到第 k 个最小妙数的最小交换次数
    """
    nums = list(map(int, num))
    for _ in range(k):
        next_permutation(nums)
    
    target_num = ''.join(map(str, nums))
    swaps = 0
    num_list = list(num)
    
    for i in range(len(num)):
        if num_list[i] != target_num[i]:
            j = i + 1
            while num_list[j] != target_num[i]:
                j += 1
            while j > i:
                num_list[j], num_list[j - 1] = num_list[j - 1], num_list[j]
                swaps += 1
                j -= 1
    
    return swaps


Solution = create_solution(min_swaps_to_reach_kth_smallest)