# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000442
标题: 力扣泡泡龙
难度: hard
链接: https://leetcode.cn/problems/WInSav/
题目类型: 树、动态规划、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCP 60. 力扣泡泡龙 - 欢迎各位勇者来到力扣城，本次试炼主题为「力扣泡泡龙」。 游戏初始状态的泡泡形如二叉树 `root`，每个节点值对应了该泡泡的分值。勇者最多可以击破一个节点泡泡，要求满足： - 被击破的节点泡泡 **至多** 只有一个子节点泡泡 - 当被击破的节点泡泡有子节点泡泡时，则子节点泡泡将取代被击破泡泡的位置 > 注：即整棵子树泡泡上移 请问在击破一个节点泡泡操作或无击破操作后，二叉泡泡树的最大「层和」是多少。 **注意：** - 「层和」为同一高度的所有节点的分值之和 **示例 1：** > 输入：`root = [6,0,3,null,8]` > > 输出：`11` > > 解释：勇者的最佳方案如图所示 >![image.png](https://pic.leetcode.cn/1648180809-XSWPLu-image.png){:height="100px"} **示例 2：** > 输入：`root = [5,6,2,4,null,null,1,3,5]` > > 输出：`9` > > 解释：勇者击破 6 节点，此时「层和」最大为 3+5+1 = 9 >![image.png](https://pic.leetcode.cn/1648180769-TLpYop-image.png){:height="200px"} **示例 3：** > 输入：`root = [-5,1,7]` > > 输出：`8` > > 解释：勇者不击破节点，「层和」最大为 1+7 = 8 **提示**： - `2 <= 树中节点个数 <= 10^5` - `-10000 <= 树中节点的值 <= 10000`
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用层次遍历计算每一层的和，并记录可以被击破的节点及其对层和的影响。

算法步骤:
1. 层次遍历二叉树，记录每一层的节点和。
2. 在遍历过程中，记录可以被击破的节点及其对层和的影响。
3. 计算击破某个节点后的最大层和。

关键点:
- 使用队列进行层次遍历。
- 记录每一层的节点和。
- 记录可以被击破的节点及其对层和的影响。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是树中节点的数量。每个节点只访问一次。
空间复杂度: O(n)，队列和层和记录所需的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def max_layer_sum(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    
    # 初始化队列和层和记录
    queue = [root]
    layer_sums = []
    removable_nodes = []

    while queue:
        level_size = len(queue)
        current_sum = 0
        next_level = []
        
        for _ in range(level_size):
            node = queue.pop(0)
            current_sum += node.val
            
            # 记录可以被击破的节点
            if (node.left and not node.right) or (node.right and not node.left):
                removable_nodes.append((node, current_sum - node.val))
            
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        
        layer_sums.append(current_sum)
        queue = next_level
    
    # 计算击破某个节点后的最大层和
    max_sum = max(layer_sums)
    for node, new_sum in removable_nodes:
        max_sum = max(max_sum, new_sum + sum(layer_sums[node.level + 1:]))
    
    return max_sum

Solution = create_solution(max_layer_sum)