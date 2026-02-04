# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100307
标题: 序列化与反序列化二叉树
难度: hard
链接: https://leetcode.cn/problems/xu-lie-hua-er-cha-shu-lcof/
题目类型: 树、深度优先搜索、广度优先搜索、设计、字符串、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 156. 序列化与反序列化二叉树 - 序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。 请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。 提示: 输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式 [/faq/#binary-tree]。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。 示例 1： [https://assets.leetcode.com/uploads/2020/09/15/serdeser.jpg] 输入：root = [1,2,3,null,null,4,5] 输出：[1,2,3,null,null,4,5] 示例 2： 输入：root = [] 输出：[] 示例 3： 输入：root = [1] 输出：[1] 示例 4： 输入：root = [1,2] 输出：[1,2] 提示： * 树中结点数在范围 [0, 104] 内 * -1000 <= Node.val <= 1000 注意：本题与主站 297 题相同：https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/ [https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用前序遍历进行序列化和反序列化。

算法步骤:
1. 序列化时，使用前序遍历（根-左-右），将节点值和空节点用特殊字符表示。
2. 反序列化时，根据前序遍历的结果重建二叉树。

关键点:
- 使用前序遍历可以唯一确定二叉树的结构。
- 空节点用特殊字符表示，以便在反序列化时正确处理。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是二叉树的节点数，每个节点都需要访问一次。
空间复杂度: O(n)，递归调用栈的空间以及存储序列化结果的空间。
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
            val = nodes.pop(0)
            if val == "None":
                return None
            node = TreeNode(int(val))
            node.left = build_tree(nodes)
            node.right = build_tree(nodes)
            return node
        
        nodes = data.split(',')
        return build_tree(nodes)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

Solution = create_solution(Codec)