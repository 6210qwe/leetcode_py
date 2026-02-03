# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 68
标题: Text Justification
难度: hard
链接: https://leetcode.cn/problems/text-justification/
题目类型: 数组、字符串、模拟
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
68. 文本左右对齐 - 给定一个单词数组 words 和一个长度 maxWidth ，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。 你应该使用 “贪心算法” 来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。 要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。 文本的最后一行应为左对齐，且单词之间不插入额外的空格。 注意: * 单词是指由非空格字符组成的字符序列。 * 每个单词的长度大于 0，小于等于 maxWidth。 * 输入单词数组 words 至少包含一个单词。 示例 1: 输入: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16 输出: [ "This is an", "example of text", "justification. " ] 示例 2: 输入:words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16 输出: [ "What must be", "acknowledgment ", "shall be " ] 解释: 注意最后一行的格式应为 "shall be " 而不是 "shall be", 因为最后一行应为左对齐，而不是左右两端对齐。 第二行同样为左对齐，这是因为这行只包含一个单词。 示例 3: 输入:words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]，maxWidth = 20 输出: [ "Science is what we", "understand well", "enough to explain to", "a computer. Art is", "everything else we", "do " ] 提示: * 1 <= words.length <= 300 * 1 <= words[i].length <= 20 * words[i] 由小写英文字母和符号组成 * 1 <= maxWidth <= 100 * words[i].length <= maxWidth
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 贪心算法，尽可能多地往每行放置单词，然后均匀分配空格

算法步骤:
1. 遍历单词数组，收集可以放在同一行的单词
2. 对于每一行：
   - 如果是最后一行或只有一个单词：左对齐，单词间只有一个空格
   - 否则：计算需要分配的空格数，尽可能均匀分配
3. 构建每一行的字符串并加入结果

关键点:
- 贪心策略：尽可能多地放置单词
- 空格分配：如果不能均匀分配，左侧空格数多于右侧
- 最后一行特殊处理：左对齐，单词间只有一个空格
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - n为所有单词的总字符数
空间复杂度: O(n) - 存储结果字符串列表
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from leetcode_solutions.utils.solution import create_solution


def full_justify(words: List[str], max_width: int) -> List[str]:
    """
    函数式接口 - 贪心算法
    
    实现思路:
    使用贪心算法尽可能多地往每行放置单词，然后均匀分配空格。
    
    Args:
        words: 单词数组
        max_width: 每行的最大宽度
        
    Returns:
        重新排版后的文本行列表
        
    Example:
        >>> full_justify(["This", "is", "an", "example"], 16)
        ['This    is    an', 'example         ']
    """
    result = []
    i = 0
    
    while i < len(words):
        # 收集可以放在同一行的单词
        line_words = []
        line_length = 0
        
        while i < len(words):
            word = words[i]
            # 计算添加这个单词后的长度
            # 如果line_words不为空，需要加一个空格
            needed_length = line_length + len(word) + (1 if line_words else 0)
            
            if needed_length <= max_width:
                line_words.append(word)
                line_length = needed_length
                i += 1
            else:
                break
        
        # 构建当前行
        if i == len(words) or len(line_words) == 1:
            # 最后一行或只有一个单词：左对齐
            line = ' '.join(line_words)
            line += ' ' * (max_width - len(line))
        else:
            # 计算需要分配的空格数
            total_spaces = max_width - sum(len(word) for word in line_words)
            num_gaps = len(line_words) - 1
            
            # 计算每个间隙的基础空格数和额外空格数
            base_spaces = total_spaces // num_gaps
            extra_spaces = total_spaces % num_gaps
            
            # 构建行
            line = line_words[0]
            for j in range(1, len(line_words)):
                spaces = base_spaces + (1 if j <= extra_spaces else 0)
                line += ' ' * spaces + line_words[j]
        
        result.append(line)
    
    return result


# 自动生成Solution类（无需手动编写）
Solution = create_solution(full_justify)
