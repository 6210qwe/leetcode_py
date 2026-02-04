# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000304
标题: 二叉树的序列化与反序列化
难度: hard
链接: https://leetcode.cn/problems/h54YBf/
题目类型: 树、深度优先搜索、广度优先搜索、设计、字符串、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 048. 二叉树的序列化与反序列化 - 序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。 请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。 示例 1： [https://assets.leetcode.com/uploads/2020/09/15/serdeser.jpg] 输入：root = [1,2,3,null,null,4,5] 输出：[1,2,3,null,null,4,5] 示例 2： 输入：root = [] 输出：[] 示例 3： 输入：root = [1] 输出：[1] 示例 4： 输入：root = [1,2] 输出：[1,2] 提示： * 输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式 [/faq/#binary-tree]。你并非必须采取这种方式，也可以采用其他的方法解决这个问题。 * 树中结点数在范围 [0, 104] 内 * -1000 <= Node.val <= 1000 注意：本题与主站 297 题相同：https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/ [https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用前序遍历进行序列化和反序列化。

算法步骤:
1. 序列化：
   - 使用前序遍历（根-左-右）将二叉树转换为字符串。
   - 空节点用 'None' 表示，并用逗号分隔节点值。
2. 反序列化：
   - 将字符串分割成列表。
   - 使用递归方法构建二叉树，根据列表中的值创建节点或空节点。

关键点:
- 前序遍历能够唯一确定一棵二叉树。
- 使用 'None' 表示空节点，确保序列化后的字符串能够准确表示二叉树结构。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是二叉树的节点数。每个节点都需要访问一次。
空间复杂度: O(n)，递归调用栈的深度最多为 n，且需要存储序列化后的字符串。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string."""
        if not root:
            return "None"
        return f"{root.val},{self.serialize(root.left)},{self.serialize(root.right)}"

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree."""
        def build_tree(nodes: List[str]) -> Optional[TreeNode]:
            if nodes[0] == "None":
                nodes.pop(0)
                return None
            root = TreeNode(int(nodes[0]))
            nodes.pop(0)
            root.left = build_tree(nodes)
            root.right = build_tree(nodes)
            return root

        nodes = data.split(',')
        return build_tree(nodes)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

Solution = create_solution(Codec)