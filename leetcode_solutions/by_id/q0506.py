# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 506
标题: Relative Ranks
难度: easy
链接: https://leetcode.cn/problems/relative-ranks/
题目类型: 数组、排序、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
506. 相对名次 - 给你一个长度为 n 的整数数组 score ，其中 score[i] 是第 i 位运动员在比赛中的得分。所有得分都 互不相同 。 运动员将根据得分 决定名次 ，其中名次第 1 的运动员得分最高，名次第 2 的运动员得分第 2 高，依此类推。运动员的名次决定了他们的获奖情况： * 名次第 1 的运动员获金牌 "Gold Medal" 。 * 名次第 2 的运动员获银牌 "Silver Medal" 。 * 名次第 3 的运动员获铜牌 "Bronze Medal" 。 * 从名次第 4 到第 n 的运动员，只能获得他们的名次编号（即，名次第 x 的运动员获得编号 "x"）。 使用长度为 n 的数组 answer 返回获奖，其中 answer[i] 是第 i 位运动员的获奖情况。 示例 1： 输入：score = [5,4,3,2,1] 输出：["Gold Medal","Silver Medal","Bronze Medal","4","5"] 解释：名次为 [1st, 2nd, 3rd, 4th, 5th] 。 示例 2： 输入：score = [10,3,8,9,4] 输出：["Gold Medal","5","Bronze Medal","Silver Medal","4"] 解释：名次为 [1st, 5th, 3rd, 2nd, 4th] 。 提示： * n == score.length * 1 <= n <= 104 * 0 <= score[i] <= 106 * score 中的所有值 互不相同
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 对分数进行降序排序，然后根据排序后的索引分配名次。

算法步骤:
1. 将分数和原始索引配对。
2. 按分数降序排序。
3. 根据排序后的索引分配名次。
4. 构建结果数组。

关键点:
- 使用元组 (分数, 原始索引) 来保持分数和索引的对应关系。
- 排序后直接分配名次，前三名特殊处理。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n) - 主要由排序操作决定。
空间复杂度: O(n) - 需要额外的空间来存储分数和索引的配对。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def find_relative_ranks(score: List[int]) -> List[str]:
    """
    函数式接口 - 找到相对名次
    """
    n = len(score)
    if n == 0:
        return []

    # 将分数和原始索引配对
    score_with_index = [(s, i) for i, s in enumerate(score)]
    
    # 按分数降序排序
    sorted_score_with_index = sorted(score_with_index, key=lambda x: x[0], reverse=True)
    
    # 初始化结果数组
    result = [""] * n
    
    # 分配名次
    for rank, (s, i) in enumerate(sorted_score_with_index):
        if rank == 0:
            result[i] = "Gold Medal"
        elif rank == 1:
            result[i] = "Silver Medal"
        elif rank == 2:
            result[i] = "Bronze Medal"
        else:
            result[i] = str(rank + 1)
    
    return result


Solution = create_solution(find_relative_ranks)