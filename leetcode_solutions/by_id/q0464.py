# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 464
标题: Can I Win
难度: medium
链接: https://leetcode.cn/problems/can-i-win/
题目类型: 位运算、记忆化搜索、数学、动态规划、状态压缩、博弈
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
464. 我能赢吗 - 在 "100 game" 这个游戏中，两名玩家轮流选择从 1 到 10 的任意整数，累计整数和，先使得累计整数和 达到或超过 100 的玩家，即为胜者。 如果我们将游戏规则改为 “玩家 不能 重复使用整数” 呢？ 例如，两个玩家可以轮流从公共整数池中抽取从 1 到 15 的整数（不放回），直到累计整数和 >= 100。 给定两个整数 maxChoosableInteger （整数池中可选择的最大数）和 desiredTotal（累计和），若先出手的玩家能稳赢则返回 true ，否则返回 false 。假设两位玩家游戏时都表现 最佳 。 示例 1： 输入：maxChoosableInteger = 10, desiredTotal = 11 输出：false 解释： 无论第一个玩家选择哪个整数，他都会失败。 第一个玩家可以选择从 1 到 10 的整数。 如果第一个玩家选择 1，那么第二个玩家只能选择从 2 到 10 的整数。 第二个玩家可以通过选择整数 10（那么累积和为 11 >= desiredTotal），从而取得胜利. 同样地，第一个玩家选择任意其他整数，第二个玩家都会赢。 示例 2: 输入：maxChoosableInteger = 10, desiredTotal = 0 输出：true 示例 3: 输入：maxChoosableInteger = 10, desiredTotal = 1 输出：true 提示: * 1 <= maxChoosableInteger <= 20 * 0 <= desiredTotal <= 300
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 记忆化搜索+状态压缩，博弈论

算法步骤:
1. 使用位掩码表示已选择的数字
2. 记忆化搜索，判断当前状态是否能赢
3. 如果当前玩家能选择一个数字使得对手必输，则当前玩家能赢

关键点:
- 状态压缩：使用整数表示已选择的数字集合
- 记忆化搜索避免重复计算
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(2^n * n) - n为maxChoosableInteger，状态数*每次选择
空间复杂度: O(2^n) - 记忆化存储空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from functools import lru_cache
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def can_i_win(maxChoosableInteger: int, desiredTotal: int) -> bool:
    """
    函数式接口 - 我能赢吗
    
    实现思路:
    使用记忆化搜索+状态压缩，判断先手是否能赢。
    
    Args:
        maxChoosableInteger: 可选择的最大整数
        desiredTotal: 目标累计和
        
    Returns:
        先手是否能赢
        
    Example:
        >>> can_i_win(10, 11)
        False
    """
    # 如果所有数字的和都小于目标，先手不能赢
    if maxChoosableInteger * (maxChoosableInteger + 1) // 2 < desiredTotal:
        return False
    
    # 如果目标为0，先手直接赢
    if desiredTotal <= 0:
        return True
    
    @lru_cache(maxsize=None)
    def dfs(used: int, current_sum: int) -> bool:
        """记忆化搜索"""
        # 如果当前累计和已经达到或超过目标，当前玩家输了（因为是对手达到的）
        if current_sum >= desiredTotal:
            return False
        
        # 尝试选择每个未使用的数字
        for i in range(1, maxChoosableInteger + 1):
            mask = 1 << (i - 1)
            if used & mask == 0:  # 数字i未被使用
                # 如果选择i后，对手不能赢，则当前玩家能赢
                if not dfs(used | mask, current_sum + i):
                    return True
        
        return False
    
    return dfs(0, 0)


# 自动生成Solution类（无需手动编写）
Solution = create_solution(can_i_win)
