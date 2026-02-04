# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2389
标题: Design a Text Editor
难度: hard
链接: https://leetcode.cn/problems/design-a-text-editor/
题目类型: 栈、设计、链表、字符串、双向链表、模拟
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2296. 设计一个文本编辑器 - 请你设计一个带光标的文本编辑器，它可以实现以下功能： * 添加：在光标所在处添加文本。 * 删除：在光标所在处删除文本（模拟键盘的删除键）。 * 移动：将光标往左或者往右移动。 当删除文本时，只有光标左边的字符会被删除。光标会留在文本内，也就是说任意时候 0 <= cursor.position <= currentText.length 都成立。 请你实现 TextEditor 类： * TextEditor() 用空文本初始化对象。 * void addText(string text) 将 text 添加到光标所在位置。添加完后光标在 text 的右边。 * int deleteText(int k) 删除光标左边 k 个字符。返回实际删除的字符数目。 * string cursorLeft(int k) 将光标向左移动 k 次。返回移动后光标左边 min(10, len) 个字符，其中 len 是光标左边的字符数目。 * string cursorRight(int k) 将光标向右移动 k 次。返回移动后光标左边 min(10, len) 个字符，其中 len 是光标左边的字符数目。 示例 1： 输入： ["TextEditor", "addText", "deleteText", "addText", "cursorRight", "cursorLeft", "deleteText", "cursorLeft", "cursorRight"] [[], ["leetcode"], [4], ["practice"], [3], [8], [10], [2], [6]] 输出： [null, null, 4, null, "etpractice", "leet", 4, "", "practi"] 解释： TextEditor textEditor = new TextEditor(); // 当前 text 为 "|" 。（'|' 字符表示光标） textEditor.addText("leetcode"); // 当前文本为 "leetcode|" 。 textEditor.deleteText(4); // 返回 4 // 当前文本为 "leet|" 。 // 删除了 4 个字符。 textEditor.addText("practice"); // 当前文本为 "leetpractice|" 。 textEditor.cursorRight(3); // 返回 "etpractice" // 当前文本为 "leetpractice|". // 光标无法移动到文本以外，所以无法移动。 // "etpractice" 是光标左边的 10 个字符。 textEditor.cursorLeft(8); // 返回 "leet" // 当前文本为 "leet|practice" 。 // "leet" 是光标左边的 min(10, 4) = 4 个字符。 textEditor.deleteText(10); // 返回 4 // 当前文本为 "|practice" 。 // 只有 4 个字符被删除了。 textEditor.cursorLeft(2); // 返回 "" // 当前文本为 "|practice" 。 // 光标无法移动到文本以外，所以无法移动。 // "" 是光标左边的 min(10, 0) = 0 个字符。 textEditor.cursorRight(6); // 返回 "practi" // 当前文本为 "practi|ce" 。 // "practi" 是光标左边的 min(10, 6) = 6 个字符。 提示： * 1 <= text.length, k <= 40 * text 只含有小写英文字母。 * 调用 addText ，deleteText ，cursorLeft 和 cursorRight 的 总 次数不超过 2 * 104 次。 进阶：你能设计并实现一个每次调用时间复杂度为 O(k) 的解决方案吗？
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用双端队列来存储文本，并维护光标的位置。

算法步骤:
1. 初始化时，创建两个双端队列 left 和 right，分别存储光标左边和右边的字符。
2. addText: 将文本添加到 left 队列的末尾。
3. deleteText: 从 left 队列中删除 k 个字符，返回实际删除的字符数目。
4. cursorLeft: 将光标向左移动 k 次，每次将 left 队列的最后一个字符移到 right 队列的开头。
5. cursorRight: 将光标向右移动 k 次，每次将 right 队列的第一个字符移到 left 队列的末尾。

关键点:
- 使用双端队列可以高效地在光标左右移动和添加删除字符。
- 通过维护两个双端队列，可以确保操作的时间复杂度为 O(k)。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(k)
空间复杂度: O(n)，其中 n 是文本的长度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from collections import deque

class TextEditor:

    def __init__(self):
        self.left = deque()
        self.right = deque()

    def addText(self, text: str) -> None:
        for char in text:
            self.left.append(char)

    def deleteText(self, k: int) -> int:
        deleted = 0
        while k > 0 and self.left:
            self.left.pop()
            k -= 1
            deleted += 1
        return deleted

    def cursorLeft(self, k: int) -> str:
        while k > 0 and self.left:
            self.right.appendleft(self.left.pop())
            k -= 1
        return ''.join(list(self.left)[-10:])

    def cursorRight(self, k: int) -> str:
        while k > 0 and self.right:
            self.left.append(self.right.popleft())
            k -= 1
        return ''.join(list(self.left)[-10:])


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)