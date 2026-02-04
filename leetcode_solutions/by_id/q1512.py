# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1512
标题: Design Underground System
难度: medium
链接: https://leetcode.cn/problems/design-underground-system/
题目类型: 设计、哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1396. 设计地铁系统 - 地铁系统跟踪不同车站之间的乘客出行时间，并使用这一数据来计算从一站到另一站的平均时间。 实现 UndergroundSystem 类： * void checkIn(int id, string stationName, int t) * 通行卡 ID 等于 id 的乘客，在时间 t ，从 stationName 站进入 * 乘客一次只能从一个站进入 * void checkOut(int id, string stationName, int t) * 通行卡 ID 等于 id 的乘客，在时间 t ，从 stationName 站离开 * double getAverageTime(string startStation, string endStation) * 返回从 startStation 站到 endStation 站的平均时间 * 平均时间会根据截至目前所有从 startStation 站 直接 到达 endStation 站的行程进行计算，也就是从 startStation 站进入并从 endStation 离开的行程 * 从 startStation 到 endStation 的行程时间与从 endStation 到 startStation 的行程时间可能不同 * 在调用 getAverageTime 之前，至少有一名乘客从 startStation 站到达 endStation 站 你可以假设对 checkIn 和 checkOut 方法的所有调用都是符合逻辑的。如果一名乘客在时间 t1 进站、时间 t2 出站，那么 t1 < t2 。所有时间都按时间顺序发生。 示例 1： 输入 ["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime","getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"] [[],[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],["Paradise","Cambridge"],["Leyton","Waterloo"],[10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],["Leyton","Waterloo"]] 输出 [null,null,null,null,null,null,null,14.00000,11.00000,null,11.00000,null,12.00000] 解释 UndergroundSystem undergroundSystem = new UndergroundSystem(); undergroundSystem.checkIn(45, "Leyton", 3); undergroundSystem.checkIn(32, "Paradise", 8); undergroundSystem.checkIn(27, "Leyton", 10); undergroundSystem.checkOut(45, "Waterloo", 15); // 乘客 45 "Leyton" -> "Waterloo" ，用时 15-3 = 12 undergroundSystem.checkOut(27, "Waterloo", 20); // 乘客 27 "Leyton" -> "Waterloo" ，用时 20-10 = 10 undergroundSystem.checkOut(32, "Cambridge", 22); // 乘客 32 "Paradise" -> "Cambridge" ，用时 22-8 = 14 undergroundSystem.getAverageTime("Paradise", "Cambridge"); // 返回 14.00000 。只有一个 "Paradise" -> "Cambridge" 的行程，(14) / 1 = 14 undergroundSystem.getAverageTime("Leyton", "Waterloo"); // 返回 11.00000 。有两个 "Leyton" -> "Waterloo" 的行程，(10 + 12) / 2 = 11 undergroundSystem.checkIn(10, "Leyton", 24); undergroundSystem.getAverageTime("Leyton", "Waterloo"); // 返回 11.00000 undergroundSystem.checkOut(10, "Waterloo", 38); // 乘客 10 "Leyton" -> "Waterloo" ，用时 38-24 = 14 undergroundSystem.getAverageTime("Leyton", "Waterloo"); // 返回 12.00000 。有三个 "Leyton" -> "Waterloo" 的行程，(10 + 12 + 14) / 3 = 12 示例 2： 输入 ["UndergroundSystem","checkIn","checkOut","getAverageTime","checkIn","checkOut","getAverageTime","checkIn","checkOut","getAverageTime"] [[],[10,"Leyton",3],[10,"Paradise",8],["Leyton","Paradise"],[5,"Leyton",10],[5,"Paradise",16],["Leyton","Paradise"],[2,"Leyton",21],[2,"Paradise",30],["Leyton","Paradise"]] 输出 [null,null,null,5.00000,null,null,5.50000,null,null,6.66667] 解释 UndergroundSystem undergroundSystem = new UndergroundSystem(); undergroundSystem.checkIn(10, "Leyton", 3); undergroundSystem.checkOut(10, "Paradise", 8); // 乘客 10 "Leyton" -> "Paradise" ，用时 8-3 = 5 undergroundSystem.getAverageTime("Leyton", "Paradise"); // 返回 5.00000 ，(5) / 1 = 5 undergroundSystem.checkIn(5, "Leyton", 10); undergroundSystem.checkOut(5, "Paradise", 16); // 乘客 5 "Leyton" -> "Paradise" ，用时 16-10 = 6 undergroundSystem.getAverageTime("Leyton", "Paradise"); // 返回 5.50000 ，(5 + 6) / 2 = 5.5 undergroundSystem.checkIn(2, "Leyton", 21); undergroundSystem.checkOut(2, "Paradise", 30); // 乘客 2 "Leyton" -> "Paradise" ，用时 30-21 = 9 undergroundSystem.getAverageTime("Leyton", "Paradise"); // 返回 6.66667 ，(5 + 6 + 9) / 3 = 6.66667 提示： * 1 <= id, t <= 106 * 1 <= stationName.length, startStation.length, endStation.length <= 10 * 所有字符串由大小写英文字母与数字组成 * 总共最多调用 checkIn、checkOut 和 getAverageTime 方法 2 * 104 次 * 与标准答案误差在 10-5 以内的结果都被视为正确结果
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想:
- 使用两个字典来分别存储每个乘客的进站信息和每条路线的总时间和旅行次数。

算法步骤:
1. 初始化两个字典：`check_ins` 用于存储每个乘客的进站信息（包括进站名称和时间），`route_times` 用于存储每条路线的总时间和旅行次数。
2. `checkIn` 方法：将乘客的进站信息存储在 `check_ins` 字典中。
3. `checkOut` 方法：计算乘客的旅行时间，并更新 `route_times` 字典中的总时间和旅行次数。
4. `getAverageTime` 方法：根据 `route_times` 字典中的总时间和旅行次数计算平均时间。

关键点:
- 使用哈希表来存储和更新乘客的进站信息和路线的总时间和旅行次数，以实现高效的查询和更新操作。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1)
- `checkIn`、`checkOut` 和 `getAverageTime` 方法的时间复杂度均为 O(1)，因为它们只涉及字典的插入、更新和查询操作。

空间复杂度: O(P + R)
- `P` 是乘客数量，`R` 是不同的路线数量。`check_ins` 字典的空间复杂度为 O(P)，`route_times` 字典的空间复杂度为 O(R)。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Dict, Tuple

class UndergroundSystem:
    def __init__(self):
        self.check_ins: Dict[int, Tuple[str, int]] = {}
        self.route_times: Dict[Tuple[str, str], Tuple[int, int]] = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_ins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.check_ins.pop(id)
        route = (start_station, stationName)
        if route not in self.route_times:
            self.route_times[route] = (0, 0)
        total_time, count = self.route_times[route]
        self.route_times[route] = (total_time + t - start_time, count + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, count = self.route_times[(startStation, endStation)]
        return total_time / count


Solution = create_solution(UndergroundSystem)