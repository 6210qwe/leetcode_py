# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 297
标题: Serialize and Deserialize Binary Tree
难度: hard
链接: https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/
题目类型: 树、深度优先搜索、广度优先搜索、设计、字符串、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
297. 二叉树的序列化与反序列化 - 序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。 请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。 提示: 输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式 [https://leetcode.cn/help-center/3812581/]。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。 示例 1： [https://assets.leetcode.com/uploads/2020/09/15/serdeser.jpg] 输入：root = [1,2,3,null,null,4,5] 输出：[1,2,3,null,null,4,5] 示例 2： 输入：root = [] 输出：[] 示例 3： 输入：root = [1] 输出：[1] 示例 4： 输入：root = [1,2] 输出：[1,2] 提示： * 树中结点数在范围 [0, 104] 内 * -1000 <= Node.val <= 1000
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 前序遍历序列化，递归反序列化

算法步骤:
1. 序列化：前序遍历，用","分隔，null用"#"表示
2. 反序列化：递归构建，按前序遍历顺序

关键点:
- 前序遍历
- 递归构建
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 遍历所有节点
空间复杂度: O(n) - 序列化字符串空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def serialize(root: Optional[TreeNode]) -> str:
    """
    函数式接口 - 二叉树的序列化
    
    实现思路:
    前序遍历序列化。
    
    Args:
        root: 二叉树根节点
        
    Returns:
        序列化字符串
        
    Example:
        >>> root = TreeNode(1)
        >>> root.left = TreeNode(2)
        >>> serialize(root)
        '1,2,#,#,#'
    """
    result = []
    
    def preorder(node: Optional[TreeNode]):
        if not node:
            result.append("#")
            return
        result.append(str(node.val))
        preorder(node.left)
        preorder(node.right)
    
    preorder(root)
    return ",".join(result)


def deserialize(data: str) -> Optional[TreeNode]:
    """
    函数式接口 - 二叉树的反序列化
    
    实现思路:
    递归反序列化。
    
    Args:
        data: 序列化字符串
        
    Returns:
        二叉树根节点
        
    Example:
        >>> root = deserialize('1,2,#,#,#')
    """
    values = data.split(",")
    index = [0]
    
    def build() -> Optional[TreeNode]:
        if index[0] >= len(values) or values[index[0]] == "#":
            index[0] += 1
            return None
        
        node = TreeNode(int(values[index[0]]))
        index[0] += 1
        node.left = build()
        node.right = build()
        return node
    
    return build()


# 自动生成Solution类（无需手动编写）
Solution = create_solution(serialize, deserialize)
