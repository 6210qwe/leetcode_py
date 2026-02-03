# -*- coding:utf-8 -*-
"""
LeetCode题解PyPI包
支持按题号、难度、题型、周赛等多维度导入最优Python解法
"""

from setuptools import setup, find_packages
import os

__version__ = '0.1.0'

# 读取README文件
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    return ""

setup(
    name="leetcode-solutions",
    version=__version__,
    author="MindLullaby",
    description="LeetCode题解包，支持按题号/难度/题型/周赛导入最优Python解法",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/leetcode-solutions",
    license="MIT",
    packages=find_packages(include=['leetcode_solutions', 'leetcode_solutions.*']),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Education",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: Chinese (Simplified)",
    ],
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.28.0",  # 用于获取LeetCode题目
    ],
    include_package_data=True,
    zip_safe=False,
)

