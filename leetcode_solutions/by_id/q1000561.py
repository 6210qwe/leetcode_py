# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000561
标题: 探险营地
难度: medium
链接: https://leetcode.cn/problems/0Zeoeg/
题目类型: 其他
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCP 73. 探险营地 - 探险家小扣的行动轨迹，都将保存在记录仪中。`expeditions[i]` 表示小扣第 `i` 次探险记录，用一个字符串数组表示。其中的每个「营地」由大小写字母组成，通过子串 `->` 连接。 > 例："Leet->code->Campsite"，表示到访了 "Leet"、"code"、"Campsite" 三个营地。 `expeditions[0]` 包含了初始小扣已知的所有营地；对于之后的第 `i` 次探险(即 `expeditions[i]` 且 i > 0)，如果记录中包含了之前均没出现的营地，则表示小扣 **新发现** 的营地。 请你找出小扣发现新营地最多且索引最小的那次探险，并返回对应的记录索引。如果所有探险记录都没有发现新的营地，返回 `-1` **注意：** - 大小写不同的营地视为不同的营地； - 营地的名称长度均大于 `0`。 **示例 1：** >输入：`expeditions = ["leet->code","leet->code->Campsite->Leet","leet->code->leet->courier"]` > >输出：`1` > >解释： >初始已知的所有营地为 "leet" 和 "code" >第 1 次，到访了 "leet"、"code"、"Campsite"、"Leet"，新发现营地 2 处："Campsite"、"Leet" >第 2 次，到访了 "leet"、"code"、"courier"，新发现营地 1 处："courier" >第 1 次探险发现的新营地数量最多，因此返回 `1` **示例 2：** >输入：`expeditions = ["Alice->Dex","","Dex"]` > >输出：`-1` > >解释： >初始已知的所有营地为 "Alice" 和 "Dex" >第 1 次，未到访任何营地； >第 2 次，到访了 "Dex"，未新发现营地； >因为两次探险均未发现新的营地，返回 `-1` **示例 3：** >输入：`expeditions = ["","Gryffindor->Slytherin->Gryffindor","Hogwarts->Hufflepuff->Ravenclaw"]` > >输出：`2` > >解释： >初始未发现任何营地； >第 1 次，到访 "Gryffindor"、"Slytherin" 营地，其中重复到访 "Gryffindor" 两次， >因此新发现营地为 2 处："Gryffindor"、"Slytherin" >第 2 次，到访 "Hogwarts"、"Hufflepuff"、"Ravenclaw" 营地； >新发现营地 3 处："Hogwarts"、"Hufflepuff"、"Ravenclaw"； >第 2 次探险发现的新营地数量最多，因此返回 `2` **提示：** - `1 <= expeditions.length <= 1000` - `0 <= expeditions[i].length <= 1000` - 探险记录中只包含大小写字母和子串"->"
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用集合来记录已知的营地，并在每次探险中检查新发现的营地。

算法步骤:
1. 初始化一个集合 `known_camps` 来存储已知的营地。
2. 遍历 `expeditions` 数组，从第一个元素开始提取已知的营地并加入 `known_camps`。
3. 对于后续的每次探险，将当前探险记录中的营地拆分成单独的营地名称。
4. 计算当前探险中发现的新营地数量，并更新最大新发现营地数量及其对应的索引。
5. 返回最大新发现营地数量对应的索引，如果没有新发现则返回 `-1`。

关键点:
- 使用集合来高效地检查和存储已知的营地。
- 通过遍历和拆分字符串来提取每次探险中的营地名称。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m)，其中 n 是 `expeditions` 的长度，m 是每次探险记录的平均长度。
空间复杂度: O(k)，其中 k 是所有营地名称的总长度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(expeditions: List[str]) -> int:
    """
    函数式接口 - 找出小扣发现新营地最多且索引最小的那次探险，并返回对应的记录索引。
    """
    known_camps = set()
    
    # 提取初始已知的营地
    if expeditions[0]:
        known_camps.update(expeditions[0].split("->"))
    
    max_new_camps = 0
    max_index = -1
    
    for i in range(1, len(expeditions)):
        if not expeditions[i]:
            continue
        
        current_camps = expeditions[i].split("->")
        new_camps_count = sum(1 for camp in current_camps if camp not in known_camps)
        
        if new_camps_count > max_new_camps:
            max_new_camps = new_camps_count
            max_index = i
        
        known_camps.update(current_camps)
    
    return max_index


Solution = create_solution(solution_function_name)