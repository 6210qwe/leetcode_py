# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2104
标题: Operations on Tree
难度: medium
链接: https://leetcode.cn/problems/operations-on-tree/
题目类型: 树、深度优先搜索、广度优先搜索、设计、数组、哈希表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1993. 树上的操作 - 给你一棵 n 个节点的树，编号从 0 到 n - 1 ，以父节点数组 parent 的形式给出，其中 parent[i] 是第 i 个节点的父节点。树的根节点为 0 号节点，所以 parent[0] = -1 ，因为它没有父节点。你想要设计一个数据结构实现树里面对节点的加锁，解锁和升级操作。 数据结构需要支持如下函数： * Lock：指定用户给指定节点 上锁 ，上锁后其他用户将无法给同一节点上锁。只有当节点处于未上锁的状态下，才能进行上锁操作。 * Unlock：指定用户给指定节点 解锁 ，只有当指定节点当前正被指定用户锁住时，才能执行该解锁操作。 * Upgrade：指定用户给指定节点 上锁 ，并且将该节点的所有子孙节点 解锁 。只有如下 3 个条件 全部 满足时才能执行升级操作： * 指定节点当前状态为未上锁。 * 指定节点至少有一个上锁状态的子孙节点（可以是 任意 用户上锁的）。 * 指定节点没有任何上锁的祖先节点。 请你实现 LockingTree 类： * LockingTree(int[] parent) 用父节点数组初始化数据结构。 * lock(int num, int user) 如果 id 为 user 的用户可以给节点 num 上锁，那么返回 true ，否则返回 false 。如果可以执行此操作，节点 num 会被 id 为 user 的用户 上锁 。 * unlock(int num, int user) 如果 id 为 user 的用户可以给节点 num 解锁，那么返回 true ，否则返回 false 。如果可以执行此操作，节点 num 变为 未上锁 状态。 * upgrade(int num, int user) 如果 id 为 user 的用户可以给节点 num 升级，那么返回 true ，否则返回 false 。如果可以执行此操作，节点 num 会被 升级 。 示例 1： [https://assets.leetcode.com/uploads/2021/07/29/untitled.png] 输入： ["LockingTree", "lock", "unlock", "unlock", "lock", "upgrade", "lock"] [[[-1, 0, 0, 1, 1, 2, 2]], [2, 2], [2, 3], [2, 2], [4, 5], [0, 1], [0, 1]] 输出： [null, true, false, true, true, true, false] 解释： LockingTree lockingTree = new LockingTree([-1, 0, 0, 1, 1, 2, 2]); lockingTree.lock(2, 2); // 返回 true ，因为节点 2 未上锁。 // 节点 2 被用户 2 上锁。 lockingTree.unlock(2, 3); // 返回 false ，因为用户 3 无法解锁被用户 2 上锁的节点。 lockingTree.unlock(2, 2); // 返回 true ，因为节点 2 之前被用户 2 上锁。 // 节点 2 现在变为未上锁状态。 lockingTree.lock(4, 5); // 返回 true ，因为节点 4 未上锁。 // 节点 4 被用户 5 上锁。 lockingTree.upgrade(0, 1); // 返回 true ，因为节点 0 未上锁且至少有一个被上锁的子孙节点（节点 4）。 // 节点 0 被用户 1 上锁，节点 4 变为未上锁。 lockingTree.lock(0, 1); // 返回 false ，因为节点 0 已经被上锁了。 提示： * n == parent.length * 2 <= n <= 2000 * 对于 i != 0 ，满足 0 <= parent[i] <= n - 1 * parent[0] == -1 * 0 <= num <= n - 1 * 1 <= user <= 104 * parent 表示一棵合法的树。 * lock ，unlock 和 upgrade 的调用 总共 不超过 2000 次。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用邻接表表示树，并维护每个节点的锁定状态和锁定用户。

算法步骤:
1. 初始化时，构建邻接表和子节点列表。
2. lock 操作：检查节点是否已锁定，如果没有则锁定并记录用户。
3. unlock 操作：检查节点是否被指定用户锁定，如果是则解锁。
4. upgrade 操作：
   - 检查节点是否未锁定且没有上锁的祖先节点。
   - 检查节点是否有上锁的子孙节点。
   - 如果满足条件，则锁定节点并解锁所有子孙节点。

关键点:
- 使用邻接表和子节点列表来快速访问父子关系。
- 使用字典记录每个节点的锁定状态和锁定用户。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 每次操作的时间复杂度取决于树的高度和子孙节点的数量。
空间复杂度: O(n) - 需要存储邻接表、子节点列表和锁定状态。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional

class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.n = len(parent)
        self.children = [[] for _ in range(self.n)]
        self.locked = [None] * self.n
        for i in range(1, self.n):
            self.children[parent[i]].append(i)

    def lock(self, num: int, user: int) -> bool:
        if self.locked[num] is None:
            self.locked[num] = user
            return True
        return False

    def unlock(self, num: int, user: int) -> bool:
        if self.locked[num] == user:
            self.locked[num] = None
            return True
        return False

    def has_locked_ancestor(self, num: int) -> bool:
        while num != -1:
            if self.locked[num] is not None:
                return True
            num = self.parent[num]
        return False

    def has_locked_descendant(self, num: int) -> bool:
        stack = [num]
        while stack:
            node = stack.pop()
            if self.locked[node] is not None:
                return True
            for child in self.children[node]:
                stack.append(child)
        return False

    def unlock_descendants(self, num: int):
        stack = [num]
        while stack:
            node = stack.pop()
            self.locked[node] = None
            for child in self.children[node]:
                stack.append(child)

    def upgrade(self, num: int, user: int) -> bool:
        if self.locked[num] is not None:
            return False
        if self.has_locked_ancestor(num):
            return False
        if not self.has_locked_descendant(num):
            return False
        self.locked[num] = user
        self.unlock_descendants(num)
        return True

# Example usage
# lockingTree = LockingTree([-1, 0, 0, 1, 1, 2, 2])
# print(lockingTree.lock(2, 2))  # True
# print(lockingTree.unlock(2, 3))  # False
# print(lockingTree.unlock(2, 2))  # True
# print(lockingTree.lock(4, 5))  # True
# print(lockingTree.upgrade(0, 1))  # True
# print(lockingTree.lock(0, 1))  # False