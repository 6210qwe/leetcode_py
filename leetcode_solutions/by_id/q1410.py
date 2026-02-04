# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1410
标题: Traffic Light Controlled Intersection
难度: easy
链接: https://leetcode.cn/problems/traffic-light-controlled-intersection/
题目类型: 多线程
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1279. 红绿灯路口 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用信号量来控制红绿灯的切换，确保在同一时间只有一个方向的车辆可以通过。

算法步骤:
1. 初始化两个信号量，一个用于控制南北方向的交通，另一个用于控制东西方向的交通。
2. 在每个方向的车辆通过时，先获取对应的信号量，然后释放另一个方向的信号量。
3. 通过这种方式，确保同一时间只有一个方向的车辆可以通过。

关键点:
- 使用 `threading.Semaphore` 来控制并发访问。
- 确保信号量的正确释放和获取，避免死锁。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - 每个方向的车辆通过时，信号量的获取和释放操作都是常数时间。
空间复杂度: O(1) - 只使用了固定的额外空间来存储信号量。
"""

# ============================================================================
# 代码实现
# ============================================================================

import threading
from typing import Callable
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

class TrafficLight:
    def __init__(self):
        self.north_south = threading.Semaphore(1)
        self.east_west = threading.Semaphore(0)

    def carArrived(
        self,
        carId: int,                      # ID of the car
        roadId: int,                     # ID of the road the car travels on. Can be 1 (road A) or 2 (road B)
        direction: int,                  # Direction of the car
        turnGreen: Callable[[], None],   # Use turnGreen() to turn light to green on current road
        crossCar: Callable[[], None]     # Use crossCar() to make car cross the intersection
    ) -> None:
        if roadId == 1:
            self.north_south.acquire()
            turnGreen()
            crossCar()
            self.east_west.release()
        else:
            self.east_west.acquire()
            turnGreen()
            crossCar()
            self.north_south.release()

Solution = create_solution(TrafficLight)