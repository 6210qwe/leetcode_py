# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2169
标题: Simple Bank System
难度: medium
链接: https://leetcode.cn/problems/simple-bank-system/
题目类型: 设计、数组、哈希表、模拟
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2043. 简易银行系统 - 你的任务是为一个很受欢迎的银行设计一款程序，以自动化执行所有传入的交易（转账，存款和取款）。银行共有 n 个账户，编号从 1 到 n 。每个账号的初始余额存储在一个下标从 0 开始的整数数组 balance 中，其中第 (i + 1) 个账户的初始余额是 balance[i] 。 请你执行所有 有效的 交易。如果满足下面全部条件，则交易 有效 ： * 指定的账户编号在 1 和 n 之间，且 * 取款或者转账需要的钱的总数 小于或者等于 账户余额。 实现 Bank 类： * Bank(long[] balance) 使用下标从 0 开始的整数数组 balance 初始化该对象。 * boolean transfer(int account1, int account2, long money) 从编号为 account1 的账户向编号为 account2 的账户转帐 money 美元。如果交易成功，返回 true ，否则，返回 false 。 * boolean deposit(int account, long money) 向编号为 account 的账户存款 money 美元。如果交易成功，返回 true ；否则，返回 false 。 * boolean withdraw(int account, long money) 从编号为 account 的账户取款 money 美元。如果交易成功，返回 true ；否则，返回 false 。 示例： 输入： ["Bank", "withdraw", "transfer", "deposit", "transfer", "withdraw"] [[[10, 100, 20, 50, 30]], [3, 10], [5, 1, 20], [5, 20], [3, 4, 15], [10, 50]] 输出： [null, true, true, true, false, false] 解释： Bank bank = new Bank([10, 100, 20, 50, 30]); bank.withdraw(3, 10); // 返回 true ，账户 3 的余额是 $20 ，所以可以取款 $10 。 // 账户 3 余额为 $20 - $10 = $10 。 bank.transfer(5, 1, 20); // 返回 true ，账户 5 的余额是 $30 ，所以可以转账 $20 。 // 账户 5 的余额为 $30 - $20 = $10 ，账户 1 的余额为 $10 + $20 = $30 。 bank.deposit(5, 20); // 返回 true ，可以向账户 5 存款 $20 。 // 账户 5 的余额为 $10 + $20 = $30 。 bank.transfer(3, 4, 15); // 返回 false ，账户 3 的当前余额是 $10 。 // 所以无法转账 $15 。 bank.withdraw(10, 50); // 返回 false ，交易无效，因为账户 10 并不存在。 提示： * n == balance.length * 1 <= n, account, account1, account2 <= 105 * 0 <= balance[i], money <= 1012 * transfer, deposit, withdraw 三个函数，每个 最多调用 104 次
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用一个数组来存储每个账户的余额，并通过索引进行操作。

算法步骤:
1. 初始化时，将输入的余额数组存储在类的实例变量中。
2. 对于转账操作，检查两个账户是否有效且有足够的余额，然后进行转账。
3. 对于存款操作，检查账户是否有效，然后进行存款。
4. 对于取款操作，检查账户是否有效且有足够的余额，然后进行取款。

关键点:
- 使用数组索引来快速访问和更新账户余额。
- 在每次操作前检查账户的有效性和余额。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - 每次操作的时间复杂度都是常数级别。
空间复杂度: O(n) - 使用一个长度为 n 的数组来存储账户余额。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


class Bank:
    def __init__(self, balance: List[int]):
        self.balance = balance
        self.n = len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self._is_valid_account(account1) or not self._is_valid_account(account2):
            return False
        if self.balance[account1 - 1] < money:
            return False
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if not self._is_valid_account(account):
            return False
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self._is_valid_account(account):
            return False
        if self.balance[account - 1] < money:
            return False
        self.balance[account - 1] -= money
        return True

    def _is_valid_account(self, account: int) -> bool:
        return 1 <= account <= self.n


Solution = create_solution(Bank)