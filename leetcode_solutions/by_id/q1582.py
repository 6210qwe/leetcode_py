# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1582
标题: Design Browser History
难度: medium
链接: https://leetcode.cn/problems/design-browser-history/
题目类型: 栈、设计、数组、链表、数据流、双向链表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1472. 设计浏览器历史记录 - 你有一个只支持单个标签页的 浏览器 ，最开始你浏览的网页是 homepage ，你可以访问其他的网站 url ，也可以在浏览历史中后退 steps 步或前进 steps 步。 请你实现 BrowserHistory 类： * BrowserHistory(string homepage) ，用 homepage 初始化浏览器类。 * void visit(string url) 从当前页跳转访问 url 对应的页面 。执行此操作会把浏览历史前进的记录全部删除。 * string back(int steps) 在浏览历史中后退 steps 步。如果你只能在浏览历史中后退至多 x 步且 steps > x ，那么你只后退 x 步。请返回后退 至多 steps 步以后的 url 。 * string forward(int steps) 在浏览历史中前进 steps 步。如果你只能在浏览历史中前进至多 x 步且 steps > x ，那么你只前进 x 步。请返回前进 至多 steps步以后的 url 。 示例： 输入： ["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"] [["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]] 输出： [null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"] 解释： BrowserHistory browserHistory = new BrowserHistory("leetcode.com"); browserHistory.visit("google.com"); // 你原本在浏览 "leetcode.com" 。访问 "google.com" browserHistory.visit("facebook.com"); // 你原本在浏览 "google.com" 。访问 "facebook.com" browserHistory.visit("youtube.com"); // 你原本在浏览 "facebook.com" 。访问 "youtube.com" browserHistory.back(1); // 你原本在浏览 "youtube.com" ，后退到 "facebook.com" 并返回 "facebook.com" browserHistory.back(1); // 你原本在浏览 "facebook.com" ，后退到 "google.com" 并返回 "google.com" browserHistory.forward(1); // 你原本在浏览 "google.com" ，前进到 "facebook.com" 并返回 "facebook.com" browserHistory.visit("linkedin.com"); // 你原本在浏览 "facebook.com" 。 访问 "linkedin.com" browserHistory.forward(2); // 你原本在浏览 "linkedin.com" ，你无法前进任何步数。 browserHistory.back(2); // 你原本在浏览 "linkedin.com" ，后退两步依次先到 "facebook.com" ，然后到 "google.com" ，并返回 "google.com" browserHistory.back(7); // 你原本在浏览 "google.com"， 你只能后退一步到 "leetcode.com" ，并返回 "leetcode.com" 提示： * 1 <= homepage.length <= 20 * 1 <= url.length <= 20 * 1 <= steps <= 100 * homepage 和 url 都只包含 '.' 或者小写英文字母。 * 最多调用 5000 次 visit， back 和 forward 函数。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用一个列表来存储浏览历史，并使用一个指针来表示当前所在的页面。

算法步骤:
1. 初始化时，将 homepage 添加到历史记录列表中，并将指针指向该页面。
2. 当调用 visit 方法时，将新的 URL 添加到历史记录列表中，并更新指针位置。同时，删除指针之后的所有记录。
3. 当调用 back 方法时，根据给定的步数向后移动指针，并返回指针所在位置的 URL。
4. 当调用 forward 方法时，根据给定的步数向前移动指针，并返回指针所在位置的 URL。

关键点:
- 使用一个列表来存储浏览历史，使用一个指针来表示当前所在的页面。
- 在 visit 方法中，删除指针之后的所有记录。
- 在 back 和 forward 方法中，确保指针不会越界。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - 所有操作的时间复杂度都是常数级别。
空间复杂度: O(n) - 其中 n 是浏览历史的长度。
"""

# ============================================================================
# 代码实现
# ============================================================================

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]  # 存储浏览历史
        self.current_index = 0  # 当前页面的索引

    def visit(self, url: str) -> None:
        # 删除当前页面之后的所有记录
        self.history = self.history[:self.current_index + 1]
        self.history.append(url)
        self.current_index += 1

    def back(self, steps: int) -> str:
        # 向后移动指针
        self.current_index = max(0, self.current_index - steps)
        return self.history[self.current_index]

    def forward(self, steps: int) -> str:
        # 向前移动指针
        self.current_index = min(len(self.history) - 1, self.current_index + steps)
        return self.history[self.current_index]


Solution = create_solution(BrowserHistory)