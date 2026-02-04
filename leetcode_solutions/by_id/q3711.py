# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3711
标题: First Letter Capitalization II
难度: hard
链接: https://leetcode.cn/problems/first-letter-capitalization-ii/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3374. 首字母大写 II - 表：user_content +-------------+---------+ | Column Name | Type | +-------------+---------+ | content_id | int | | content_text| varchar | +-------------+---------+ content_id 是这张表的唯一主键。 每一行包含一个不同的 ID 以及对应的文本内容。 编写一个解决方案来根据下面的规则来转换 content_text 列中的文本： * 将每个单词的 第一个字母 转换为 大写，其余字母 保持小写。 * 特殊处理包含特殊字符的单词： * 对于用短横 - 连接的词语，两个部份 都应该 大写（例如，top-rated → Top-Rated） * 所有其他 格式 和 空格 应保持 不变 返回结果表同时包含原始的 content_text 以及根据上述规则修改后的文本。 结果格式如下例所示。 示例： 输入： user_content 表： +------------+---------------------------------+ | content_id | content_text | +------------+---------------------------------+ | 1 | hello world of SQL | | 2 | the QUICK-brown fox | | 3 | modern-day DATA science | | 4 | web-based FRONT-end development | +------------+---------------------------------+ 输出： +------------+---------------------------------+---------------------------------+ | content_id | original_text | converted_text | +------------+---------------------------------+---------------------------------+ | 1 | hello world of SQL | Hello World Of Sql | | 2 | the QUICK-brown fox | The Quick-Brown Fox | | 3 | modern-day DATA science | Modern-Day Data Science | | 4 | web-based FRONT-end development | Web-Based Front-End Development | +------------+---------------------------------+---------------------------------+ 解释： * 对于 content_id = 1： * 每个单词的首字母都是大写的："Hello World Of Sql" * 对于 content_id = 2： * 包含的连字符词 "QUICK-brown" 变为 "Quick-Brown" * 其它单词遵循普通的首字母大写规则 * 对于 content_id = 3： * 连字符词 "modern-day" 变为 "Modern-Day" * "DATA" 转换为 "Data" * 对于 content_id = 4： * 包含两个连字符词："web-based" → "Web-Based" * 以及 "FRONT-end" → "Front-End"
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用正则表达式和字符串操作来处理文本。

算法步骤:
1. 定义一个辅助函数 `capitalize_word` 来处理单个单词。
2. 使用正则表达式将文本拆分为单词列表。
3. 对每个单词应用 `capitalize_word` 函数。
4. 将处理后的单词重新组合成字符串。

关键点:
- 使用正则表达式来识别连字符词。
- 保持原始文本中的空格和其他格式不变。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是文本的长度。
空间复杂度: O(n)，用于存储处理后的文本。
"""

# ============================================================================
# 代码实现
# ============================================================================

import re

def capitalize_word(word):
    if '-' in word:
        parts = word.split('-')
        return '-'.join(part.capitalize() for part in parts)
    else:
        return word.capitalize()

def solution_function_name(content_text):
    """
    函数式接口 - 将每个单词的首字母大写，其余字母小写，并处理连字符词。
    """
    # 使用正则表达式将文本拆分为单词列表
    words = re.findall(r'\b\w+\b', content_text)
    
    # 对每个单词应用 capitalize_word 函数
    capitalized_words = [capitalize_word(word) for word in words]
    
    # 将处理后的单词重新组合成字符串
    def replace_match(match):
        return capitalized_words.pop(0)
    
    converted_text = re.sub(r'\b\w+\b', replace_match, content_text)
    
    return converted_text

Solution = create_solution(solution_function_name)