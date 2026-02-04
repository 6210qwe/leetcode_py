# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1820
标题: Number Of Ways To Reconstruct A Tree
难度: hard
链接: https://leetcode.cn/problems/number-of-ways-to-reconstruct-a-tree/
题目类型: 树、图
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1719. 重构一棵树的方案数 - 给你一个数组 pairs ，其中 pairs[i] = [xi, yi] ，并且满足： * pairs 中没有重复元素 * xi < yi 令 ways 为满足下面条件的有根树的方案数： * 树所包含的所有节点值都在 pairs 中。 * 一个数对 [xi, yi] 出现在 pairs 中 当且仅当 xi 是 yi 的祖先或者 yi 是 xi 的祖先。 * 注意：构造出来的树不一定是二叉树。 两棵树被视为不同的方案当存在至少一个节点在两棵树中有不同的父节点。 请你返回： * 如果 ways == 0 ，返回 0 。 * 如果 ways == 1 ，返回 1 。 * 如果 ways > 1 ，返回 2 。 一棵 有根树 指的是只有一个根节点的树，所有边都是从根往外的方向。 我们称从根到一个节点路径上的任意一个节点（除去节点本身）都是该节点的 祖先 。根节点没有祖先。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2021/01/09/trees2.png] 输入：pairs = [[1,2],[2,3]] 输出：1 解释：如上图所示，有且只有一个符合规定的有根树。 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2021/01/09/tree.png] 输入：pairs = [[1,2],[2,3],[1,3]] 输出：2 解释：有多个符合规定的有根树，其中三个如上图所示。 示例 3： 输入：pairs = [[1,2],[2,3],[2,4],[1,5]] 输出：0 解释：没有符合规定的有根树。 提示： * 1 <= pairs.length <= 105 * 1 <= xi < yi <= 500 * pairs 中的元素互不相同。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用度数和拓扑排序来判断树的唯一性。

算法步骤:
1. 构建邻接表表示图，并计算每个节点的度数。
2. 找出度数最大的节点作为根节点。
3. 检查是否存在多个度数相同的最大节点，如果有则返回 2。
4. 使用拓扑排序验证是否可以构建唯一的树。
5. 如果拓扑排序过程中发现矛盾，则返回 0；否则返回 1。

关键点:
- 使用度数来确定根节点。
- 使用拓扑排序来验证树的唯一性。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是节点数，m 是边数。
空间复杂度: O(n + m)，用于存储邻接表和度数。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional

def checkWays(pairs: List[List[int]]) -> int:
    from collections import defaultdict, deque
    
    # 构建邻接表和度数
    graph = defaultdict(set)
    degree = defaultdict(int)
    
    for x, y in pairs:
        graph[x].add(y)
        graph[y].add(x)
        degree[x] += 1
        degree[y] += 1
    
    # 找出度数最大的节点
    max_degree = max(degree.values())
    roots = [node for node, deg in degree.items() if deg == max_degree]
    
    if len(roots) > 1:
        return 2
    
    root = roots[0]
    
    # 拓扑排序验证
    queue = deque([root])
    visited = set([root])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    if len(visited) != len(graph):
        return 0
    
    # 检查是否有多个根节点
    if any(len(graph[node]) == max_degree for node in graph if node != root):
        return 2
    
    return 1

Solution = create_solution(checkWays)