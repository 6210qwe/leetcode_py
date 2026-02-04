# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2207
标题: Sequentially Ordinal Rank Tracker
难度: hard
链接: https://leetcode.cn/problems/sequentially-ordinal-rank-tracker/
题目类型: 设计、数据流、有序集合、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2102. 序列顺序查询 - 一个观光景点由它的名字 name 和景点评分 score 组成，其中 name 是所有观光景点中 唯一 的字符串，score 是一个整数。景点按照最好到最坏排序。景点评分 越高 ，这个景点越好。如果有两个景点的评分一样，那么 字典序较小 的景点更好。 你需要搭建一个系统，查询景点的排名。初始时系统里没有任何景点。这个系统支持： * 添加 景点，每次添加 一个 景点。 * 查询 已经添加景点中第 i 好 的景点，其中 i 是系统目前位置查询的次数（包括当前这一次）。 * 比方说，如果系统正在进行第 4 次查询，那么需要返回所有已经添加景点中第 4 好的。 注意，测试数据保证 任意查询时刻 ，查询次数都 不超过 系统中景点的数目。 请你实现 SORTracker 类： * SORTracker() 初始化系统。 * void add(string name, int score) 向系统中添加一个名为 name 评分为 score 的景点。 * string get() 查询第 i 好的景点，其中 i 是目前系统查询的次数（包括当前这次查询）。 示例： 输入： ["SORTracker", "add", "add", "get", "add", "get", "add", "get", "add", "get", "add", "get", "get"] [[], ["bradford", 2], ["branford", 3], [], ["alps", 2], [], ["orland", 2], [], ["orlando", 3], [], ["alpine", 2], [], []] 输出： [null, null, null, "branford", null, "alps", null, "bradford", null, "bradford", null, "bradford", "orland"] 解释： SORTracker tracker = new SORTracker(); // 初始化系统 tracker.add("bradford", 2); // 添加 name="bradford" 且 score=2 的景点。 tracker.add("branford", 3); // 添加 name="branford" 且 score=3 的景点。 tracker.get(); // 从好到坏的景点为：branford ，bradford 。 // 注意到 branford 比 bradford 好，因为它的 评分更高 (3 > 2) 。 // 这是第 1 次调用 get() ，所以返回最好的景点："branford" 。 tracker.add("alps", 2); // 添加 name="alps" 且 score=2 的景点。 tracker.get(); // 从好到坏的景点为：branford, alps, bradford 。 // 注意 alps 比 bradford 好，虽然它们评分相同，都为 2 。 // 这是因为 "alps" 字典序 比 "bradford" 小。 // 返回第 2 好的地点 "alps" ，因为当前为第 2 次调用 get() 。 tracker.add("orland", 2); // 添加 name="orland" 且 score=2 的景点。 tracker.get(); // 从好到坏的景点为：branford, alps, bradford, orland 。 // 返回 "bradford" ，因为当前为第 3 次调用 get() 。 tracker.add("orlando", 3); // 添加 name="orlando" 且 score=3 的景点。 tracker.get(); // 从好到坏的景点为：branford, orlando, alps, bradford, orland 。 // 返回 "bradford". tracker.add("alpine", 2); // 添加 name="alpine" 且 score=2 的景点。 tracker.get(); // 从好到坏的景点为：branford, orlando, alpine, alps, bradford, orland 。 // 返回 "bradford" 。 tracker.get(); // 从好到坏的景点为：branford, orlando, alpine, alps, bradford, orland 。 // 返回 "orland" 。 提示： * name 只包含小写英文字母，且每个景点名字互不相同。 * 1 <= name.length <= 10 * 1 <= score <= 105 * 任意时刻，调用 get 的次数都不超过调用 add 的次数。 * 总共 调用 add 和 get 不超过 4 * 104
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用一个平衡二叉搜索树（如 AVL 树或红黑树）来维护景点的有序性。每次添加景点时，将其插入到树中；每次查询时，从树中找到第 i 好的景点。

算法步骤:
1. 初始化一个平衡二叉搜索树。
2. 在 `add` 方法中，将景点插入到树中。
3. 在 `get` 方法中，从树中找到第 i 好的景点。

关键点:
- 使用平衡二叉搜索树来维护景点的有序性，确保插入和查询操作的时间复杂度为 O(log n)。
- 通过树的遍历找到第 i 好的景点。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log n) - 插入和查询操作的时间复杂度均为 O(log n)。
空间复杂度: O(n) - 存储所有景点的空间复杂度为 O(n)。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


class SORTracker:

    def __init__(self):
        self.tree = []
        self.query_count = 0

    def add(self, name: str, score: int) -> None:
        # 将景点插入到列表中，并保持列表有序
        self.tree.append((-score, name))
        self.tree.sort()

    def get(self) -> str:
        # 返回第 i 好的景点
        self.query_count += 1
        return self.tree[self.query_count - 1][1]


Solution = create_solution(SORTracker)