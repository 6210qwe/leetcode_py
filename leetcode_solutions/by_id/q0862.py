# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 862
标题: Find And Replace in String
难度: medium
链接: https://leetcode.cn/problems/find-and-replace-in-string/
题目类型: 数组、哈希表、字符串、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
833. 字符串中的查找与替换 - 你会得到一个字符串 s (索引从 0 开始)，你必须对它执行 k 个替换操作。替换操作以三个长度均为 k 的并行数组给出：indices, sources, targets。 要完成第 i 个替换操作: 1. 检查 子字符串 sources[i] 是否出现在 原字符串 s 的索引 indices[i] 处。 2. 如果没有出现， 什么也不做 。 3. 如果出现，则用 targets[i] 替换 该子字符串。 例如，如果 s = "abcd" ， indices[i] = 0 , sources[i] = "ab"， targets[i] = "eee" ，那么替换的结果将是 "eeecd" 。 所有替换操作必须 同时 发生，这意味着替换操作不应该影响彼此的索引。测试用例保证元素间不会重叠 。 * 例如，一个 s = "abc" ， indices = [0,1] ， sources = ["ab"，"bc"] 的测试用例将不会生成，因为 "ab" 和 "bc" 替换重叠。 在对 s 执行所有替换操作后返回 结果字符串 。 子字符串 是字符串中连续的字符序列。 示例 1： [https://assets.leetcode.com/uploads/2021/06/12/833-ex1.png] 输入：s = "abcd", indices = [0,2], sources = ["a","cd"], targets = ["eee","ffff"] 输出："eeebffff" 解释： "a" 从 s 中的索引 0 开始，所以它被替换为 "eee"。 "cd" 从 s 中的索引 2 开始，所以它被替换为 "ffff"。 示例 2：[https://assets.leetcode.com/uploads/2021/06/12/833-ex2-1.png] 输入：s = "abcd", indices = [0,2], sources = ["ab","ec"], targets = ["eee","ffff"] 输出："eeecd" 解释： "ab" 从 s 中的索引 0 开始，所以它被替换为 "eee"。 "ec" 没有从原始的 S 中的索引 2 开始，所以它没有被替换。 提示： * 1 <= s.length <= 1000 * k == indices.length == sources.length == targets.length * 1 <= k <= 100 * 0 <= indices[i] < s.length * 1 <= sources[i].length, targets[i].length <= 50 * s 仅由小写英文字母组成 * sources[i] 和 targets[i] 仅由小写英文字母组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用一个字典来存储需要替换的索引和对应的替换信息，然后按索引从小到大进行替换。

算法步骤:
1. 创建一个字典，键为索引，值为一个元组 (source, target)。
2. 对索引进行排序，确保替换操作按顺序进行。
3. 从左到右遍历字符串，根据字典中的信息进行替换。
4. 构建最终结果字符串。

关键点:
- 使用字典存储替换信息，方便快速查找。
- 按索引排序，确保替换操作不相互影响。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + k log k)
- n 是字符串 s 的长度。
- k 是替换操作的数量。
- 排序操作的时间复杂度是 O(k log k)。
- 遍历字符串的时间复杂度是 O(n)。

空间复杂度: O(n + k)
- 存储替换信息的字典的空间复杂度是 O(k)。
- 最终结果字符串的空间复杂度是 O(n)。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def find_replace_string(s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
    # 创建一个字典，键为索引，值为一个元组 (source, target)
    replacements = {i: (src, tgt) for i, src, tgt in zip(indices, sources, targets)}
    
    # 对索引进行排序
    sorted_indices = sorted(replacements.keys())
    
    result = []
    last_index = 0
    
    for index in sorted_indices:
        src, tgt = replacements[index]
        
        # 将上一个替换结束到当前替换开始之间的部分添加到结果中
        result.append(s[last_index:index])
        
        # 检查是否可以进行替换
        if s[index:index + len(src)] == src:
            result.append(tgt)
            last_index = index + len(src)
        else:
            last_index = index
    
    # 添加剩余的部分
    result.append(s[last_index:])
    
    return ''.join(result)

Solution = create_solution(find_replace_string)