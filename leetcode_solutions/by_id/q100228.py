# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100228
标题: Animal Shelter LCCI
难度: easy
链接: https://leetcode.cn/problems/animal-shelter-lcci/
题目类型: 设计、队列
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
面试题 03.06. 动物收容所 - 动物收容所。有家动物收容所只收容狗与猫，且严格遵守“先进先出”的原则。在收养该收容所的动物时，收养人只能收养所有动物中“最老”（由其进入收容所的时间长短而定）的动物，或者可以挑选猫或狗（同时必须收养此类动物中“最老”的）。换言之，收养人不能自由挑选想收养的对象。请创建适用于这个系统的数据结构，实现各种操作方法，比如enqueue、dequeueAny、dequeueDog和dequeueCat。允许使用Java内置的LinkedList数据结构。 enqueue方法有一个animal参数，animal[0]代表动物编号，animal[1]代表动物种类，其中 0 代表猫，1 代表狗。 dequeue*方法返回一个列表[动物编号, 动物种类]，若没有可以收养的动物，则返回[-1,-1]。 示例 1： 输入： ["AnimalShelf", "enqueue", "enqueue", "dequeueCat", "dequeueDog", "dequeueAny"] [[], [[0, 0]], [[1, 0]], [], [], []] 输出： [null,null,null,[0,0],[-1,-1],[1,0]] 示例 2： 输入： ["AnimalShelf", "enqueue", "enqueue", "enqueue", "dequeueDog", "dequeueCat", "dequeueAny"] [[], [[0, 0]], [[1, 0]], [[2, 1]], [], [], []] 输出： [null,null,null,null,[2,1],[0,0],[1,0]] 说明: 1. 收纳所的最大容量为20000
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用两个队列分别存储猫和狗，每个队列中的元素包含动物编号和进入时间戳。通过比较时间戳来确保先进先出的原则。

算法步骤:
1. 初始化两个队列，分别用于存储猫和狗。
2. 在enqueue操作中，将动物加入相应的队列，并记录进入时间戳。
3. 在dequeueAny操作中，比较两个队列的头部元素的时间戳，返回时间戳较小的动物。
4. 在dequeueDog和dequeueCat操作中，直接从相应的队列中取出并返回头部元素。

关键点:
- 使用两个队列分别存储猫和狗，确保先进先出的原则。
- 通过时间戳来比较不同队列中的动物，确保dequeueAny操作的正确性。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - 每个操作的时间复杂度都是常数级别。
空间复杂度: O(n) - 空间复杂度取决于存储的动物数量。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


class AnimalShelf:

    def __init__(self):
        self.cats = []
        self.dogs = []
        self.timestamp = 0

    def enqueue(self, animal: List[int]) -> None:
        self.timestamp += 1
        if animal[1] == 0:  # 猫
            self.cats.append((animal[0], self.timestamp))
        else:  # 狗
            self.dogs.append((animal[0], self.timestamp))

    def dequeueAny(self) -> List[int]:
        if not self.cats and not self.dogs:
            return [-1, -1]
        if not self.cats:
            return self.dequeueDog()
        if not self.dogs:
            return self.dequeueCat()
        if self.cats[0][1] < self.dogs[0][1]:
            return self.dequeueCat()
        else:
            return self.dequeueDog()

    def dequeueDog(self) -> List[int]:
        if not self.dogs:
            return [-1, -1]
        animal = self.dogs.pop(0)
        return [animal[0], 1]

    def dequeueCat(self) -> List[int]:
        if not self.cats:
            return [-1, -1]
        animal = self.cats.pop(0)
        return [animal[0], 0]


Solution = create_solution(AnimalShelf)