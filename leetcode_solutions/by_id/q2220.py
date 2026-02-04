# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2220
标题: Find All Possible Recipes from Given Supplies
难度: medium
链接: https://leetcode.cn/problems/find-all-possible-recipes-from-given-supplies/
题目类型: 图、拓扑排序、数组、哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2115. 从给定原材料中找到所有可以做出的菜 - 你有 n 道不同菜的信息。给你一个字符串数组 recipes 和一个二维字符串数组 ingredients 。第 i 道菜的名字为 recipes[i] ，如果你有它 所有 的原材料 ingredients[i] ，那么你可以 做出 这道菜。一份食谱也可以是 其它 食谱的原料，也就是说 ingredients[i] 可能包含 recipes 中另一个字符串。 同时给你一个字符串数组 supplies ，它包含你初始时拥有的所有原材料，每一种原材料你都有无限多。 请你返回你可以做出的所有菜。你可以以 任意顺序 返回它们。 注意两道菜在它们的原材料中可能互相包含。 示例 1： 输入：recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"] 输出：["bread"] 解释： 我们可以做出 "bread" ，因为我们有原材料 "yeast" 和 "flour" 。 示例 2： 输入：recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"] 输出：["bread","sandwich"] 解释： 我们可以做出 "bread" ，因为我们有原材料 "yeast" 和 "flour" 。 我们可以做出 "sandwich" ，因为我们有原材料 "meat" 且可以做出原材料 "bread" 。 示例 3： 输入：recipes = ["bread","sandwich","burger"], ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies = ["yeast","flour","meat"] 输出：["bread","sandwich","burger"] 解释： 我们可以做出 "bread" ，因为我们有原材料 "yeast" 和 "flour" 。 我们可以做出 "sandwich" ，因为我们有原材料 "meat" 且可以做出原材料 "bread" 。 我们可以做出 "burger" ，因为我们有原材料 "meat" 且可以做出原材料 "bread" 和 "sandwich" 。 示例 4： 输入：recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast"] 输出：[] 解释： 我们没法做出任何菜，因为我们只有原材料 "yeast" 。 提示： * n == recipes.length == ingredients.length * 1 <= n <= 100 * 1 <= ingredients[i].length, supplies.length <= 100 * 1 <= recipes[i].length, ingredients[i][j].length, supplies[k].length <= 10 * recipes[i], ingredients[i][j] 和 supplies[k] 只包含小写英文字母。 * 所有 recipes 和 supplies 中的值互不相同。 * ingredients[i] 中的字符串互不相同。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用拓扑排序来解决这个问题。我们将每个菜视为一个节点，如果一个菜需要另一个菜作为原料，则在这两个节点之间建立一条边。然后我们使用拓扑排序来确定哪些菜可以制作。

算法步骤:
1. 构建图和入度表。
2. 初始化队列，将所有初始原材料加入队列。
3. 使用广度优先搜索进行拓扑排序，更新入度表并处理可以制作的菜。
4. 返回可以制作的所有菜。

关键点:
- 使用拓扑排序来处理依赖关系。
- 使用队列进行广度优先搜索。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是 recipes 的长度，m 是 ingredients 的总长度。
空间复杂度: O(n + m)，用于存储图和入度表。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def find_all_recipes(recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
    """
    函数式接口 - 找出所有可以制作的菜
    """
    from collections import defaultdict, deque
    
    # 构建图和入度表
    graph = defaultdict(list)
    in_degree = {recipe: 0 for recipe in recipes}
    
    # 构建图和入度表
    for i, ingredient_list in enumerate(ingredients):
        for ingredient in ingredient_list:
            if ingredient in in_degree:
                graph[ingredient].append(recipes[i])
                in_degree[recipes[i]] += 1
    
    # 初始化队列
    queue = deque(supplies)
    can_make = []
    
    # 拓扑排序
    while queue:
        supply = queue.popleft()
        if supply in in_degree:
            can_make.append(supply)
        
        for neighbor in graph[supply]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return [recipe for recipe in recipes if in_degree[recipe] == 0]


Solution = create_solution(find_all_recipes)