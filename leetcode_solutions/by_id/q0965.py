# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 965
标题: Unique Email Addresses
难度: easy
链接: https://leetcode.cn/problems/unique-email-addresses/
题目类型: 数组、哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
929. 独特的电子邮件地址 - 每个 有效电子邮件地址 都由一个 本地名 和一个 域名 组成，以 '@' 符号分隔。除小写字母之外，电子邮件地址还可以含有一个或多个 '.' 或 '+' 。 * 例如，在 alice@leetcode.com中， alice 是 本地名 ，而 leetcode.com 是 域名 。 如果在电子邮件地址的 本地名 部分中的某些字符之间添加句点（'.'），则发往那里的邮件将会转发到本地名中没有点的同一地址。请注意，此规则 不适用于域名 。 * 例如，"alice.z@leetcode.com” 和 “alicez@leetcode.com” 会转发到同一电子邮件地址。 如果在 本地名 中添加加号（'+'），则会忽略第一个加号后面的所有内容。这允许过滤某些电子邮件。同样，此规则 不适用于域名 。 * 例如 m.y+name@email.com 将转发到 my@email.com。 可以同时使用这两个规则。 给你一个字符串数组 emails，我们会向每个 emails[i] 发送一封电子邮件。返回实际收到邮件的不同地址数目。 示例 1： 输入：emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"] 输出：2 解释：实际收到邮件的是 "testemail@leetcode.com" 和 "testemail@lee.tcode.com"。 示例 2： 输入：emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"] 输出：3 提示： * 1 <= emails.length <= 100 * 1 <= emails[i].length <= 100 * emails[i] 由小写英文字母、'+'、'.' 和 '@' 组成 * 每个 emails[i] 都包含有且仅有一个 '@' 字符 * 所有本地名和域名都不为空 * 本地名不会以 '+' 字符作为开头 * 域名以 ".com" 后缀结尾。 * 域名在 ".com" 后缀前至少包含一个字符
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用集合来存储处理后的唯一电子邮件地址。

算法步骤:
1. 初始化一个空集合 `unique_emails` 用于存储唯一的电子邮件地址。
2. 遍历每个电子邮件地址：
   - 分割本地名和域名。
   - 处理本地名：去掉所有 '.' 并忽略第一个 '+' 及其后面的部分。
   - 将处理后的本地名和域名重新组合，并加入集合 `unique_emails`。
3. 返回集合 `unique_emails` 的大小。

关键点:
- 使用集合来自动去重。
- 本地名处理时，需要去掉 '.' 并忽略 '+' 后面的部分。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m)，其中 n 是 emails 的长度，m 是每个 email 的平均长度。
空间复杂度: O(n * m)，用于存储处理后的电子邮件地址。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def unique_email_addresses(emails: List[str]) -> int:
    """
    函数式接口 - 返回实际收到邮件的不同地址数目
    """
    unique_emails = set()

    for email in emails:
        local_name, domain_name = email.split('@')
        local_name = local_name.split('+')[0].replace('.', '')
        unique_emails.add(local_name + '@' + domain_name)

    return len(unique_emails)


Solution = create_solution(unique_email_addresses)