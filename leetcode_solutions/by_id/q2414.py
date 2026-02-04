# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2414
标题: Move Pieces to Obtain a String
难度: medium
链接: https://leetcode.cn/problems/move-pieces-to-obtain-a-string/
题目类型: 双指针、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2337. 移动片段得到字符串 - 给你两个字符串 start 和 target ，长度均为 n 。每个字符串 仅 由字符 'L'、'R' 和 '_' 组成，其中： * 字符 'L' 和 'R' 表示片段，其中片段 'L' 只有在其左侧直接存在一个 空位 时才能向 左 移动，而片段 'R' 只有在其右侧直接存在一个 空位 时才能向 右 移动。 * 字符 '_' 表示可以被 任意 'L' 或 'R' 片段占据的空位。 如果在移动字符串 start 中的片段任意次之后可以得到字符串 target ，返回 true ；否则，返回 false 。 示例 1： 输入：start = "_L__R__R_", target = "L______RR" 输出：true 解释：可以从字符串 start 获得 target ，需要进行下面的移动： - 将第一个片段向左移动一步，字符串现在变为 "L___R__R_" 。 - 将最后一个片段向右移动一步，字符串现在变为 "L___R___R" 。 - 将第二个片段向右移动三步，字符串现在变为 "L______RR" 。 可以从字符串 start 得到 target ，所以返回 true 。 示例 2： 输入：start = "R_L_", target = "__LR" 输出：false 解释：字符串 start 中的 'R' 片段可以向右移动一步得到 "_RL_" 。 但是，在这一步之后，不存在可以移动的片段，所以无法从字符串 start 得到 target 。 示例 3： 输入：start = "_R", target = "R_" 输出：false 解释：字符串 start 中的片段只能向右移动，所以无法从字符串 start 得到 target 。 提示： * n == start.length == target.length * 1 <= n <= 105 * start 和 target 由字符 'L'、'R' 和 '_' 组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用双指针分别遍历 start 和 target，确保所有 'L' 和 'R' 的相对顺序和位置正确。

算法步骤:
1. 初始化两个指针 i 和 j 分别指向 start 和 target 的起始位置。
2. 遍历 start 和 target，跳过所有的 '_'。
3. 检查当前字符是否匹配：
   - 如果不匹配，返回 False。
   - 如果 start 中的 'L' 在 target 中出现的位置在其右边，或者 start 中的 'R' 在 target 中出现的位置在其左边，返回 False。
4. 如果遍历完所有字符且没有冲突，返回 True。

关键点:
- 忽略 '_'，只关注 'L' 和 'R' 的相对位置。
- 'L' 只能向左移动，'R' 只能向右移动。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是字符串的长度。我们只需遍历一次字符串。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def can_transform(start: str, target: str) -> bool:
    """
    函数式接口 - 判断是否可以通过移动片段将 start 转换为 target
    """
    i, j = 0, 0
    n = len(start)
    
    while i < n or j < n:
        # 跳过 start 中的 '_'
        while i < n and start[i] == '_':
            i += 1
        # 跳过 target 中的 '_'
        while j < n and target[j] == '_':
            j += 1
        
        # 如果其中一个指针已经到达末尾，另一个未到达，返回 False
        if (i == n and j < n) or (j == n and i < n):
            return False
        
        # 检查当前字符是否匹配
        if start[i] != target[j]:
            return False
        
        # 检查 'L' 和 'R' 的相对位置
        if start[i] == 'L' and i < j:
            return False
        if start[i] == 'R' and i > j:
            return False
        
        i += 1
        j += 1
    
    return True


Solution = create_solution(can_transform)