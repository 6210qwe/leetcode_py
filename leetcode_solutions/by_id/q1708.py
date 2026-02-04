# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1708
标题: Design Parking System
难度: easy
链接: https://leetcode.cn/problems/design-parking-system/
题目类型: 设计、计数、模拟
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1603. 设计停车系统 - 请你给一个停车场设计一个停车系统。停车场总共有三种不同大小的车位：大，中和小，每种尺寸分别有固定数目的车位。 请你实现 ParkingSystem 类： * ParkingSystem(int big, int medium, int small) 初始化 ParkingSystem 类，三个参数分别对应每种停车位的数目。 * bool addCar(int carType) 检查是否有 carType 对应的停车位。 carType 有三种类型：大，中，小，分别用数字 1， 2 和 3 表示。一辆车只能停在 carType 对应尺寸的停车位中。如果没有空车位，请返回 false ，否则将该车停入车位并返回 true 。 示例 1： 输入： ["ParkingSystem", "addCar", "addCar", "addCar", "addCar"] [[1, 1, 0], [1], [2], [3], [1]] 输出： [null, true, true, false, false] 解释： ParkingSystem parkingSystem = new ParkingSystem(1, 1, 0); parkingSystem.addCar(1); // 返回 true ，因为有 1 个空的大车位 parkingSystem.addCar(2); // 返回 true ，因为有 1 个空的中车位 parkingSystem.addCar(3); // 返回 false ，因为没有空的小车位 parkingSystem.addCar(1); // 返回 false ，因为没有空的大车位，唯一一个大车位已经被占据了 提示： * 0 <= big, medium, small <= 1000 * carType 取值为 1， 2 或 3 * 最多会调用 addCar 函数 1000 次
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用一个列表来存储每种车位的数量，并根据 carType 来更新相应的车位数量。

算法步骤:
1. 初始化 ParkingSystem 类时，将大、中、小车位的数量存储在一个列表中。
2. 在 addCar 方法中，检查对应的车位数量是否大于 0，如果是，则减少一个车位并返回 True；否则返回 False。

关键点:
- 使用列表来简化对不同车位数量的管理。
- 根据 carType 直接索引到对应的车位数量。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.slots = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.slots[carType - 1] > 0:
            self.slots[carType - 1] -= 1
            return True
        return False


Solution = create_solution(ParkingSystem)