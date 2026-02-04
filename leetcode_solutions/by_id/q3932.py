# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3932
标题: Find COVID Recovery Patients
难度: medium
链接: https://leetcode.cn/problems/find-covid-recovery-patients/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3586. 寻找 COVID 康复患者 - 表：patients +-------------+---------+ | Column Name | Type | +-------------+---------+ | patient_id | int | | patient_name| varchar | | age | int | +-------------+---------+ patient_id 是这张表的唯一主键。 每一行表示一个患者的信息。 表：covid_tests +-------------+---------+ | Column Name | Type | +-------------+---------+ | test_id | int | | patient_id | int | | test_date | date | | result | varchar | +-------------+---------+ test_id 是这张表的唯一主键。 每一行代表一个 COVID 检测结果。结果可以是阳性、阴性或不确定。 编写一个解决方案以找到从 COVID 中康复的患者——那些曾经检测呈阳性但后来检测呈阴性的患者。 * 患者如果 至少有一次阳性 检测结果后，在 之后的日期 至少有一次 阴性 检测结果，则被认为已康复。 * 计算从 首次阳性检测 结果到 该阳性检测 后的 首次阴性检测结果 之间的 康复时间（以天为单位） * 仅包括 同时具有阳性及阴性检测结果的患者 返回结果表以 recovery_time 升序 排序，然后以 patient_name 升序 排序。 结果格式如下所示。 示例： 输入： patients 表： +------------+--------------+-----+ | patient_id | patient_name | age | +------------+--------------+-----+ | 1 | Alice Smith | 28 | | 2 | Bob Johnson | 35 | | 3 | Carol Davis | 42 | | 4 | David Wilson | 31 | | 5 | Emma Brown | 29 | +------------+--------------+-----+ covid_tests 表： +---------+------------+------------+--------------+ | test_id | patient_id | test_date | result | +---------+------------+------------+--------------+ | 1 | 1 | 2023-01-15 | Positive | | 2 | 1 | 2023-01-25 | Negative | | 3 | 2 | 2023-02-01 | Positive | | 4 | 2 | 2023-02-05 | Inconclusive | | 5 | 2 | 2023-02-12 | Negative | | 6 | 3 | 2023-01-20 | Negative | | 7 | 3 | 2023-02-10 | Positive | | 8 | 3 | 2023-02-20 | Negative | | 9 | 4 | 2023-01-10 | Positive | | 10 | 4 | 2023-01-18 | Positive | | 11 | 5 | 2023-02-15 | Negative | | 12 | 5 | 2023-02-20 | Negative | +---------+------------+------------+--------------+ 输出： +------------+--------------+-----+---------------+ | patient_id | patient_name | age | recovery_time | +------------+--------------+-----+---------------+ | 1 | Alice Smith | 28 | 10 | | 3 | Carol Davis | 42 | 10 | | 2 | Bob Johnson | 35 | 11 | +------------+--------------+-----+---------------+ 解释： * Alice Smith (patient_id = 1): * 首次阳性检测：2023-01-15 * 阳性检测后的首次阴性检测：2023-01-25 * 康复时间：25 - 15 = 10 天 * Bob Johnson (patient_id = 2): * 首次阳性检测：2023-02-01 * 测试结果不明确：2023-02-05（忽略计算康复时间） * 阳性检测后的首次阴性检测：2023-02-12 * 康复时间：12 - 1 = 11 天 * Carol Davis (patient_id = 3): * 检测呈阴性：2023-01-20（在阳性检测前） * 首次阳性检测：2023-02-10 * 阳性检测后的首次阴性检测：2023-02-20 * 康复时间：20 - 10 = 10 天 * 没有包含的患者： * David Wilson（patient_id = 4）：只有阳性检测，之后没有阴性检测。 * Emma Brown（patient_id = 5）：只有阴性检测，从未有阳性检测。 输出表以 recovery_time 升序排序，然后以 patient_name 升序排序。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想:
1. 找出每个患者的首次阳性检测日期和首次阴性检测日期。
2. 计算从首次阳性检测到首次阴性检测之间的天数。
3. 过滤出同时具有阳性及阴性检测结果的患者，并按要求排序。

算法步骤:
1. 使用子查询找出每个患者的首次阳性检测日期。
2. 使用子查询找出每个患者的首次阴性检测日期。
3. 将两个子查询的结果进行连接，计算康复时间。
4. 过滤出康复时间大于0的患者。
5. 按照康复时间和患者姓名进行排序。

关键点:
- 使用窗口函数 `MIN` 和 `CASE` 来找出每个患者的首次阳性检测日期和首次阴性检测日期。
- 使用 `DATEDIFF` 函数计算康复时间。
- 使用 `JOIN` 将两个子查询的结果进行连接。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是 covid_tests 表中的行数。主要的时间开销在于排序操作。
空间复杂度: O(n)，需要存储中间结果。
"""

# ============================================================================
# 代码实现
# ============================================================================

def solution_function_name(patients, covid_tests):
    """
    函数式接口 - 找出从 COVID 中康复的患者
    """
    # 找出每个患者的首次阳性检测日期
    first_positive_query = """
    SELECT
        patient_id,
        MIN(test_date) AS first_positive_date
    FROM
        (SELECT
            patient_id,
            test_date,
            CASE
                WHEN result = 'Positive' THEN 1
                ELSE 0
            END AS is_positive
        FROM
            covid_tests) AS subquery
    WHERE
        is_positive = 1
    GROUP BY
        patient_id
    """

    # 找出每个患者的首次阴性检测日期
    first_negative_query = """
    SELECT
        patient_id,
        MIN(test_date) AS first_negative_date
    FROM
        (SELECT
            patient_id,
            test_date,
            CASE
                WHEN result = 'Negative' THEN 1
                ELSE 0
            END AS is_negative
        FROM
            covid_tests) AS subquery
    WHERE
        is_negative = 1
    GROUP BY
        patient_id
    """

    # 将两个子查询的结果进行连接，计算康复时间
    final_query = f"""
    SELECT
        p.patient_id,
        p.patient_name,
        p.age,
        DATEDIFF(n.first_negative_date, p.first_positive_date) AS recovery_time
    FROM
        ({first_positive_query}) AS p
    JOIN
        ({first_negative_query}) AS n
    ON
        p.patient_id = n.patient_id
    WHERE
        n.first_negative_date > p.first_positive_date
    ORDER BY
        recovery_time ASC, p.patient_name ASC
    """

    # 执行最终查询
    return final_query

Solution = create_solution(solution_function_name)