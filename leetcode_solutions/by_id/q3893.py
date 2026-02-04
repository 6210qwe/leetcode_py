# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3893
标题: Generate Tag for Video Caption
难度: easy
链接: https://leetcode.cn/problems/generate-tag-for-video-caption/
题目类型: 字符串、模拟
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3582. 为视频标题生成标签 - 给你一个字符串 caption，表示一个视频的标题。 需要按照以下步骤 按顺序 生成一个视频的 有效标签 ： 1. 将 所有单词 组合为单个 驼峰命名字符串 ，并在前面加上 '#'。驼峰命名字符串 指的是除第一个单词外，其余单词的首字母大写，且每个单词的首字母之后的字符必须是小写。 2. 移除 所有不是英文字母的字符，但 保留 第一个字符 '#'。 3. 将结果 截断 为最多 100 个字符。 对 caption 执行上述操作后，返回生成的 标签 。 示例 1： 输入： caption = "Leetcode daily streak achieved" 输出： "#leetcodeDailyStreakAchieved" 解释： 除了 "leetcode" 以外的所有单词的首字母需要大写。 示例 2： 输入： caption = "can I Go There" 输出： "#canIGoThere" 解释： 除了 "can" 以外的所有单词的首字母需要大写。 示例 3： 输入： caption = "hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh" 输出： "#hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh" 解释： 由于第一个单词长度为 101，因此需要从单词末尾截去最后两个字符。 提示： * 1 <= caption.length <= 150 * caption 仅由英文字母和 ' ' 组成。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 将输入字符串转换为驼峰命名格式，并进行必要的字符过滤和截断。

算法步骤:
1. 分割输入字符串为单词列表。
2. 将第一个单词保持原样，其余单词首字母大写，其余字母小写。
3. 合并所有单词为一个字符串，并在前面加上 '#'。
4. 移除所有非英文字母字符。
5. 截断结果字符串为最多 100 个字符。

关键点:
- 使用 `str.split()` 方法分割字符串。
- 使用 `str.capitalize()` 方法将单词首字母大写。
- 使用 `isalpha()` 方法检查字符是否为英文字母。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是输入字符串的长度。我们需要遍历整个字符串进行处理。
空间复杂度: O(n)，最坏情况下需要存储与输入字符串等长的结果字符串。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def generate_tag_for_video_caption(caption: str) -> str:
    """
    生成视频标题的有效标签。
    """
    # 分割输入字符串为单词列表
    words = caption.split()
    
    # 将第一个单词保持原样，其余单词首字母大写，其余字母小写
    camel_case_words = [words[0].lower()] + [word.capitalize() for word in words[1:]]
    
    # 合并所有单词为一个字符串，并在前面加上 '#'
    tag = "#" + "".join(camel_case_words)
    
    # 移除所有非英文字母字符
    tag = ''.join(char for char in tag if char.isalpha() or char == '#')
    
    # 截断结果字符串为最多 100 个字符
    tag = tag[:100]
    
    return tag


Solution = create_solution(generate_tag_for_video_caption)