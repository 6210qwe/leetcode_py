# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3891
标题: Find Category Recommendation Pairs
难度: hard
链接: https://leetcode.cn/problems/find-category-recommendation-pairs/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3554. 查找类别推荐对 - 表：ProductPurchases +-------------+------+ | Column Name | Type | +-------------+------+ | user_id | int | | product_id | int | | quantity | int | +-------------+------+ (user_id, product_id) 是这张表的唯一主键。 每一行代表用户以特定数量购买的一种产品。 表：ProductInfo +-------------+---------+ | Column Name | Type | +-------------+---------+ | product_id | int | | category | varchar | | price | decimal | +-------------+---------+ product_id 是这张表的唯一主键。 每一行表示一件商品的类别和价格。 亚马逊想要了解不同产品类别的购物模式。编写一个解决方案： 1. 查找所有 类别对（其中 category1 < category2） 2. 对于 每个类别对，确定 同时 购买了两类别产品的 不同用户 数量 如果至少有 3 个不同的客户购买了两个类别的产品，则类别对被视为 可报告的。 返回可报告类别对的结果表以 customer_count 降序 排序，并且为了防止排序持平，以 category1 字典序 升序 排序，然后以 category2 升序 排序。 结果格式如下所示。 示例： 输入： ProductPurchases 表： +---------+------------+----------+ | user_id | product_id | quantity | +---------+------------+----------+ | 1 | 101 | 2 | | 1 | 102 | 1 | | 1 | 201 | 3 | | 1 | 301 | 1 | | 2 | 101 | 1 | | 2 | 102 | 2 | | 2 | 103 | 1 | | 2 | 201 | 5 | | 3 | 101 | 2 | | 3 | 103 | 1 | | 3 | 301 | 4 | | 3 | 401 | 2 | | 4 | 101 | 1 | | 4 | 201 | 3 | | 4 | 301 | 1 | | 4 | 401 | 2 | | 5 | 102 | 2 | | 5 | 103 | 1 | | 5 | 201 | 2 | | 5 | 202 | 3 | +---------+------------+----------+ ProductInfo 表： +------------+-------------+-------+ | product_id | category | price | +------------+-------------+-------+ | 101 | Electronics | 100 | | 102 | Books | 20 | | 103 | Books | 35 | | 201 | Clothing | 45 | | 202 | Clothing | 60 | | 301 | Sports | 75 | | 401 | Kitchen | 50 | +------------+-------------+-------+ 输出： +-------------+-------------+----------------+ | category1 | category2 | customer_count | +-------------+-------------+----------------+ | Books | Clothing | 3 | | Books | Electronics | 3 | | Clothing | Electronics | 3 | | Electronics | Sports | 3 | +-------------+-------------+----------------+ 解释： * Books-Clothing: * 用户 1 购买来自 Books (102) 和 Clothing (201) 的商品 * 用户 2 购买来自 Books (102, 103) 和 Clothing (201) 的商品 * 用户 5 购买来自 Books (102, 103) 和 Clothing (201, 202) 的商品 * 共计：3 个用户购买同一类别的商品 * Books-Electronics: * 用户 1 购买来自 Books (102) 和 Electronics (101) 的商品 * 用户 2 购买来自 Books (102, 103) 和 Electronics (101) 的商品 * 用户 3 购买来自 Books (103) 和 Electronics (101) 的商品 * 共计：3 个消费者购买同一类别的商品 * Clothing-Electronics: * 用户 1 购买来自 Clothing (201) 和 Electronics (101) 的商品 * 用户 2 购买来自 Clothing (201) 和 Electronics (101) 的商品 * 用户 4 购买来自 Clothing (201) 和 Electronics (101) 的商品 * 共计：3 个消费者购买同一类别的商品 * Electronics-Sports: * 用户 1 购买来自 Electronics (101) 和 Sports (301) 的商品 * 用户 3 购买来自 Electronics (101) 和 Sports (301) 的商品 * 用户 4 购买来自 Electronics (101) 和 Sports (301) 的商品 * 共计：3 个消费者购买同一类别的商品 * 其它类别对比如 Clothing-Sports（只有 2 个消费者：用户 1 和 4）和 Books-Kitchen（只有 1 个消费者：用户 3）共同的消费者少于 3 个，因此不包含在结果内。 结果按 customer_count 降序排列。由于所有对都有相同的客户数量 3，它们按 category1（然后是 category2）升序排列。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想:
1. 将 ProductPurchases 和 ProductInfo 表进行连接，获取每个用户的购买记录及其对应的类别。
2. 使用自连接的方式，生成所有可能的类别对 (category1, category2)，并计算每个类别对中同时购买两个类别的不同用户数量。
3. 过滤出至少有 3 个不同用户购买的类别对。
4. 按照 customer_count 降序、category1 和 category2 升序排序。

算法步骤:
1. 将 ProductPurchases 和 ProductInfo 表进行连接，获取每个用户的购买记录及其对应的类别。
2. 使用自连接的方式，生成所有可能的类别对 (category1, category2)，并计算每个类别对中同时购买两个类别的不同用户数量。
3. 过滤出至少有 3 个不同用户购买的类别对。
4. 按照 customer_count 降序、category1 和 category2 升序排序。

关键点:
- 使用 SQL 查询来高效地处理数据连接和过滤操作。
- 使用自连接和聚合函数来计算每个类别对的用户数量。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2)，其中 n 是 ProductPurchases 表中的行数。主要的时间消耗在于自连接操作。
空间复杂度: O(n)，存储中间结果和最终结果所需的空间。
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
    函数式接口 - 实现
    """
    # SQL 查询实现
    query = """
    WITH UserCategory AS (
        SELECT pp.user_id, pi.category
        FROM ProductPurchases pp
        JOIN ProductInfo pi ON pp.product_id = pi.product_id
    ),
    CategoryPairs AS (
        SELECT uc1.category AS category1, uc2.category AS category2, COUNT(DISTINCT uc1.user_id) AS customer_count
        FROM UserCategory uc1
        JOIN UserCategory uc2 ON uc1.user_id = uc2.user_id AND uc1.category < uc2.category
        GROUP BY uc1.category, uc2.category
    )
    SELECT category1, category2, customer_count
    FROM CategoryPairs
    WHERE customer_count >= 3
    ORDER BY customer_count DESC, category1 ASC, category2 ASC
    """
    return query


Solution = create_solution(solution_function_name)