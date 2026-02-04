# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2894
标题: Maximum Elegance of a K-Length Subsequence
难度: hard
链接: https://leetcode.cn/problems/maximum-elegance-of-a-k-length-subsequence/
题目类型: 栈、贪心、数组、哈希表、排序、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2813. 子序列最大优雅度 - 给你一个长度为 n 的二维整数数组 items 和一个整数 k 。 items[i] = [profiti, categoryi]，其中 profiti 和 categoryi 分别表示第 i 个项目的利润和类别。 现定义 items 的 子序列 的 优雅度 可以用 total_profit + distinct_categories2 计算，其中 total_profit 是子序列中所有项目的利润总和，distinct_categories 是所选子序列所含的所有类别中不同类别的数量。 你的任务是从 items 所有长度为 k 的子序列中，找出 最大优雅度 。 用整数形式表示并返回 items 中所有长度恰好为 k 的子序列的最大优雅度。 注意：数组的子序列是经由原数组删除一些元素（可能不删除）而产生的新数组，且删除不改变其余元素相对顺序。 示例 1： 输入：items = [[3,2],[5,1],[10,1]], k = 2 输出：17 解释： 在这个例子中，我们需要选出长度为 2 的子序列。 其中一种方案是 items[0] = [3,2] 和 items[2] = [10,1] 。 子序列的总利润为 3 + 10 = 13 ，子序列包含 2 种不同类别 [2,1] 。 因此，优雅度为 13 + 22 = 17 ，可以证明 17 是可以获得的最大优雅度。 示例 2： 输入：items = [[3,1],[3,1],[2,2],[5,3]], k = 3 输出：19 解释： 在这个例子中，我们需要选出长度为 3 的子序列。 其中一种方案是 items[0] = [3,1] ，items[2] = [2,2] 和 items[3] = [5,3] 。 子序列的总利润为 3 + 2 + 5 = 10 ，子序列包含 3 种不同类别 [1, 2, 3] 。 因此，优雅度为 10 + 32 = 19 ，可以证明 19 是可以获得的最大优雅度。 示例 3： 输入：items = [[1,1],[2,1],[3,1]], k = 3 输出：7 解释： 在这个例子中，我们需要选出长度为 3 的子序列。 我们需要选中所有项目。 子序列的总利润为 1 + 2 + 3 = 6，子序列包含 1 种不同类别 [1] 。 因此，最大优雅度为 6 + 12 = 7 。 提示： * 1 <= items.length == n <= 105 * items[i].length == 2 * items[i][0] == profiti * items[i][1] == categoryi * 1 <= profiti <= 109 * 1 <= categoryi <= n * 1 <= k <= n
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法和双指针方法来找到最大优雅度。

算法步骤:
1. 按照利润从高到低对项目进行排序。
2. 选择前 k 个项目，计算其总利润和不同类别的数量。
3. 如果存在重复类别，使用双指针方法替换重复类别项目，以增加不同类别的数量，从而提高优雅度。

关键点:
- 按利润排序后，优先选择利润高的项目。
- 使用双指针方法替换重复类别项目，以增加不同类别的数量。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是 items 的长度。排序操作的时间复杂度为 O(n log n)。
空间复杂度: O(n)，用于存储排序后的项目和类别集合。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def find_max_elegance(items: List[List[int]], k: int) -> int:
    """
    函数式接口 - 实现最优解法
    """
    # 按利润从高到低排序
    items.sort(key=lambda x: -x[0])
    
    # 选择前 k 个项目
    selected = items[:k]
    total_profit = sum(item[0] for item in selected)
    categories = set(item[1] for item in selected)
    distinct_categories = len(categories)
    
    # 计算初始优雅度
    max_elegance = total_profit + distinct_categories ** 2
    
    # 使用双指针方法替换重复类别项目
    j = k
    for i in range(k):
        if selected[i][1] in categories:
            while j < len(items) and items[j][1] in categories:
                j += 1
            if j == len(items):
                break
            # 替换重复类别项目
            total_profit -= selected[i][0]
            total_profit += items[j][0]
            categories.remove(selected[i][1])
            categories.add(items[j][1])
            distinct_categories = len(categories)
            max_elegance = max(max_elegance, total_profit + distinct_categories ** 2)
            j += 1
    
    return max_elegance


Solution = create_solution(find_max_elegance)