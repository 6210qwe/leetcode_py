# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2596
标题: Add Edges to Make Degrees of All Nodes Even
难度: hard
链接: https://leetcode.cn/problems/add-edges-to-make-degrees-of-all-nodes-even/
题目类型: 图、哈希表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2508. 添加边使所有节点度数都为偶数 - 给你一个有 n 个节点的 无向 图，节点编号为 1 到 n 。再给你整数 n 和一个二维整数数组 edges ，其中 edges[i] = [ai, bi] 表示节点 ai 和 bi 之间有一条边。图不一定连通。 你可以给图中添加 至多 两条额外的边（也可以一条边都不添加），使得图中没有重边也没有自环。 如果添加额外的边后，可以使得图中所有点的度数都是偶数，返回 true ，否则返回 false 。 点的度数是连接一个点的边的数目。 示例 1： [https://assets.leetcode.com/uploads/2022/10/26/agraphdrawio.png] 输入：n = 5, edges = [[1,2],[2,3],[3,4],[4,2],[1,4],[2,5]] 输出：true 解释：上图展示了添加一条边的合法方案。 最终图中每个节点都连接偶数条边。 示例 2： [https://assets.leetcode.com/uploads/2022/10/26/aagraphdrawio.png] 输入：n = 4, edges = [[1,2],[3,4]] 输出：true 解释：上图展示了添加两条边的合法方案。 示例 3： [https://assets.leetcode.com/uploads/2022/10/26/aaagraphdrawio.png] 输入：n = 4, edges = [[1,2],[1,3],[1,4]] 输出：false 解释：无法添加至多 2 条边得到一个符合要求的图。 提示： * 3 <= n <= 105 * 2 <= edges.length <= 105 * edges[i].length == 2 * 1 <= ai, bi <= n * ai != bi * 图中不会有重边
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过检查奇数度节点的数量来决定是否可以通过添加至多两条边使所有节点的度数变为偶数。

算法步骤:
1. 构建邻接表表示图。
2. 统计每个节点的度数，并记录奇数度节点。
3. 根据奇数度节点的数量和它们之间的连接情况，判断是否可以通过添加至多两条边使所有节点的度数变为偶数。

关键点:
- 奇数度节点的数量必须是 0 或 2 或 4。
- 如果有 2 个奇数度节点，可以直接连接它们。
- 如果有 4 个奇数度节点，需要检查是否存在两个未连接的节点对。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是节点数，m 是边数。
空间复杂度: O(n + m)，用于存储邻接表和度数统计。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def is_possible_to_make_even_degrees(n: int, edges: List[List[int]]) -> bool:
    # 构建邻接表
    adj_list = [[] for _ in range(n + 1)]
    degrees = [0] * (n + 1)
    
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
        degrees[u] += 1
        degrees[v] += 1
    
    # 找出所有奇数度节点
    odd_degree_nodes = [i for i in range(1, n + 1) if degrees[i] % 2 != 0]
    
    # 奇数度节点的数量必须是 0 或 2 或 4
    if len(odd_degree_nodes) > 4 or len(odd_degree_nodes) % 2 != 0:
        return False
    
    # 如果没有奇数度节点，直接返回 True
    if len(odd_degree_nodes) == 0:
        return True
    
    # 如果有两个奇数度节点，直接连接它们
    if len(odd_degree_nodes) == 2:
        u, v = odd_degree_nodes
        return u not in adj_list[v]
    
    # 如果有四个奇数度节点，检查是否存在两个未连接的节点对
    if len(odd_degree_nodes) == 4:
        a, b, c, d = odd_degree_nodes
        return (a not in adj_list[b] and c not in adj_list[d]) or \
               (a not in adj_list[c] and b not in adj_list[d]) or \
               (a not in adj_list[d] and b not in adj_list[c])
    
    return False

Solution = create_solution(is_possible_to_make_even_degrees)