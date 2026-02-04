# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2197
标题: Decode the Slanted Ciphertext
难度: medium
链接: https://leetcode.cn/problems/decode-the-slanted-ciphertext/
题目类型: 字符串、模拟
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2075. 解码斜向换位密码 - 字符串 originalText 使用 斜向换位密码 ，经由 行数固定 为 rows 的矩阵辅助，加密得到一个字符串 encodedText 。 originalText 先按从左上到右下的方式放置到矩阵中。 [https://assets.leetcode.com/uploads/2021/11/07/exa11.png] 先填充蓝色单元格，接着是红色单元格，然后是黄色单元格，以此类推，直到到达 originalText 末尾。箭头指示顺序即为单元格填充顺序。所有空单元格用 ' ' 进行填充。矩阵的列数需满足：用 originalText 填充之后，最右侧列 不为空 。 接着按行将字符附加到矩阵中，构造 encodedText 。 [https://assets.leetcode.com/uploads/2021/11/07/exa12.png] 先把蓝色单元格中的字符附加到 encodedText 中，接着是红色单元格，最后是黄色单元格。箭头指示单元格访问顺序。 例如，如果 originalText = "cipher" 且 rows = 3 ，那么我们可以按下述方法将其编码： [https://assets.leetcode.com/uploads/2021/10/25/desc2.png] 蓝色箭头标识 originalText 是如何放入矩阵中的，红色箭头标识形成 encodedText 的顺序。在上述例子中，encodedText = "ch ie pr" 。 给你编码后的字符串 encodedText 和矩阵的行数 rows ，返回源字符串 originalText 。 注意：originalText 不 含任何尾随空格 ' ' 。生成的测试用例满足 仅存在一个 可能的 originalText 。 示例 1： 输入：encodedText = "ch ie pr", rows = 3 输出："cipher" 解释：此示例与问题描述中的例子相同。 示例 2： [https://assets.leetcode.com/uploads/2021/10/26/exam1.png] 输入：encodedText = "iveo eed l te olc", rows = 4 输出："i love leetcode" 解释：上图标识用于编码 originalText 的矩阵。 蓝色箭头展示如何从 encodedText 找到 originalText 。 示例 3： [https://assets.leetcode.com/uploads/2021/10/26/eg2.png] 输入：encodedText = "coding", rows = 1 输出："coding" 解释：由于只有 1 行，所以 originalText 和 encodedText 是相同的。 示例 4： [https://assets.leetcode.com/uploads/2021/10/26/exam3.png] 输入：encodedText = " b ac", rows = 2 输出：" abc" 解释：originalText 不能含尾随空格，但它可能会有一个或者多个前置空格。 提示： * 0 <= encodedText.length <= 106 * encodedText 仅由小写英文字母和 ' ' 组成 * encodedText 是对某个 不含 尾随空格的 originalText 的一个有效编码 * 1 <= rows <= 1000 * 生成的测试用例满足 仅存在一个 可能的 originalText
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过计算每个字符在原始矩阵中的位置来重构原始字符串。

算法步骤:
1. 计算矩阵的列数。
2. 初始化一个空字符串 `originalText`。
3. 遍历 `encodedText`，根据当前字符在矩阵中的位置，将其添加到 `originalText` 中。
4. 返回 `originalText`，去除尾随空格。

关键点:
- 计算矩阵的列数时，需要确保最右侧列不为空。
- 通过计算每个字符在矩阵中的位置来重构原始字符串。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是 `encodedText` 的长度。
空间复杂度: O(n)，存储重构后的 `originalText`。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def decode_ciphertext(encodedText: str, rows: int) -> str:
    """
    函数式接口 - 解码斜向换位密码
    """
    if not encodedText or rows == 1:
        return encodedText.strip()

    n = len(encodedText)
    cols = (n + rows - 1) // rows  # 计算列数
    originalText = []

    for col in range(cols):
        for row in range(rows):
            index = row * cols + col
            if index < n:
                originalText.append(encodedText[index])

    return ''.join(originalText).rstrip()


Solution = create_solution(decode_ciphertext)