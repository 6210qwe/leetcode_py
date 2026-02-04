# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 726
标题: Number of Atoms
难度: hard
链接: https://leetcode.cn/problems/number-of-atoms/
题目类型: 栈、哈希表、字符串、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
726. 原子的数量 - 给你一个字符串化学式 formula ，返回 每种原子的数量 。 原子总是以一个大写字母开始，接着跟随 0 个或任意个小写字母，表示原子的名字。 如果数量大于 1，原子后会跟着数字表示原子的数量。如果数量等于 1 则不会跟数字。 * 例如，"H2O" 和 "H2O2" 是可行的，但 "H1O2" 这个表达是不可行的。 两个化学式连在一起可以构成新的化学式。 * 例如 "H2O2He3Mg4" 也是化学式。 由括号括起的化学式并佐以数字（可选择性添加）也是化学式。 * 例如 "(H2O2)" 和 "(H2O2)3" 是化学式。 返回所有原子的数量，格式为：第一个（按字典序）原子的名字，跟着它的数量（如果数量大于 1），然后是第二个原子的名字（按字典序），跟着它的数量（如果数量大于 1），以此类推。 示例 1： 输入：formula = "H2O" 输出："H2O" 解释：原子的数量是 {'H': 2, 'O': 1}。 示例 2： 输入：formula = "Mg(OH)2" 输出："H2MgO2" 解释：原子的数量是 {'H': 2, 'Mg': 1, 'O': 2}。 示例 3： 输入：formula = "K4(ON(SO3)2)2" 输出："K4N2O14S4" 解释：原子的数量是 {'K': 4, 'N': 2, 'O': 14, 'S': 4}。 提示： * 1 <= formula.length <= 1000 * formula 由英文字母、数字、'(' 和 ')' 组成 * formula 总是有效的化学式
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用栈来处理嵌套的括号，并使用哈希表来记录每种原子的数量。

算法步骤:
1. 初始化一个栈，用于存储当前层级的原子计数。
2. 从右到左遍历字符串，解析原子和数量。
3. 遇到右括号时，将当前计数压入栈中，并初始化一个新的计数。
4. 遇到左括号时，弹出栈顶元素，并乘以括号外的倍数。
5. 最终合并所有层级的计数，生成结果字符串。

关键点:
- 使用栈来处理嵌套的括号。
- 从右到左遍历字符串，方便处理嵌套结构。
- 使用哈希表记录每种原子的数量。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def count_of_atoms(formula: str) -> str:
    def parse():
        nonlocal i
        stack = [collections.Counter()]
        num = ''
        
        while i >= 0:
            char = formula[i]
            
            if char.isdigit():
                num = char + num
            elif char.islower():
                i -= 1
                continue
            elif char == ')':
                if num:
                    multiplier = int(num)
                    num = ''
                else:
                    multiplier = 1
                counter = collections.Counter()
                while True:
                    top = stack.pop()
                    for atom, count in top.items():
                        counter[atom] += count * multiplier
                    if stack and isinstance(stack[-1], int):
                        multiplier *= stack.pop()
                    else:
                        break
                stack.append(counter)
            elif char == '(':
                if num:
                    stack.append(int(num))
                    num = ''
                else:
                    stack.append(1)
            else:
                if num:
                    stack[-1][char] += int(num)
                    num = ''
                else:
                    stack[-1][char] += 1
            
            i -= 1
        
        return sum((collections.Counter({atom: count}) for count in stack), collections.Counter())

    i = len(formula) - 1
    result = parse()
    return ''.join(f'{atom}{count if count > 1 else ""}' for atom, count in sorted(result.items()))


Solution = create_solution(count_of_atoms)