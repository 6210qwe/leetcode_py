# -*- coding:utf-8 -*-
"""
检查前500道题中缺失的题目
"""
import os
import json
from pathlib import Path

project_root = Path(__file__).parent.parent

def check_missing():
    # 检查已实现的题目
    by_id_dir = project_root / "leetcode_solutions" / "by_id"
    if not by_id_dir.exists():
        print("by_id目录不存在")
        return
    
    files = [f for f in os.listdir(by_id_dir) if f.startswith('q') and f.endswith('.py')]
    implemented = set()
    for f in files:
        try:
            num = int(f[1:5])
            if 1 <= num <= 500:
                implemented.add(num)
        except:
            pass
    
    print(f"前500道题已实现: {len(implemented)}")
    missing = [i for i in range(1, 501) if i not in implemented]
    print(f"前500道题缺失: {len(missing)}")
    if missing:
        print(f"缺失的题目: {missing[:50]}")
    return missing

if __name__ == "__main__":
    check_missing()













