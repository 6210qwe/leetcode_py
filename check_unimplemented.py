#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
检查未实现的LeetCode题目
通过查找文件中是否包含"TODO"或"[待实现]"来判断题目是否已实现
"""

import os
import re
from pathlib import Path


def check_unimplemented_problems(base_dir="leetcode_solutions/by_id"):
    """
    检查未实现的题目
    
    Args:
        base_dir: 题目文件所在目录
        
    Returns:
        未实现的题目列表
    """
    base_path = Path(base_dir)
    if not base_path.exists():
        print(f"目录不存在: {base_dir}")
        return []
    
    unimplemented = []
    todo_patterns = [
        r"TODO.*实现",
        r"\[待实现\]",
        r"# TODO:",
        r"待实现",
    ]
    
    # 获取所有Python文件
    python_files = sorted(base_path.glob("q*.py"))
    
    for file_path in python_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
                # 检查是否包含TODO标记
                has_todo = any(re.search(pattern, content, re.IGNORECASE) for pattern in todo_patterns)
                
                # 检查是否有pass语句（可能是未实现）
                has_pass = "pass" in content and "def" in content
                
                # 检查函数体是否为空或只有pass
                if has_todo or (has_pass and "TODO" in content.upper()):
                    # 提取题号
                    match = re.search(r'q(\d+)\.py', file_path.name)
                    if match:
                        problem_id = int(match.group(1))
                        unimplemented.append((problem_id, file_path.name))
        except Exception as e:
            print(f"读取文件 {file_path} 时出错: {e}")
    
    return unimplemented


def main():
    """主函数"""
    print("=" * 60)
    print("检查未实现的LeetCode题目")
    print("=" * 60)
    
    unimplemented = check_unimplemented_problems()
    
    if not unimplemented:
        print("\n✓ 所有题目都已实现！")
        return
    
    print(f"\n发现 {len(unimplemented)} 个未实现的题目：\n")
    
    # 按题号排序
    unimplemented.sort(key=lambda x: x[0])
    
    # 分组显示
    current_range = None
    for problem_id, filename in unimplemented:
        # 计算范围（每10题一组）
        range_start = (problem_id // 10) * 10
        range_end = range_start + 9
        
        if current_range != (range_start, range_end):
            if current_range is not None:
                print()
            print(f"【{range_start}-{range_end}题】")
            current_range = (range_start, range_end)
        
        print(f"  - {filename} (题号: {problem_id})")
    
    print("\n" + "=" * 60)
    print(f"总计: {len(unimplemented)} 个未实现的题目")
    print("=" * 60)
    
    # 保存到文件
    output_file = "unimplemented_problems.txt"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("未实现的LeetCode题目列表\n")
        f.write("=" * 60 + "\n\n")
        for problem_id, filename in unimplemented:
            f.write(f"{problem_id:4d} - {filename}\n")
    
    print(f"\n结果已保存到: {output_file}")


if __name__ == "__main__":
    main()

