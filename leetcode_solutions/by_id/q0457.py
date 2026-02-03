# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 457
标题: Circular Array Loop
难度: medium
链接: https://leetcode.cn/problems/circular-array-loop/
题目类型: 数组、哈希表、双指针
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
457. 环形数组是否存在循环 - 存在一个不含 0 的 环形 数组 nums ，每个 nums[i] 都表示位于下标 i 的角色应该向前或向后移动的下标个数： * 如果 nums[i] 是正数，向前（下标递增方向）移动 nums[i] 步 * 如果 nums[i] 是负数，向后（下标递减方向）移动 abs(nums[i]) 步 因为数组是 环形 的，所以可以假设从最后一个元素向前移动一步会到达第一个元素，而第一个元素向后移动一步会到达最后一个元素。 数组中的 循环 由长度为 k 的下标序列 seq 标识： * 遵循上述移动规则将导致一组重复下标序列 seq[0] -> seq[1] -> ... -> seq[k - 1] -> seq[0] -> ... * 所有 nums[seq[j]] 应当不是 全正 就是 全负 * k > 1 如果 nums 中存在循环，返回 true ；否则，返回 false 。 示例 1： [https://pic.leetcode.cn/1723688159-qYjpWT-image.png] 输入：nums = [2,-1,1,2,2] 输出：true 解释：图片展示了节点间如何连接。白色节点向前跳跃，而红色节点向后跳跃。 我们可以看到存在循环，按下标 0 -> 2 -> 3 -> 0 --> ...，并且其中的所有节点都是白色（以相同方向跳跃）。 示例 2： [https://pic.leetcode.cn/1723688183-lRSkjp-image.png] 输入：nums = [-1,-2,-3,-4,-5,6] 输出：false 解释：图片展示了节点间如何连接。白色节点向前跳跃，而红色节点向后跳跃。 唯一的循环长度为 1，所以返回 false。 示例 3： [https://pic.leetcode.cn/1723688199-nhaMuF-image.png] 输入：nums = [1,-1,5,1,4] 输出：true 解释：图片展示了节点间如何连接。白色节点向前跳跃，而红色节点向后跳跃。 我们可以看到存在循环，按下标 0 --> 1 --> 0 --> ...，当它的大小大于 1 时，它有一个向前跳的节点和一个向后跳的节点，所以 它不是一个循环。 我们可以看到存在循环，按下标 3 --> 4 --> 3 --> ...，并且其中的所有节点都是白色（以相同方向跳跃）。 提示： * 1 <= nums.length <= 5000 * -1000 <= nums[i] <= 1000 * nums[i] != 0 进阶：你能设计一个时间复杂度为 O(n) 且额外空间复杂度为 O(1) 的算法吗？
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 快慢指针检测循环，标记已访问节点

算法步骤:
1. 对每个未访问的节点，使用快慢指针检测循环
2. 检查循环长度是否大于1，且方向一致
3. 标记已访问的节点，避免重复检测

关键点:
- 快慢指针检测循环
- 检查方向一致性
- 标记已访问节点优化
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 每个节点最多访问一次
空间复杂度: O(1) - 只使用常数额外空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def circular_array_loop(nums: List[int]) -> bool:
    """
    函数式接口 - 环形数组是否存在循环
    
    实现思路:
    使用快慢指针检测循环，确保循环长度>1且方向一致。
    
    Args:
        nums: 环形数组
        
    Returns:
        是否存在符合条件的循环
        
    Example:
        >>> circular_array_loop([2,-1,1,2,2])
        True
    """
    n = len(nums)
    
    def get_next(i):
        """获取下一个位置"""
        return (i + nums[i]) % n
    
    def get_direction(i):
        """获取方向：正数返回True，负数返回False"""
        return nums[i] > 0
    
    for i in range(n):
        if nums[i] == 0:
            continue
        
        slow = fast = i
        direction = get_direction(i)
        
        # 快慢指针检测循环
        while True:
            slow = get_next(slow)
            if get_direction(slow) != direction:
                break
            
            fast = get_next(get_next(fast))
            if get_direction(fast) != direction:
                break
            
            if slow == fast:
                # 检查循环长度是否大于1
                next_slow = get_next(slow)
                if next_slow != slow:
                    return True
                break
        
        # 标记已访问的节点为0，避免重复检测
        cur = i
        while nums[cur] != 0 and get_direction(cur) == direction:
            next_cur = get_next(cur)
            nums[cur] = 0
            cur = next_cur
    
    return False


# 自动生成Solution类（无需手动编写）
Solution = create_solution(circular_array_loop)
