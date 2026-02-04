# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3942
标题: Find Drivers with Improved Fuel Efficiency
难度: medium
链接: https://leetcode.cn/problems/find-drivers-with-improved-fuel-efficiency/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3601. 寻找燃油效率提升的驾驶员 - 表：drivers +-------------+---------+ | Column Name | Type | +-------------+---------+ | driver_id | int | | driver_name | varchar | +-------------+---------+ driver_id 是这张表的唯一主键。 每一行都包含一个司机的信息。 表：trips +---------------+---------+ | Column Name | Type | +---------------+---------+ | trip_id | int | | driver_id | int | | trip_date | date | | distance_km | decimal | | fuel_consumed | decimal | +---------------+---------+ trip_id 是这张表的唯一主键。 每一行表示一名司机完成的一次行程，包括该次行程行驶的距离和消耗的燃油量。 编写一个解决方案，通过 比较 司机在 上半年 和 下半年 的 平均燃油效率 来找出 燃油效率有所提高 的司机。 * 通过 distance_km / fuel_consumed 计算 每次 行程的 燃油效率。 * 上半年：一月到六月，下半年：七月到十二月 * 只包含在上半年和下半年都有行程的司机 * 通过（second_half_avg - first_half_avg）计算 提升效率。 * 将所有结果 四舍五入 到小数点后 2 位 返回结果表按提升效率 降序 排列，然后按司机姓名 升序 排列。 结果格式如下所示。 示例： 输入： drivers 表： +-----------+---------------+ | driver_id | driver_name | +-----------+---------------+ | 1 | Alice Johnson | | 2 | Bob Smith | | 3 | Carol Davis | | 4 | David Wilson | | 5 | Emma Brown | +-----------+---------------+ trips 表： +---------+-----------+------------+-------------+---------------+ | trip_id | driver_id | trip_date | distance_km | fuel_consumed | +---------+-----------+------------+-------------+---------------+ | 1 | 1 | 2023-02-15 | 120.5 | 10.2 | | 2 | 1 | 2023-03-20 | 200.0 | 16.5 | | 3 | 1 | 2023-08-10 | 150.0 | 11.0 | | 4 | 1 | 2023-09-25 | 180.0 | 12.5 | | 5 | 2 | 2023-01-10 | 100.0 | 9.0 | | 6 | 2 | 2023-04-15 | 250.0 | 22.0 | | 7 | 2 | 2023-10-05 | 200.0 | 15.0 | | 8 | 3 | 2023-03-12 | 80.0 | 8.5 | | 9 | 3 | 2023-05-18 | 90.0 | 9.2 | | 10 | 4 | 2023-07-22 | 160.0 | 12.8 | | 11 | 4 | 2023-11-30 | 140.0 | 11.0 | | 12 | 5 | 2023-02-28 | 110.0 | 11.5 | +---------+-----------+------------+-------------+---------------+ 输出： +-----------+---------------+------------------+-------------------+------------------------+ | driver_id | driver_name | first_half_avg | second_half_avg | efficiency_improvement | +-----------+---------------+------------------+-------------------+------------------------+ | 2 | Bob Smith | 11.24 | 13.33 | 2.10 | | 1 | Alice Johnson | 11.97 | 14.02 | 2.05 | +-----------+---------------+------------------+-------------------+------------------------+ 解释： * Alice Johnson (driver_id = 1): * 上半年行程（一月到六月）：Feb 15 (120.5/10.2 = 11.81), Mar 20 (200.0/16.5 = 12.12) * 上半年平均效率：(11.81 + 12.12) / 2 = 11.97 * 下半年行程（七月到十二月）：Aug 10 (150.0/11.0 = 13.64), Sep 25 (180.0/12.5 = 14.40) * 下半年平均效率：(13.64 + 14.40) / 2 = 14.02 * 效率提升：14.02 - 11.97 = 2.05 * Bob Smith (driver_id = 2): * 上半年行程：Jan 10 (100.0/9.0 = 11.11), Apr 15 (250.0/22.0 = 11.36) * 上半年平均效率：(11.11 + 11.36) / 2 = 11.24 * 下半年行程：Oct 5 (200.0/15.0 = 13.33) * 下半年平均效率：13.33 * 效率提升：13.33 - 11.24 = 2.10（舍入到 2 位小数） * 未包含的司机： * Carol Davis (driver_id = 3)：只有上半年的行程（三月，五月） * David Wilson (driver_id = 4)：只有下半年的行程（七月，十一月） * Emma Brown (driver_id = 5)：只有上半年的行程（二月） 输出表按提升效率降序排列，然后按司机名字升序排列。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来计算每个司机在上半年和下半年的平均燃油效率，并找出燃油效率有所提高的司机。

算法步骤:
1. 计算每个司机在上半年和下半年的平均燃油效率。
2. 过滤出在上半年和下半年都有行程的司机。
3. 计算每个司机的燃油效率提升。
4. 将结果四舍五入到小数点后两位。
5. 按照提升效率降序排列，然后按司机姓名升序排列。

关键点:
- 使用子查询和聚合函数来计算平均燃油效率。
- 使用条件过滤来确保只包含在上半年和下半年都有行程的司机。
- 使用四舍五入函数来处理结果。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是 trips 表中的行数。主要的时间开销在于排序操作。
空间复杂度: O(n)，需要存储中间结果。
"""

# ============================================================================
# 代码实现
# ============================================================================

def solution_function_name(drivers, trips):
    """
    函数式接口 - 实现最优解法
    """
    import pandas as pd

    # 将输入数据转换为 DataFrame
    drivers_df = pd.DataFrame(drivers)
    trips_df = pd.DataFrame(trips)

    # 计算每次行程的燃油效率
    trips_df['efficiency'] = trips_df['distance_km'] / trips_df['fuel_consumed']

    # 计算上半年和下半年的平均燃油效率
    first_half_avg = trips_df[trips_df['trip_date'].dt.month <= 6].groupby('driver_id')['efficiency'].mean().reset_index(name='first_half_avg')
    second_half_avg = trips_df[trips_df['trip_date'].dt.month >= 7].groupby('driver_id')['efficiency'].mean().reset_index(name='second_half_avg')

    # 合并上半年和下半年的平均燃油效率
    merged_avg = pd.merge(first_half_avg, second_half_avg, on='driver_id', how='inner')

    # 计算燃油效率提升
    merged_avg['efficiency_improvement'] = (merged_avg['second_half_avg'] - merged_avg['first_half_avg']).round(2)

    # 过滤出燃油效率提升的司机
    improved_drivers = merged_avg[merged_avg['efficiency_improvement'] > 0]

    # 合并司机信息
    result = pd.merge(improved_drivers, drivers_df, on='driver_id', how='left')

    # 按照提升效率降序排列，然后按司机姓名升序排列
    result = result.sort_values(by=['efficiency_improvement', 'driver_name'], ascending=[False, True])

    # 选择输出列
    result = result[['driver_id', 'driver_name', 'first_half_avg', 'second_half_avg', 'efficiency_improvement']]

    return result.to_dict(orient='records')


Solution = create_solution(solution_function_name)