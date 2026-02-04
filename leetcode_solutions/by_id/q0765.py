# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 765
标题: Serialize and Deserialize N-ary Tree
难度: hard
链接: https://leetcode.cn/problems/serialize-and-deserialize-n-ary-tree/
题目类型: 树、深度优先搜索、广度优先搜索、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
428. 序列化和反序列化 N 叉树 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用前序遍历（根-子树）来序列化N叉树，并使用递归的方法进行反序列化。

算法步骤:
1. 序列化：
   - 使用前序遍历将N叉树转换为字符串。
   - 每个节点的格式为 "node.val[num_children]child1...childN"。
   - 使用逗号分隔每个节点。
2. 反序列化：
   - 将字符串按逗号分割成节点列表。
   - 使用递归方法重建N叉树。

关键点:
- 使用前序遍历可以唯一确定N叉树的结构。
- 在反序列化时，通过递归解析每个节点及其子节点。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是节点数。每个节点在序列化和反序列化过程中都被访问一次。
空间复杂度: O(n)，存储序列化后的字符串和递归调用栈。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.tree import Node


class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string."""
        if not root:
            return ""
        
        def dfs(node: 'Node') -> str:
            if not node.children:
                return f"{node.val}"
            children = ",".join(dfs(child) for child in node.children)
            return f"{node.val}[{len(node.children)}]{children}"
        
        return dfs(root)

    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree."""
        if not data:
            return None
        
        def parse_node(s: str) -> 'Node':
            i = s.find('[')
            if i == -1:
                return Node(int(s), [])
            val = int(s[:i])
            num_children = int(s[i+1:i+3])
            j = i + 3
            children = []
            for _ in range(num_children):
                end = s.find(',', j)
                if end == -1:
                    end = len(s)
                children.append(parse_node(s[j:end]))
                j = end + 1
            return Node(val, children)
        
        return parse_node(data)


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

Solution = create_solution(Codec)