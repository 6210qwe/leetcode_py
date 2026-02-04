# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2774
标题: Differences Between Two Objects
难度: medium
链接: https://leetcode.cn/problems/differences-between-two-objects/
题目类型: 其他
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2700. 两个对象之间的差异 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用递归深度优先搜索 (DFS) 来比较两个对象的差异。

算法步骤:
1. 定义一个递归函数 `dfs`，用于比较两个对象。
2. 如果两个对象都是字典，递归比较它们的键值对。
3. 如果两个对象都是列表，递归比较它们的元素。
4. 如果两个对象不相等，记录差异。
5. 返回所有差异。

关键点:
- 使用递归处理嵌套结构。
- 记录差异时，使用路径表示法来标识不同之处。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是对象中元素的总数。
空间复杂度: O(d)，其中 d 是对象的最大深度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Any, List, Optional


def dfs(obj1: Any, obj2: Any, path: List[str]) -> List[str]:
    if isinstance(obj1, dict) and isinstance(obj2, dict):
        for key in set(obj1.keys()).union(obj2.keys()):
            if key not in obj1 or key not in obj2:
                yield f"{'.'.join(path + [key])}: {obj1.get(key, 'None')} != {obj2.get(key, 'None')}"
            else:
                yield from dfs(obj1[key], obj2[key], path + [key])
    elif isinstance(obj1, list) and isinstance(obj2, list):
        for i in range(max(len(obj1), len(obj2))):
            if i >= len(obj1) or i >= len(obj2):
                yield f"{'.'.join(path + [str(i)])}: {obj1[i] if i < len(obj1) else 'None'} != {obj2[i] if i < len(obj2) else 'None'}"
            else:
                yield from dfs(obj1[i], obj2[i], path + [str(i)])
    elif obj1 != obj2:
        yield f"{'.'.join(path)}: {obj1} != {obj2}"


def solution_function_name(obj1: Any, obj2: Any) -> List[str]:
    """
    函数式接口 - 比较两个对象之间的差异
    """
    return list(dfs(obj1, obj2, []))


Solution = create_solution(solution_function_name)