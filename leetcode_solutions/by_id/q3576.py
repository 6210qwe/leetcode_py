# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3576
标题: Find Subtree Sizes After Changes
难度: medium
链接: https://leetcode.cn/problems/find-subtree-sizes-after-changes/
题目类型: 树、深度优先搜索、数组、哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3331. 修改后子树的大小 - 给你一棵 n 个节点且根节点为编号 0 的树，节点编号为 0 到 n - 1 。这棵树用一个长度为 n 的数组 parent 表示，其中 parent[i] 是第 i 个节点的父亲节点的编号。由于节点 0 是根，parent[0] == -1 。 给你一个长度为 n 的字符串 s ，其中 s[i] 是节点 i 对应的字符。 对于节点编号从 1 到 n - 1 的每个节点 x ，我们 同时 执行以下操作 一次 ： * 找到距离节点 x 最近 的祖先节点 y ，且 s[x] == s[y] 。 * 如果节点 y 不存在，那么不做任何修改。 * 否则，将节点 x 与它父亲节点之间的边 删除 ，在 x 与 y 之间连接一条边，使 y 变为 x 新的父节点。 请你返回一个长度为 n 的数组 answer ，其中 answer[i] 是 最终 树中，节点 i 为根的 子树 的 大小 。 示例 1： 输入：parent = [-1,0,0,1,1,1], s = "abaabc" 输出：[6,3,1,1,1,1] 解释： [https://assets.leetcode.com/uploads/2024/08/15/graphex1drawio.png] 节点 3 的父节点从节点 1 变为节点 0 。 示例 2： 输入：parent = [-1,0,4,0,1], s = "abbba" 输出：[5,2,1,1,1] 解释： [https://assets.leetcode.com/uploads/2024/08/20/exgraph2drawio.png] 以下变化会同时发生： * 节点 4 的父节点从节点 1 变为节点 0 。 * 节点 2 的父节点从节点 4 变为节点 1 。 提示： * n == parent.length == s.length * 1 <= n <= 105 * 对于所有的 i >= 1 ，都有 0 <= parent[i] <= n - 1 。 * parent[0] == -1 * parent 表示一棵合法的树。 * s 只包含小写英文字母。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索 (DFS) 来重构树，并计算每个子树的大小。

算法步骤:
1. 构建初始树结构。
2. 使用 DFS 重新构建树，找到每个节点最近的祖先节点。
3. 再次使用 DFS 计算每个子树的大小。

关键点:
- 使用字典来存储每个节点的子节点。
- 在 DFS 中更新每个节点的父节点。
- 使用递归计算每个子树的大小。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def find_subtree_sizes_after_changes(parent: List[int], s: str) -> List[int]:
    n = len(parent)
    children = [[] for _ in range(n)]
    new_parent = list(parent)
    
    # 构建初始树结构
    for i in range(1, n):
        children[parent[i]].append(i)
    
    # 使用 DFS 重新构建树
    def dfs(node: int, ancestors: dict) -> None:
        for child in children[node]:
            if s[child] in ancestors:
                new_parent[child] = ancestors[s[child]]
            else:
                ancestors[s[child]] = child
            dfs(child, ancestors)
            del ancestors[s[child]]
    
    dfs(0, {s[0]: 0})
    
    # 重新构建子节点列表
    new_children = [[] for _ in range(n)]
    for i in range(1, n):
        new_children[new_parent[i]].append(i)
    
    # 计算每个子树的大小
    def calculate_size(node: int) -> int:
        size = 1
        for child in new_children[node]:
            size += calculate_size(child)
        return size
    
    result = [calculate_size(i) for i in range(n)]
    return result

Solution = create_solution(find_subtree_sizes_after_changes)