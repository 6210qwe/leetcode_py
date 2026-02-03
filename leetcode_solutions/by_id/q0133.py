# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 133
标题: Clone Graph
难度: medium
链接: https://leetcode.cn/problems/clone-graph/
题目类型: 深度优先搜索、广度优先搜索、图、哈希表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
133. 克隆图 - 给你无向 连通 [https://baike.baidu.com/item/连通图/6460995?fr=aladdin] 图中一个节点的引用，请你返回该图的 深拷贝 [https://baike.baidu.com/item/深拷贝/22785317?fr=aladdin]（克隆）。 图中的每个节点都包含它的值 val（int） 和其邻居的列表（list[Node]）。 class Node { public int val; public List<Node> neighbors; } 测试用例格式： 简单起见，每个节点的值都和它的索引相同。例如，第一个节点值为 1（val = 1），第二个节点值为 2（val = 2），以此类推。该图在测试用例中使用邻接列表表示。 邻接列表 是用于表示有限图的无序列表的集合。每个列表都描述了图中节点的邻居集。 给定节点将始终是图中的第一个节点（值为 1）。你必须将 给定节点的拷贝 作为对克隆图的引用返回。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/02/01/133_clone_graph_question.png] 输入：adjList = [[2,4],[1,3],[2,4],[1,3]] 输出：[[2,4],[1,3],[2,4],[1,3]] 解释： 图中有 4 个节点。 节点 1 的值是 1，它有两个邻居：节点 2 和 4 。 节点 2 的值是 2，它有两个邻居：节点 1 和 3 。 节点 3 的值是 3，它有两个邻居：节点 2 和 4 。 节点 4 的值是 4，它有两个邻居：节点 1 和 3 。 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/02/01/graph.png] 输入：adjList = [[]] 输出：[[]] 解释：输入包含一个空列表。该图仅仅只有一个值为 1 的节点，它没有任何邻居。 示例 3： 输入：adjList = [] 输出：[] 解释：这个图是空的，它不含任何节点。 提示： * 这张图中的节点数在 [0, 100] 之间。 * 1 <= Node.val <= 100 * 每个节点值 Node.val 都是唯一的， * 图中没有重复的边，也没有自环。 * 图是连通图，你可以从给定节点访问到所有节点。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: BFS或DFS遍历图，使用哈希表存储已克隆的节点

算法步骤:
1. 使用BFS遍历图
2. 对于每个节点，创建克隆节点并存储到哈希表
3. 复制邻居关系

关键点:
- BFS+哈希表
- 时间复杂度O(V+E)，空间复杂度O(V)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(V+E) - V为节点数，E为边数
空间复杂度: O(V) - 哈希表和队列空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from collections import deque
from leetcode_solutions.utils.solution import create_solution


# Node类定义（LeetCode提供）
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: Optional[Node]) -> Optional[Node]:
    """
    函数式接口 - 克隆图
    
    实现思路:
    BFS遍历图，使用哈希表存储已克隆的节点。
    
    Args:
        node: 无向连通图的节点引用
        
    Returns:
        克隆图的头节点
        
    Example:
        >>> # 示例用法
        >>> # node = Node(1, [Node(2), Node(4)])
        >>> # cloned = clone_graph(node)
    """
    if not node:
        return None
    
    cloned = {node: Node(node.val)}
    queue = deque([node])
    
    while queue:
        current = queue.popleft()
        for neighbor in current.neighbors:
            if neighbor not in cloned:
                cloned[neighbor] = Node(neighbor.val)
                queue.append(neighbor)
            cloned[current].neighbors.append(cloned[neighbor])
    
    return cloned[node]


# 自动生成Solution类（无需手动编写）
Solution = create_solution(clone_graph)
