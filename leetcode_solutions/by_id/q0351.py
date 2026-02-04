# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 351
标题: Android Unlock Patterns
难度: medium
链接: https://leetcode.cn/problems/android-unlock-patterns/
题目类型: 位运算、动态规划、回溯、状态压缩
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
351. 安卓系统手势解锁 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 回溯 + 预处理中间必须经过的点 + 利用对称性剪枝

算法步骤:
1. 预先建立一个 10×10 的矩阵 skip[i][j]，表示从点 i 跳到点 j 之间如果存在必须经过的中间点，则为该点编号，否则为 0；例如 1 和 3 之间必须经过 2。
2. 使用一个长度为 10 的 visited 数组记录 1~9 是否已被使用，编写回溯函数 dfs(cur, remain) 表示当前在 cur 点，还需要选择 remain 个点。
3. 在 dfs 中枚举下一个点 nxt，要求：nxt 未访问，且 skip[cur][nxt] == 0 或者 skip[cur][nxt] 已经访问过，即中间点要么不存在要么已经被选取。
4. 当 remain 递减到 0 时累加方案数。
5. 由于键盘具有对称性（1、3、7、9 等价，2、4、6、8 成对对称），分别从代表点开始搜索，然后乘以对应倍数以减少搜索量。

关键点:
- 使用 skip 矩阵显式限制「跨越中间点」的非法跳跃。
- 回溯时及时剪枝，避免重复访问或非法连接。
- 通过对称性优化，将原本 9 个起点的搜索缩减为 3 类起点。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(3^9) 量级 - 搜索树高度不超过 9，且大量分支被剪枝，实际状态数远小于 9!。
空间复杂度: O(1) - 仅使用固定规模的 visited 与 skip 数组以及递归栈。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def android_unlock_patterns(m: int, n: int) -> int:
    """
    统计安卓九宫格中，从长度为 m 到 n 的所有合法解锁方案数。

    使用回溯 + 预处理跨越中点的非法跳跃 + 利用对称性剪枝。
    """
    # 预处理跳跃中必经的中间点，0 表示无中间点
    skip = [[0] * 10 for _ in range(10)]
    skip[1][3] = skip[3][1] = 2
    skip[1][7] = skip[7][1] = 4
    skip[3][9] = skip[9][3] = 6
    skip[7][9] = skip[9][7] = 8
    skip[1][9] = skip[9][1] = 5
    skip[3][7] = skip[7][3] = 5
    skip[4][6] = skip[6][4] = 5
    skip[2][8] = skip[8][2] = 5

    visited = [False] * 10

    def dfs(cur: int, remain: int) -> int:
        if remain == 0:
            return 1
        visited[cur] = True
        res = 0
        for nxt in range(1, 10):
            mid = skip[cur][nxt]
            if not visited[nxt] and (mid == 0 or visited[mid]):
                res += dfs(nxt, remain - 1)
        visited[cur] = False
        return res

    ans = 0
    for length in range(m, n + 1):
        # 1,3,7,9 对称
        ans += dfs(1, length - 1) * 4
        # 2,4,6,8 对称
        ans += dfs(2, length - 1) * 4
        # 中心点 5
        ans += dfs(5, length - 1)
    return ans


# 自动生成Solution类（无需手动编写）
Solution = create_solution(android_unlock_patterns)
