# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 4103
标题: Find Churn Risk Customers
难度: medium
链接: https://leetcode.cn/problems/find-churn-risk-customers/
题目类型: 其他
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3716. 寻找流失风险客户 - 表：subscription_events +------------------+---------+ | Column Name | Type | +------------------+---------+ | event_id | int | | user_id | int | | event_date | date | | event_type | varchar | | plan_name | varchar | | monthly_amount | decimal | +------------------+---------+ event_id 是这张表的唯一主键。 event_type 可以是 start，upgrade，downgrade 或 cancel。 plan_name 可以是 basic，standard，premium 或 NULL（当 event_type 是 cancel）。 monthly_amount 表示此次事件后的月度订阅费用。 对于 cancel 的事件，monthly_amount 为 0。 编写一个解决方案来 寻找流失风险用户 - 出现预流失信号的用户。如果用户符合以下所有条件，则被视为 有流失风险 的客户： * 目前有 有效的订阅（他们的最后事件不是 cancel）。 * 已在其订阅历史中 至少进行过一次 降级。 * 他们 目前的订阅费用 低于历史最高订阅费用的 50%。 * 已订阅 至少 60 天。 返回结果表按 days_as_subscriber 降序 排序，然后按 user_id 升序 排序。 结果格式如下所示。 示例： 输入： subscription_events 表： +----------+---------+------------+------------+-----------+----------------+ | event_id | user_id | event_date | event_type | plan_name | monthly_amount | +----------+---------+------------+------------+-----------+----------------+ | 1 | 501 | 2024-01-01 | start | premium | 29.99 | | 2 | 501 | 2024-02-15 | downgrade | standard | 19.99 | | 3 | 501 | 2024-03-20 | downgrade | basic | 9.99 | | 4 | 502 | 2024-01-05 | start | standard | 19.99 | | 5 | 502 | 2024-02-10 | upgrade | premium | 29.99 | | 6 | 502 | 2024-03-15 | downgrade | basic | 9.99 | | 7 | 503 | 2024-01-10 | start | basic | 9.99 | | 8 | 503 | 2024-02-20 | upgrade | standard | 19.99 | | 9 | 503 | 2024-03-25 | upgrade | premium | 29.99 | | 10 | 504 | 2024-01-15 | start | premium | 29.99 | | 11 | 504 | 2024-03-01 | downgrade | standard | 19.99 | | 12 | 504 | 2024-03-30 | cancel | NULL | 0.00 | | 13 | 505 | 2024-02-01 | start | basic | 9.99 | | 14 | 505 | 2024-02-28 | upgrade | standard | 19.99 | | 15 | 506 | 2024-01-20 | start | premium | 29.99 | | 16 | 506 | 2024-03-10 | downgrade | basic | 9.99 | +----------+---------+------------+------------+-----------+----------------+ 输出： +----------+--------------+------------------------+-----------------------+--------------------+ | user_id | current_plan | current_monthly_amount | max_historical_amount | days_as_subscriber | +----------+--------------+------------------------+-----------------------+--------------------+ | 501 | basic | 9.99 | 29.99 | 79 | | 502 | basic | 9.99 | 29.99 | 69 | +----------+--------------+------------------------+-----------------------+--------------------+ 解释： * 用户 501： * 当前订阅有效：最近一次事件是降级到基础（未取消） * 有降级记录：是，历史上有 2 次降级 * 当前订阅（9.99）vs 最大订阅（29.99）：9.99/29.99 = 33.3%（少于 50%） * 订阅天数：1 月 1 日到 3 月 20 日 = 79 天（至少 60 天） * 结果：流失风险客户 * 用户 502： * 当前订阅有效：最近一次事件是降级到基础（未取消） * 有降级记录：是，历史上有 1 次降级 * 当前订阅（9.99）vs 最大订阅（29.99）：9.99/29.99 = 33.3%（少于 50%） * 订阅天数：1 月 5 日到 5 月 15 日 = 70 天（至少 60 天） * 结果：流失风险客户 * 用户 503： * 当前订阅有效：最近一次事件是升级到高级（未取消） * 有降级记录：历史上没有降级 * 结果：无风险客户（没有降级历史） * 用户 504： * 当前订阅有效：最近一次事件是取消 * 结果：无风险客户（已取消订阅） * 用户 505： * 当前订阅有效：最近一次事件是升级到标准（未取消） * 有降级记录：历史上没有降级 * 结果：无风险客户（没有降级历史） * 用户 506： * 当前订阅有效：最近一次事件是降级到标准（未取消） * 有降级记录：是，历史上有 1 次降级 * 当前订阅（9.99）vs 最大订阅（29.99）：9.99/29.99 = 33.3%（少于 50%） * 订阅天数：1 月 20 日到 5 月 10 日 = 50 天（少于 60 天） * 结果：无风险客户（订阅时长不足） 结果表按 days_as_subscriber 降序排序，然后按 user_id 升序排序。 注意：days_as_subscriber 按照每个用户的第一个事件日期到最后一个事件日期进行计算。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想:
1. 通过聚合操作获取每个用户的当前订阅状态、最大历史订阅费用和降级次数。
2. 过滤出符合条件的用户：当前订阅有效、有降级记录、当前订阅费用低于历史最高订阅费用的 50%、订阅天数至少 60 天。

算法步骤:
1. 获取每个用户的当前订阅状态、最大历史订阅费用和降级次数。
2. 计算每个用户的订阅天数。
3. 过滤出符合条件的用户。
4. 按 days_as_subscriber 降序排序，然后按 user_id 升序排序。

关键点:
- 使用 Pandas 进行数据处理和聚合操作。
- 通过条件过滤和排序实现最终结果。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是 subscription_events 表的行数。主要的时间开销在于排序操作。
空间复杂度: O(n)，需要存储中间结果和最终结果。
"""

# ============================================================================
# 代码实现
# ============================================================================

import pandas as pd

def find_churn_risk_customers(subscription_events: pd.DataFrame) -> pd.DataFrame:
    # 获取每个用户的当前订阅状态
    current_subscription = subscription_events.sort_values(by=['user_id', 'event_date']).groupby('user_id').tail(1)
    
    # 获取每个用户的最大历史订阅费用
    max_historical_amount = subscription_events.groupby('user_id')['monthly_amount'].max().reset_index()
    
    # 获取每个用户的降级次数
    downgrade_count = subscription_events[subscription_events['event_type'] == 'downgrade'].groupby('user_id').size().reset_index(name='downgrade_count')
    
    # 合并当前订阅状态、最大历史订阅费用和降级次数
    merged_data = pd.merge(current_subscription, max_historical_amount, on='user_id')
    merged_data = pd.merge(merged_data, downgrade_count, on='user_id', how='left').fillna(0)
    
    # 计算每个用户的订阅天数
    merged_data['days_as_subscriber'] = (merged_data['event_date'] - subscription_events.groupby('user_id')['event_date'].min()).dt.days
    
    # 过滤出符合条件的用户
    churn_risk_customers = merged_data[
        (merged_data['event_type'] != 'cancel') &
        (merged_data['downgrade_count'] > 0) &
        (merged_data['monthly_amount'] < 0.5 * merged_data['monthly_amount_y']) &
        (merged_data['days_as_subscriber'] >= 60)
    ]
    
    # 选择需要的列并排序
    result = churn_risk_customers[['user_id', 'plan_name', 'monthly_amount_x', 'monthly_amount_y', 'days_as_subscriber']].rename(columns={
        'plan_name': 'current_plan',
        'monthly_amount_x': 'current_monthly_amount',
        'monthly_amount_y': 'max_historical_amount'
    })
    
    return result.sort_values(by=['days_as_subscriber', 'user_id'], ascending=[False, True])

Solution = create_solution(find_churn_risk_customers)