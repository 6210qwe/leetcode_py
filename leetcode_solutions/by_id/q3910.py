# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3910
标题: Find Books with No Available Copies
难度: easy
链接: https://leetcode.cn/problems/find-books-with-no-available-copies/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3570. 查找无可用副本的书籍 - 表：library_books +------------------+---------+ | Column Name | Type | +------------------+---------+ | book_id | int | | title | varchar | | author | varchar | | genre | varchar | | publication_year | int | | total_copies | int | +------------------+---------+ book_id 是这张表的唯一主键。 每一行包含图书馆中一本书的信息，包括图书馆拥有的副本总数。 表：borrowing_records +---------------+---------+ | Column Name | Type | +---------------+---------+ | record_id | int | | book_id | int | | borrower_name | varchar | | borrow_date | date | | return_date | date | +---------------+---------+ record_id 是这张表的唯一主键。 每一行代表一笔借阅交易并且如果这本书目前被借出并且还没有被归还，return_date 为 NULL。 编写一个解决方案以找到 所有 当前被借出（未归还） 且图书馆中 无可用副本 的书籍。 * 如果存在一条借阅记录，其 return_date 为 NULL，那么这本书被认为 当前是借出的。 返回结果表按当前借阅者数量 降序 排列，然后按书名 升序 排列。 结果格式如下所示。 示例： 输入： library_books 表： +---------+------------------------+------------------+----------+------------------+--------------+ | book_id | title | author | genre | publication_year | total_copies | +---------+------------------------+------------------+----------+------------------+--------------+ | 1 | The Great Gatsby | F. Scott | Fiction | 1925 | 3 | | 2 | To Kill a Mockingbird | Harper Lee | Fiction | 1960 | 3 | | 3 | 1984 | George Orwell | Dystopian| 1949 | 1 | | 4 | Pride and Prejudice | Jane Austen | Romance | 1813 | 2 | | 5 | The Catcher in the Rye | J.D. Salinger | Fiction | 1951 | 1 | | 6 | Brave New World | Aldous Huxley | Dystopian| 1932 | 4 | +---------+------------------------+------------------+----------+------------------+--------------+ borrowing_records 表： +-----------+---------+---------------+-------------+-------------+ | record_id | book_id | borrower_name | borrow_date | return_date | +-----------+---------+---------------+-------------+-------------+ | 1 | 1 | Alice Smith | 2024-01-15 | NULL | | 2 | 1 | Bob Johnson | 2024-01-20 | NULL | | 3 | 2 | Carol White | 2024-01-10 | 2024-01-25 | | 4 | 3 | David Brown | 2024-02-01 | NULL | | 5 | 4 | Emma Wilson | 2024-01-05 | NULL | | 6 | 5 | Frank Davis | 2024-01-18 | 2024-02-10 | | 7 | 1 | Grace Miller | 2024-02-05 | NULL | | 8 | 6 | Henry Taylor | 2024-01-12 | NULL | | 9 | 2 | Ivan Clark | 2024-02-12 | NULL | | 10 | 2 | Jane Adams | 2024-02-15 | NULL | +-----------+---------+---------------+-------------+-------------+ 输出： +---------+------------------+---------------+-----------+------------------+-------------------+ | book_id | title | author | genre | publication_year | current_borrowers | +---------+------------------+---------------+-----------+------------------+-------------------+ | 1 | The Great Gatsby | F. Scott | Fiction | 1925 | 3 | | 3 | 1984 | George Orwell | Dystopian | 1949 | 1 | +---------+------------------+---------------+-----------+------------------+-------------------+ 解释： * The Great Gatsby (book_id = 1)： * 总副本数：3 * 当前被 Alice Smith，Bob Johnson 和 Grace Miller 借阅（3 名借阅者） * 可用副本数：3 - 3 = 0 * 因为 available_copies = 0，所以被包含 * 1984 (book_id = 3): * 总副本数：1 * 当前被 David Brown 借阅（1 名借阅者） * 可用副本数：1 - 1 = 0 * 因为 available_copies = 0，所以被包含 * 未被包含的书： * To Kill a Mockingbird (book_id = 2)：总副本数 = 3，当前借阅者 = 2，可用副本 = 1 * Pride and Prejudice (book_id = 4)：总副本数 = 2，当前借阅者 = 1，可用副本 = 1 * The Catcher in the Rye (book_id = 5)：总副本数 = 1，当前借阅者 = 0，可用副本 = 1 * Brave New World (book_id = 6)：总副本数 = 4，当前借阅者 = 1，可用副本 = 3 * 结果顺序： * The Great Gatsby 有 3 名当前借阅者，排序第一 * 1984 有 1 名当前借阅者，排序第二 输出表以 current_borrowers 降序排序，然后以 book_title 升序排序。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想:
1. 计算每本书当前被借阅的数量。
2. 计算每本书的可用副本数。
3. 筛选出当前被借阅且无可用副本的书籍。
4. 按当前借阅者数量降序排列，然后按书名升序排列。

算法步骤:
1. 使用子查询计算每本书当前被借阅的数量。
2. 将 `library_books` 表与子查询结果进行连接，计算每本书的可用副本数。
3. 筛选出当前被借阅且无可用副本的书籍。
4. 对结果进行排序。

关键点:
- 使用子查询和连接操作来计算每本书的当前借阅数量和可用副本数。
- 使用 `GROUP BY` 和 `COUNT` 来统计每本书的当前借阅数量。
- 使用 `LEFT JOIN` 来处理可能没有借阅记录的书籍。
- 使用 `ORDER BY` 进行排序。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是 `borrowing_records` 表中的记录数。主要的时间开销在于排序操作。
空间复杂度: O(n)，用于存储中间结果和最终结果。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(library_books, borrowing_records):
    """
    函数式接口 - 查找无可用副本的书籍
    """
    # 计算每本书当前被借阅的数量
    current_borrowers_subquery = (
        borrowing_records
        .filter(borrowing_records.return_date.is_(None))
        .group_by(borrowing_records.book_id)
        .count()
        .alias("current_borrowers")
    )

    # 将 library_books 表与子查询结果进行连接，计算每本书的可用副本数
    query = (
        library_books
        .join(current_borrowers_subquery, library_books.book_id == current_borrowers_subquery.c.book_id, isouter=True)
        .with_entities(
            library_books.book_id,
            library_books.title,
            library_books.author,
            library_books.genre,
            library_books.publication_year,
            (current_borrowers_subquery.c.current_borrowers).label("current_borrowers"),
            (library_books.total_copies - current_borrowers_subquery.c.current_borrowers).label("available_copies")
        )
        .filter((library_books.total_copies - current_borrowers_subquery.c.current_borrowers) == 0)
        .order_by(current_borrowers_subquery.c.current_borrowers.desc(), library_books.title.asc())
    )

    return query.all()


Solution = create_solution(solution_function_name)