# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2429
标题: Design a Food Rating System
难度: medium
链接: https://leetcode.cn/problems/design-a-food-rating-system/
题目类型: 设计、数组、哈希表、字符串、有序集合、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2353. 设计食物评分系统 - 设计一个支持下述操作的食物评分系统： * 修改 系统中列出的某种食物的评分。 * 返回系统中某一类烹饪方式下评分最高的食物。 实现 FoodRatings 类： * FoodRatings(String[] foods, String[] cuisines, int[] ratings) 初始化系统。食物由 foods、cuisines 和 ratings 描述，长度均为 n 。 * foods[i] 是第 i 种食物的名字。 * cuisines[i] 是第 i 种食物的烹饪方式。 * ratings[i] 是第 i 种食物的最初评分。 * void changeRating(String food, int newRating) 修改名字为 food 的食物的评分。 * String highestRated(String cuisine) 返回指定烹饪方式 cuisine 下评分最高的食物的名字。如果存在并列，返回 字典序较小 的名字。 注意，字符串 x 的字典序比字符串 y 更小的前提是：x 在字典中出现的位置在 y 之前，也就是说，要么 x 是 y 的前缀，或者在满足 x[i] != y[i] 的第一个位置 i 处，x[i] 在字母表中出现的位置在 y[i] 之前。 示例： 输入 ["FoodRatings", "highestRated", "highestRated", "changeRating", "highestRated", "changeRating", "highestRated"] [[["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]], ["korean"], ["japanese"], ["sushi", 16], ["japanese"], ["ramen", 16], ["japanese"]] 输出 [null, "kimchi", "ramen", null, "sushi", null, "ramen"] 解释 FoodRatings foodRatings = new FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]); foodRatings.highestRated("korean"); // 返回 "kimchi" // "kimchi" 是分数最高的韩式料理，评分为 9 。 foodRatings.highestRated("japanese"); // 返回 "ramen" // "ramen" 是分数最高的日式料理，评分为 14 。 foodRatings.changeRating("sushi", 16); // "sushi" 现在评分变更为 16 。 foodRatings.highestRated("japanese"); // 返回 "sushi" // "sushi" 是分数最高的日式料理，评分为 16 。 foodRatings.changeRating("ramen", 16); // "ramen" 现在评分变更为 16 。 foodRatings.highestRated("japanese"); // 返回 "ramen" // "sushi" 和 "ramen" 的评分都是 16 。 // 但是，"ramen" 的字典序比 "sushi" 更小。 提示： * 1 <= n <= 2 * 104 * n == foods.length == cuisines.length == ratings.length * 1 <= foods[i].length, cuisines[i].length <= 10 * foods[i]、cuisines[i] 由小写英文字母组成 * 1 <= ratings[i] <= 108 * foods 中的所有字符串 互不相同 * 在对 changeRating 的所有调用中，food 是系统中食物的名字。 * 在对 highestRated 的所有调用中，cuisine 是系统中 至少一种 食物的烹饪方式。 * 最多调用 changeRating 和 highestRated 总计 2 * 104 次
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: [TODO]

算法步骤:
1. [TODO]
2. [TODO]

关键点:
- [TODO]
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O([TODO])
空间复杂度: O([TODO])
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(params):
    """
    函数式接口 - [TODO] 实现
    """
    # TODO: 实现最优解法
    pass


Solution = create_solution(solution_function_name)
