# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1272
标题: Invalid Transactions
难度: medium
链接: https://leetcode.cn/problems/invalid-transactions/
题目类型: 数组、哈希表、字符串、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1169. 查询无效交易 - 如果出现下述两种情况，交易 可能无效：
* 交易金额超过 $1000
* 或者，它和 另一个城市 中 同名 的另一笔交易相隔不超过 60 分钟（包含 60 分钟整）

给定字符串数组交易清单 transaction 。每个交易字符串 transactions[i] 由一些用逗号分隔的值组成，这些值分别表示交易的名称，时间（以分钟计），金额以及城市。
返回 transactions，返回可能无效的交易列表。你可以按 任何顺序 返回答案。

示例 1：
输入：transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
输出：["alice,20,800,mtv","alice,50,100,beijing"]
解释：第一笔交易是无效的，因为第二笔交易和它间隔不超过 60 分钟、名称相同且发生在不同的城市。同样，第二笔交易也是无效的。

示例 2：
输入：transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
输出：["alice,50,1200,mtv"]

示例 3：
输入：transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
输出：["bob,50,1200,mtv"]

提示：
* transactions.length <= 1000
* 每笔交易 transactions[i] 按 "{name},{time},{amount},{city}" 的格式进行记录
* 每个交易名称 {name} 和城市 {city} 都由小写英文字母组成，长度在 1 到 10 之间
* 每个交易时间 {time} 由一些数字组成，表示一个 0 到 1000 之间的整数
* 每笔交易金额 {amount} 由一些数字组成，表示一个 0 到 2000 之间的整数
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想:
1. 使用字典来存储每个用户的所有交易记录，键为用户名，值为该用户的交易列表。
2. 对每个用户的交易列表按时间排序。
3. 遍历每个用户的交易列表，检查每笔交易是否满足无效条件：
   - 交易金额超过 $1000
   - 与同一用户在其他城市的交易时间间隔不超过 60 分钟

算法步骤:
1. 初始化一个字典 `user_transactions` 来存储每个用户的交易记录。
2. 解析每个交易字符串，将其转换为元组 (name, time, amount, city) 并存入 `user_transactions`。
3. 对每个用户的交易列表按时间排序。
4. 遍历每个用户的交易列表，检查每笔交易是否无效，并将无效交易添加到结果列表中。

关键点:
- 使用字典和排序来高效地处理交易记录。
- 通过双指针或滑动窗口来检查时间间隔不超过 60 分钟的交易。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是 transactions 的长度。排序操作的时间复杂度为 O(n log n)，遍历操作的时间复杂度为 O(n)。
空间复杂度: O(n)，用于存储每个用户的交易记录。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(transactions: List[str]) -> List[str]:
    """
    函数式接口 - 实现最优解法
    """
    user_transactions = {}
    
    # 解析交易记录并存储到字典中
    for transaction in transactions:
        name, time, amount, city = transaction.split(',')
        time, amount = int(time), int(amount)
        if name not in user_transactions:
            user_transactions[name] = []
        user_transactions[name].append((name, time, amount, city))
    
    invalid_transactions = []
    
    # 对每个用户的交易记录按时间排序
    for name, trans in user_transactions.items():
        trans.sort(key=lambda x: x[1])
        
        # 检查每笔交易是否无效
        for i in range(len(trans)):
            _, time_i, amount_i, city_i = trans[i]
            if amount_i > 1000:
                invalid_transactions.append(','.join(map(str, trans[i])))
                continue
            
            for j in range(i + 1, len(trans)):
                _, time_j, _, city_j = trans[j]
                if time_j - time_i > 60:
                    break
                if city_i != city_j:
                    invalid_transactions.append(','.join(map(str, trans[i])))
                    invalid_transactions.append(','.join(map(str, trans[j])))
                    break
    
    return list(set(invalid_transactions))  # 去重


Solution = create_solution(solution_function_name)