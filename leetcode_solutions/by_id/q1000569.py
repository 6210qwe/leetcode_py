# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000569
标题: 与非的谜题
难度: hard
链接: https://leetcode.cn/problems/ryfUiz/
题目类型: 其他
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCP 81. 与非的谜题 - 在永恒之森中，封存着有关万灵之树线索的卷轴，只要探险队通过最后的考验，便可以获取前往万灵之树的线索。 探险队需要从一段不断变化的谜题数组中找到最终的密码，初始的谜题为长度为 `n` 的数组 `arr`（下标从 0 开始），数组中的数字代表了 `k` 位二进制数。 破解谜题的过程中，需要使用 `与非（NAND）` 运算方式，`operations[i] = [type,x,y]` 表示第 `i` 次进行的谜题操作信息： - 若 `type = 0`，表示修改操作，将谜题数组中下标 `x` 的数字变化为 `y`； - 若 `type = 1`，表示运算操作，将数字 `y` 进行 `x*n` 次「与非」操作，第 `i` 次与非操作为 `y = y NAND arr[i%n]`； > 运算操作结果即：`y NAND arr[0%n] NAND arr[1%n] NAND arr[2%n] ... NAND arr[(x*n-1)%n]` 最后，将所有运算操作的结果按顺序逐一进行 `异或（XOR）`运算，从而得到最终解开封印的密码。请返回最终解开封印的密码。 **注意:** - 「与非」（NAND）的操作为：先进行 `与` 操作，后进行 `非` 操作。 > 例如：两个三位二进制数`2`和`3`，其与非结果为 `NOT ((010) AND (011)) = (101) = 5` **示例 1：** > 输入: > `k = 3` > `arr = [1,2]` > `operations = [[1,2,3],[0,0,3],[1,2,2]]` > > 输出: `2` > > 解释： > 初始的谜题数组为 [1,2]，二进制位数为 3， > 第 0 次进行运算操作，将数字 3(011) 进行 2\*2 次「与非」运算， > 运算操作结果为 `3 NAND 1 NAND 2 NAND 1 NAND 2 = 5` > 第 1 次进行修改操作，谜题数组的第 `0` 个数字变化为 `3`，谜题变成 `[3,2]` > 第 2 次进行运算操作，将数字 2(010) 进行 2\*2 次「与非」运算， > 运算操作结果为 `2 NAND 3 NAND 2 NAND 3 NAND 2 = 7` > 所有运算操作结果进行「异或」运算为 `5 XOR 7 = 2` > 因此得到的最终密码为 `2`。 **示例 2：** > 输入: > `k = 4` > `arr = [4,6,4,7,10,9,11]` > `operations = [[1,5,7],[1,7,14],[0,6,7],[1,6,5]]` > 输出: `9` > 解释: > 初始的谜题数组为 [4,6,4,7,10,9,11], > 第 0 次进行运算操作，运算操作结果为 5； > 第 1 次进行运算操作，运算操作结果为 5； > 第 2 次进行修改操作，修改后谜题数组为 [4, 6, 4, 7, 10, 9, 7]； > 第 3 次进行运算操作，运算操作结果为 9； > 所有运算操作结果进行「异或」运算为 `5 XOR 5 XOR 9 = 9`； > 因此得到的最终密码为 `9`。 **提示:** - `1 <= arr.length, operations.length <= 10^4` - `1 <= k <= 30` - `0 <= arr[i] < 2^k` - 若 `type = 0`，`0 <= x < arr.length` 且 `0 <= y < 2^k` - 若 `type = 1`，`1 <= x < 10^9` 且 `0 <= y < 2^k` - 保证存在 `type = 1` 的操作
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想:
- 使用线段树来维护区间内的与非操作，以便快速更新和查询。
- 对于每个修改操作，更新线段树。
- 对于每个运算操作，利用线段树快速计算结果。

算法步骤:
1. 初始化线段树，用于维护区间内的与非操作。
2. 遍历操作列表：
   - 如果是修改操作，更新线段树。
   - 如果是运算操作，利用线段树快速计算结果，并将其加入到结果列表中。
3. 将所有运算操作的结果进行异或运算，得到最终结果。

关键点:
- 线段树的构建和更新。
- 快速计算与非操作的结果。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O((n + m) * log n)，其中 n 是数组长度，m 是操作次数。
空间复杂度: O(n)，线段树的空间复杂度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)

    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self.build(arr, 2 * node + 1, start, mid)
            self.build(arr, 2 * node + 2, mid + 1, end)
            self.tree[node] = self.nand(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def update(self, index, value, node=0, start=0, end=None):
        if end is None:
            end = self.n - 1
        if start == end:
            self.tree[node] = value
        else:
            mid = (start + end) // 2
            if start <= index <= mid:
                self.update(index, value, 2 * node + 1, start, mid)
            else:
                self.update(index, value, 2 * node + 2, mid + 1, end)
            self.tree[node] = self.nand(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def query(self, left, right, node=0, start=0, end=None):
        if end is None:
            end = self.n - 1
        if left > end or right < start:
            return -1
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        left_result = self.query(left, right, 2 * node + 1, start, mid)
        right_result = self.query(left, right, 2 * node + 2, mid + 1, end)
        if left_result == -1:
            return right_result
        if right_result == -1:
            return left_result
        return self.nand(left_result, right_result)

    @staticmethod
    def nand(a, b):
        return ~ (a & b) & ((1 << 30) - 1)

def solution(k: int, arr: List[int], operations: List[List[int]]) -> int:
    n = len(arr)
    segment_tree = SegmentTree(arr)
    result = 0

    for op in operations:
        if op[0] == 0:
            # 修改操作
            segment_tree.update(op[1], op[2])
        else:
            # 运算操作
            total_nand = op[2]
            for _ in range(op[1]):
                total_nand = segment_tree.nand(total_nand, segment_tree.query(0, n - 1))
            result ^= total_nand

    return result

Solution = create_solution(solution)