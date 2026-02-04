# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1533
标题: Display Table of Food Orders in a Restaurant
难度: medium
链接: https://leetcode.cn/problems/display-table-of-food-orders-in-a-restaurant/
题目类型: 数组、哈希表、字符串、有序集合、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1418. 点菜展示表 - 给你一个数组 orders，表示客户在餐厅中完成的订单，确切地说， orders[i]=[customerNamei,tableNumberi,foodItemi] ，其中 customerNamei 是客户的姓名，tableNumberi 是客户所在餐桌的桌号，而 foodItemi 是客户点的餐品名称。 请你返回该餐厅的 点菜展示表 。在这张表中，表中第一行为标题，其第一列为餐桌桌号 “Table” ，后面每一列都是按字母顺序排列的餐品名称。接下来每一行中的项则表示每张餐桌订购的相应餐品数量，第一列应当填对应的桌号，后面依次填写下单的餐品数量。 注意：客户姓名不是点菜展示表的一部分。此外，表中的数据行应该按餐桌桌号升序排列。 示例 1： 输入：orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]] 输出：[["Table","Beef Burrito","Ceviche","Fried Chicken","Water"],["3","0","2","1","0"],["5","0","1","0","1"],["10","1","0","0","0"]] 解释： 点菜展示表如下所示： Table,Beef Burrito,Ceviche,Fried Chicken,Water 3 ,0 ,2 ,1 ,0 5 ,0 ,1 ,0 ,1 10 ,1 ,0 ,0 ,0 对于餐桌 3：David 点了 "Ceviche" 和 "Fried Chicken"，而 Rous 点了 "Ceviche" 而餐桌 5：Carla 点了 "Water" 和 "Ceviche" 餐桌 10：Corina 点了 "Beef Burrito" 示例 2： 输入：orders = [["James","12","Fried Chicken"],["Ratesh","12","Fried Chicken"],["Amadeus","12","Fried Chicken"],["Adam","1","Canadian Waffles"],["Brianna","1","Canadian Waffles"]] 输出：[["Table","Canadian Waffles","Fried Chicken"],["1","2","0"],["12","0","3"]] 解释： 对于餐桌 1：Adam 和 Brianna 都点了 "Canadian Waffles" 而餐桌 12：James, Ratesh 和 Amadeus 都点了 "Fried Chicken" 示例 3： 输入：orders = [["Laura","2","Bean Burrito"],["Jhon","2","Beef Burrito"],["Melissa","2","Soda"]] 输出：[["Table","Bean Burrito","Beef Burrito","Soda"],["2","1","1","1"]] 提示： * 1 <= orders.length <= 5 * 10^4 * orders[i].length == 3 * 1 <= customerNamei.length, foodItemi.length <= 20 * customerNamei 和 foodItemi 由大小写英文字母及空格字符 ' ' 组成。 * tableNumberi 是 1 到 500 范围内的整数。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用两个字典来分别记录每个餐桌的订单和所有出现过的餐品。

算法步骤:
1. 初始化两个字典：`table_orders` 用于记录每个餐桌的订单，`all_foods` 用于记录所有出现过的餐品。
2. 遍历 `orders`，更新 `table_orders` 和 `all_foods`。
3. 获取 `all_foods` 的排序列表作为表头。
4. 遍历 `table_orders`，构建每张餐桌的订单行，并按桌号排序。
5. 将表头和订单行组合成最终结果。

关键点:
- 使用字典进行高效统计。
- 使用排序确保表头和订单行的顺序。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m log m)，其中 n 是 `orders` 的长度，m 是不同餐品的数量。遍历 `orders` 是 O(n)，排序是 O(m log m)。
空间复杂度: O(n + m)，存储 `table_orders` 和 `all_foods`。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def display_table(orders: List[List[str]]) -> List[List[str]]:
    """
    函数式接口 - 返回餐厅的点菜展示表
    """
    # 初始化字典
    table_orders = {}
    all_foods = set()

    # 遍历 orders，更新 table_orders 和 all_foods
    for _, table, food in orders:
        if table not in table_orders:
            table_orders[table] = {}
        if food not in table_orders[table]:
            table_orders[table][food] = 0
        table_orders[table][food] += 1
        all_foods.add(food)

    # 获取 all_foods 的排序列表作为表头
    header = sorted(all_foods)
    result = [["Table"] + header]

    # 遍历 table_orders，构建每张餐桌的订单行，并按桌号排序
    for table in sorted(table_orders.keys(), key=int):
        row = [table]
        for food in header:
            row.append(str(table_orders[table].get(food, 0)))
        result.append(row)

    return result


Solution = create_solution(display_table)