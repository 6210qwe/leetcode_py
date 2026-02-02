# -*- coding:utf-8 -*-
"""通用工具函数"""

from typing import List, Any, Callable


def format_input(data: Any) -> str:
    """
    格式化输入数据为字符串（用于打印）
    
    Args:
        data: 任意数据
        
    Returns:
        格式化后的字符串
    """
    if isinstance(data, list):
        return '[' + ', '.join(str(x) for x in data) + ']'
    return str(data)


def print_result(func: Callable, *args, **kwargs):
    """
    打印函数执行结果（用于测试）
    
    Args:
        func: 要执行的函数
        *args: 位置参数
        **kwargs: 关键字参数
    """
    result = func(*args, **kwargs)
    print(f"输入: {args}, {kwargs}")
    print(f"输出: {result}")
    return result

