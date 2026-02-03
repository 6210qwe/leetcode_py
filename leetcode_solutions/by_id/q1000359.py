# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000359
标题: 环形闯关游戏
难度: hard
链接: https://leetcode.cn/problems/K8GULz/
题目类型: 位运算、并查集、数组、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCP 49. 环形闯关游戏 - 「力扣挑战赛」中有一个由 `N` 个关卡组成的**环形**闯关游戏，
关卡编号为 `0`~`N-1`，编号 `0` 的关卡和编号 `N-1` 的关卡相邻。每个关卡均有积分要求，
`challenge[i]` 表示挑战编号 `i` 的关卡最少需要拥有的积分。 
![图片.png](https://pic.leetcode.cn/1630392170-ucncVS-%E5%9B%BE%E7%89%87.png){:width="240px"} 
小扣想要挑战关卡，闯关具体规则如下： - 初始小扣可以指定其中一个关卡为「开启」状态，
其余关卡将处于「未开启」状态。 - 小扣可以挑战处于「开启」状态且**满足最少积分要求**的关卡，
若小扣挑战该关卡前积分为 `score`，挑战结束后，积分将增长为 `score|challenge[i]`
（即位运算中的 `"OR"` 运算） - 在挑战某个关卡后，该关卡两侧相邻的关卡将会开启（若之前未开启）
 请帮助小扣进行计算，初始最少需要多少积分，可以挑战 **环形闯关游戏** 的所有关卡。 
 **示例1：** > 输入：`challenge = [5,4,6,2,7]` > > 输出：`4` > > 解释： 
 初始选择编号 3 的关卡开启，积分为 4 >挑战编号 3 的关卡，积分变为 $4 | 2 = 6$，开启 2、4 处的关卡 
 >挑战编号 2 的关卡，积分变为 $6 | 6 = 6$，开启 1 处的关卡 >挑战编号 1 的关卡，积分变为 $6 | 4 = 6$，
 开启 0 处的关卡 >挑战编号 0 的关卡，积分变为 $6 | 5 = 7$ >挑战编号 4 的关卡，顺利完成全部的关卡 
 **示例2：** > 输入：`challenge = [12,7,11,3,9]` > > 输出：`8` > > 解释： 初始选择编号 3 的关卡开启，积分为 8 >挑战编号 3 的关卡，积分变为 $8 | 3 = 11$，开启 2、4 处的关卡 >挑战编号 2 的关卡，积分变为 $11 | 11 = 11$，开启 1 处的关卡 >挑战编号 4 的关卡，积分变为 $11 | 9 = 11$，开启 0 处的关卡 >挑战编号 1 的关卡，积分变为 $11 | 7 = 15$ >挑战编号 0 的关卡，顺利完成全部的关卡 **示例3：** > 输入：`challenge = [1,1,1]` > > 输出：`1` **提示：** - `1 <= challenge.length <= 5*10^4` - `1 <= challenge[i] <= 10^14`
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 贪心+位运算，找到最优起始点和挑战顺序

算法步骤:
1. 枚举所有可能的起始关卡
2. 使用贪心策略，每次选择当前可挑战且要求最低的关卡
3. 使用位运算更新积分
4. 找到所有起始点中需要的最小初始积分

关键点:
- 贪心选择策略
- 位运算优化
- 时间复杂度O(n^2)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2) - n为关卡数
空间复杂度: O(n) - 存储状态
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def ring_game(challenge: List[int]) -> int:
    """
    函数式接口 - 环形闯关游戏
    
    实现思路:
    枚举起始点，使用贪心策略选择挑战顺序。
    
    Args:
        challenge: 每个关卡的最少积分要求
        
    Returns:
        初始最少需要的积分
        
    Example:
        >>> ring_game([5,4,6,2,7])
        4
    """
    n = len(challenge)
    min_score = float('inf')
    
    # 枚举所有可能的起始关卡
    for start in range(n):
        score = challenge[start]  # 初始积分至少等于起始关卡要求
        opened = [False] * n
        opened[start] = True
        visited = [False] * n
        
        # 贪心选择：每次选择可挑战且要求最低的关卡
        while True:
            # 找到所有可挑战的关卡
            candidates = []
            for i in range(n):
                if opened[i] and not visited[i] and score >= challenge[i]:
                    candidates.append((challenge[i], i))
            
            if not candidates:
                break
            
            # 选择要求最低的关卡
            candidates.sort()
            _, chosen = candidates[0]
            
            # 挑战该关卡
            score |= challenge[chosen]
            visited[chosen] = True
            
            # 开启相邻关卡
            left = (chosen - 1 + n) % n
            right = (chosen + 1) % n
            opened[left] = True
            opened[right] = True
        
        # 检查是否所有关卡都被挑战
        if all(visited):
            # 尝试找到更小的初始积分
            # 使用二分查找或直接枚举可能的初始积分
            min_initial = challenge[start]
            for initial in range(challenge[start], score + 1):
                if (initial | challenge[start]) >= challenge[start]:
                    test_score = initial | challenge[start]
                    test_opened = [False] * n
                    test_opened[start] = True
                    test_visited = [False] * n
                    
                    while True:
                        test_candidates = []
                        for i in range(n):
                            if test_opened[i] and not test_visited[i] and test_score >= challenge[i]:
                                test_candidates.append((challenge[i], i))
                        
                        if not test_candidates:
                            break
                        
                        test_candidates.sort()
                        _, test_chosen = test_candidates[0]
                        test_score |= challenge[test_chosen]
                        test_visited[test_chosen] = True
                        
                        test_left = (test_chosen - 1 + n) % n
                        test_right = (test_chosen + 1) % n
                        test_opened[test_left] = True
                        test_opened[test_right] = True
                    
                    if all(test_visited):
                        min_initial = min(min_initial, initial)
                        break
            
            min_score = min(min_score, min_initial)
    
    return min_score


Solution = create_solution(ring_game)
