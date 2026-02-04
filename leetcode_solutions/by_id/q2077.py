# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2077
标题: Largest Number After Mutating Substring
难度: medium
链接: https://leetcode.cn/problems/largest-number-after-mutating-substring/
题目类型: 贪心、数组、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1946. 子字符串突变后可能得到的最大整数 - 给你一个字符串 num ，该字符串表示一个大整数。另给你一个长度为 10 且 下标从 0 开始 的整数数组 change ，该数组将 0-9 中的每个数字映射到另一个数字。更规范的说法是，数字 d 映射为数字 change[d] 。 你可以选择 突变 num 的任一子字符串。突变 子字符串意味着将每位数字 num[i] 替换为该数字在 change 中的映射（也就是说，将 num[i] 替换为 change[num[i]]）。 请你找出在对 num 的任一子字符串执行突变操作（也可以不执行）后，可能得到的 最大整数 ，并用字符串表示返回。 子字符串 是字符串中的一个连续序列。 示例 1： 输入：num = "132", change = [9,8,5,0,3,6,4,2,6,8] 输出："832" 解释：替换子字符串 "1"： - 1 映射为 change[1] = 8 。 因此 "132" 变为 "832" 。 "832" 是可以构造的最大整数，所以返回它的字符串表示。 示例 2： 输入：num = "021", change = [9,4,3,5,7,2,1,9,0,6] 输出："934" 解释：替换子字符串 "021"： - 0 映射为 change[0] = 9 。 - 2 映射为 change[2] = 3 。 - 1 映射为 change[1] = 4 。 因此，"021" 变为 "934" 。 "934" 是可以构造的最大整数，所以返回它的字符串表示。 示例 3： 输入：num = "5", change = [1,4,7,5,3,2,5,6,9,4] 输出："5" 解释："5" 已经是可以构造的最大整数，所以返回它的字符串表示。 提示： * 1 <= num.length <= 105 * num 仅由数字 0-9 组成 * change.length == 10 * 0 <= change[d] <= 9
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法，从左到右遍历字符串，找到第一个可以通过突变变大的位置，然后继续向右遍历，直到不能通过突变变大为止。

算法步骤:
1. 将 `change` 数组转换为字典，方便查找。
2. 初始化结果字符串 `result` 和一个标志变量 `mutating` 表示是否正在突变。
3. 遍历字符串 `num`：
   - 如果当前字符可以通过突变变大且 `mutating` 为 `False`，则开始突变。
   - 如果当前字符可以通过突变变大且 `mutating` 为 `True`，则继续突变。
   - 如果当前字符不能通过突变变大且 `mutating` 为 `True`，则停止突变。
4. 返回结果字符串 `result`。

关键点:
- 从左到右遍历，确保找到第一个可以突变的位置。
- 一旦开始突变，就一直突变直到不能再突变为止。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是字符串 `num` 的长度。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def largest_number_after_mutating_substring(num: str, change: List[int]) -> str:
    """
    函数式接口 - 找出在对 num 的任一子字符串执行突变操作后，可能得到的最大整数
    """
    # 将 change 数组转换为字典
    change_dict = {str(i): str(change[i]) for i in range(10)}
    
    result = []
    mutating = False
    
    for char in num:
        if not mutating and change_dict[char] > char:
            mutating = True
        if mutating and change_dict[char] >= char:
            result.append(change_dict[char])
        else:
            if mutating:
                mutating = False
            result.append(char)
    
    return ''.join(result)


Solution = create_solution(largest_number_after_mutating_substring)