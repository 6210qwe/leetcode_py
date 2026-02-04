# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3816
标题: DNA Pattern Recognition
难度: medium
链接: https://leetcode.cn/problems/dna-pattern-recognition/
题目类型: 其他
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3475. DNA 模式识别 - 表：Samples +----------------+---------+ | Column Name | Type | +----------------+---------+ | sample_id | int | | dna_sequence | varchar | | species | varchar | +----------------+---------+ sample_id 是这张表的唯一主键。 每一行包含一个 DNA 序列以一个字符（A，T，G，C）组成的字符串表示以及它所采集自的物种。 生物学家正在研究 DNA 序列中的基本模式。编写一个解决方案以识别具有以下模式的 sample_id： * 以 ATG 开头 的序列（一个常见的 起始密码子） * 以 TAA，TAG 或 TGA 结尾 的序列（终止密码子） * 包含基序 ATAT 的序列（一个简单重复模式） * 有 至少 3 个连续 G 的序列（如 GGG 或 GGGG） 返回结果表以 sample_id 升序 排序。 结果格式如下所示。 示例： 输入： Samples 表： +-----------+------------------+-----------+ | sample_id | dna_sequence | species | +-----------+------------------+-----------+ | 1 | ATGCTAGCTAGCTAA | Human | | 2 | GGGTCAATCATC | Human | | 3 | ATATATCGTAGCTA | Human | | 4 | ATGGGGTCATCATAA | Mouse | | 5 | TCAGTCAGTCAG | Mouse | | 6 | ATATCGCGCTAG | Zebrafish | | 7 | CGTATGCGTCGTA | Zebrafish | +-----------+------------------+-----------+ 输出： +-----------+------------------+-------------+-------------+------------+------------+------------+ | sample_id | dna_sequence | species | has_start | has_stop | has_atat | has_ggg | +-----------+------------------+-------------+-------------+------------+------------+------------+ | 1 | ATGCTAGCTAGCTAA | Human | 1 | 1 | 0 | 0 | | 2 | GGGTCAATCATC | Human | 0 | 0 | 0 | 1 | | 3 | ATATATCGTAGCTA | Human | 0 | 0 | 1 | 0 | | 4 | ATGGGGTCATCATAA | Mouse | 1 | 1 | 0 | 1 | | 5 | TCAGTCAGTCAG | Mouse | 0 | 0 | 0 | 0 | | 6 | ATATCGCGCTAG | Zebrafish | 0 | 1 | 1 | 0 | | 7 | CGTATGCGTCGTA | Zebrafish | 0 | 0 | 0 | 0 | +-----------+------------------+-------------+-------------+------------+------------+------------+ 解释： * 样本 1（ATGCTAGCTAGCTAA）： * 以 ATG 开头（has_start = 1） * 以 TAA 结尾（has_stop = 1） * 不包含 ATAT（has_atat = 0） * 不包含至少 3 个连续 ‘G’（has_ggg = 0） * 样本 2（GGGTCAATCATC）： * 不以 ATG 开头（has_start = 0） * 不以 TAA，TAG 或 TGA 结尾（has_stop = 0） * 不包含 ATAT（has_atat = 0） * 包含 GGG（has_ggg = 1） * 样本 3（ATATATCGTAGCTA）： * 不以 ATG 开头（has_start = 0） * 不以 TAA，TAG 或 TGA 结尾（has_stop = 0） * 包含 ATAT（has_atat = 1） * 不包含至少 3 个连续 ‘G’（has_ggg = 0） * 样本 4（ATGGGGTCATCATAA）： * 以 ATG 开头（has_start = 1） * 以 TAA 结尾（has_stop = 1） * 不包含 ATAT（has_atat = 0） * 包含 GGGG（has_ggg = 1） * 样本 5（TCAGTCAGTCAG）： * 不匹配任何模式（所有字段 = 0） * 样本 6（ATATCGCGCTAG）： * 不以 ATG 开头（has_start = 0） * 以 TAG 结尾（has_stop = 1） * 包含 ATAT（has_atat = 1） * 不包含至少 3 个连续 ‘G’（has_ggg = 0） * 样本 7（CGTATGCGTCGTA）： * 不以 ATG 开头（has_start = 0） * 不以 TAA，TAG 或 TGA 结尾（has_stop = 0） * 不包含 ATAT（has_atat = 0） * 不包含至少 3 个连续 ‘G’（has_ggg = 0） 注意： * 结果以 sample_id 升序排序 * 对于每个模式，1 表示该模式存在，0 表示不存在
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想:
- 遍历每个样本，检查其 DNA 序列是否符合给定的模式。
- 使用简单的字符串操作来检查各个模式。

算法步骤:
1. 初始化一个空列表 `result` 来存储结果。
2. 遍历每个样本：
   - 检查是否以 'ATG' 开头。
   - 检查是否以 'TAA', 'TAG', 'TGA' 结尾。
   - 检查是否包含 'ATAT'。
   - 检查是否包含至少 3 个连续的 'G'。
3. 将结果添加到 `result` 列表中。
4. 返回按 `sample_id` 升序排序的结果。

关键点:
- 使用字符串方法 `startswith`, `endswith`, `in` 和正则表达式来高效检查各个模式。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m)，其中 n 是样本数量，m 是每个样本 DNA 序列的平均长度。
空间复杂度: O(1)，除了输入和输出外，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(samples: List[List[str]]) -> List[List[str]]:
    """
    函数式接口 - 识别 DNA 序列中的模式
    """
    result = []
    
    for sample in samples:
        sample_id, dna_sequence, species = sample
        has_start = dna_sequence.startswith('ATG')
        has_stop = any(dna_sequence.endswith(stop_codon) for stop_codon in ['TAA', 'TAG', 'TGA'])
        has_atat = 'ATAT' in dna_sequence
        has_ggg = 'GGG' in dna_sequence
        
        result.append([int(sample_id), dna_sequence, species, int(has_start), int(has_stop), int(has_atat), int(has_ggg)])
    
    return sorted(result, key=lambda x: x[0])


Solution = create_solution(solution_function_name)