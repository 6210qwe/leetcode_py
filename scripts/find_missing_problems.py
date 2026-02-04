# -*- coding:utf-8 -*-
"""查找缺失题目的信息"""
import json
from pathlib import Path

project_root = Path(__file__).parent.parent
json_path = project_root / "leetcode.json"

with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

pairs = data.get("stat_status_pairs", [])
missing = [426, 427, 428, 429, 430, 431, 470, 478, 497]

found = {}
for pair in pairs:
    if not isinstance(pair, dict):
        continue
    stat = pair.get("stat")
    if not isinstance(stat, dict):
        continue
    pid = stat.get("question_id")
    if pid in missing:
        found[pid] = {
            "title": stat.get("question__title", "N/A"),
            "slug": stat.get("question__title_slug", "N/A"),
            "difficulty": pair.get("difficulty", {}).get("level", 1) if isinstance(pair.get("difficulty"), dict) else 1
        }

print(f"找到 {len(found)} 个题目:")
for pid in missing:
    if pid in found:
        print(f"  题目{pid}: {found[pid]['title']} (slug: {found[pid]['slug']})")
    else:
        print(f"  题目{pid}: 未找到")













