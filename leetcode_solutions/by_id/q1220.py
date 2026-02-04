# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1220
标题: Smallest Sufficient Team
难度: hard
链接: https://leetcode.cn/problems/smallest-sufficient-team/
题目类型: 位运算、数组、动态规划、状态压缩
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1125. 最小的必要团队 - 作为项目经理，你规划了一份需求的技能清单 req_skills，并打算从备选人员名单 people 中选出些人组成一个「必要团队」（ 编号为 i 的备选人员 people[i] 含有一份该备选人员掌握的技能列表）。 所谓「必要团队」，就是在这个团队中，对于所需求的技能列表 req_skills 中列出的每项技能，团队中至少有一名成员已经掌握。可以用每个人的编号来表示团队中的成员： * 例如，团队 team = [0, 1, 3] 表示掌握技能分别为 people[0]，people[1]，和 people[3] 的备选人员。 请你返回 任一 规模最小的必要团队，团队成员用人员编号表示。你可以按 任意顺序 返回答案，题目数据保证答案存在。 示例 1： 输入：req_skills = ["java","nodejs","reactjs"], people = [["java"],["nodejs"],["nodejs","reactjs"]] 输出：[0,2] 示例 2： 输入：req_skills = ["algorithms","math","java","reactjs","csharp","aws"], people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]] 输出：[1,2] 提示： * 1 <= req_skills.length <= 16 * 1 <= req_skills[i].length <= 16 * req_skills[i] 由小写英文字母组成 * req_skills 中的所有字符串 互不相同 * 1 <= people.length <= 60 * 0 <= people[i].length <= 16 * 1 <= people[i][j].length <= 16 * people[i][j] 由小写英文字母组成 * people[i] 中的所有字符串 互不相同 * people[i] 中的每个技能是 req_skills 中的技能 * 题目数据保证「必要团队」一定存在
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划和位运算来解决这个问题。

算法步骤:
1. 将每个技能映射到一个唯一的整数。
2. 使用一个掩码来表示每个人掌握的技能集合。
3. 使用动态规划来找到最小的团队，使得所有技能都被覆盖。

关键点:
- 使用位运算来表示技能集合。
- 动态规划的状态转移方程。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(2^n * m)，其中 n 是 req_skills 的长度，m 是 people 的长度。
空间复杂度: O(2^n * n)，用于存储动态规划的状态。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def smallestSufficientTeam(req_skills: List[str], people: List[List[str]]) -> List[int]:
    n = len(req_skills)
    skill_to_id = {skill: i for i, skill in enumerate(req_skills)}
    
    # 将每个人的技能列表转换为位掩码
    people_masks = []
    for person in people:
        mask = 0
        for skill in person:
            if skill in skill_to_id:
                mask |= 1 << skill_to_id[skill]
        people_masks.append(mask)
    
    # 动态规划数组
    dp = [(float('inf'), [])] * (1 << n)
    dp[0] = (0, [])
    
    for i, mask in enumerate(people_masks):
        for j in range((1 << n) - 1, -1, -1):
            new_mask = j | mask
            if dp[new_mask][0] > dp[j][0] + 1:
                dp[new_mask] = (dp[j][0] + 1, dp[j][1] + [i])
    
    return dp[(1 << n) - 1][1]

Solution = create_solution(smallestSufficientTeam)