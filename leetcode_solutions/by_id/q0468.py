# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 468
标题: Validate IP Address
难度: medium
链接: https://leetcode.cn/problems/validate-ip-address/
题目类型: 字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
468. 验证IP地址 - 给定一个字符串 queryIP。如果是有效的 IPv4 地址，返回 "IPv4" ；如果是有效的 IPv6 地址，返回 "IPv6" ；如果不是上述类型的 IP 地址，返回 "Neither" 。 有效的IPv4地址 是 “x1.x2.x3.x4” 形式的IP地址。 其中 0 <= xi <= 255 且 xi 不能包含 前导零。例如: “192.168.1.1” 、 “192.168.1.0” 为有效IPv4地址， “192.168.01.1” 为无效IPv4地址; “192.168.1.00” 、 “192.168@1.1” 为无效IPv4地址。 一个有效的IPv6地址 是一个格式为“x1:x2:x3:x4:x5:x6:x7:x8” 的IP地址，其中: * 1 <= xi.length <= 4 * xi 是一个 十六进制字符串 ，可以包含数字、小写英文字母( 'a' 到 'f' )和大写英文字母( 'A' 到 'F' )。 * 在 xi 中允许前导零。 例如 "2001:0db8:85a3:0000:0000:8a2e:0370:7334" 和 "2001:db8:85a3:0:0:8A2E:0370:7334" 是有效的 IPv6 地址，而 "2001:0db8:85a3::8A2E:037j:7334" 和 "02001:0db8:85a3:0000:0000:8a2e:0370:7334" 是无效的 IPv6 地址。 示例 1： 输入：queryIP = "172.16.254.1" 输出："IPv4" 解释：有效的 IPv4 地址，返回 "IPv4" 示例 2： 输入：queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334" 输出："IPv6" 解释：有效的 IPv6 地址，返回 "IPv6" 示例 3： 输入：queryIP = "256.256.256.256" 输出："Neither" 解释：既不是 IPv4 地址，又不是 IPv6 地址 提示： * queryIP 仅由英文字母，数字，字符 '.' 和 ':' 组成。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 分别验证IPv4和IPv6格式

算法步骤:
1. 检查是否包含'.'，如果是则验证IPv4
2. 检查是否包含':'，如果是则验证IPv6
3. IPv4验证：4段，每段0-255，无前导0
4. IPv6验证：8段，每段1-4位十六进制字符

关键点:
- 严格验证格式
- 注意边界条件
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 遍历字符串一次
空间复杂度: O(1) - 只使用常数额外空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def validate_ip_address(queryIP: str) -> str:
    """
    函数式接口 - 验证IP地址
    
    实现思路:
    分别验证IPv4和IPv6格式。
    
    Args:
        queryIP: IP地址字符串
        
    Returns:
        "IPv4"、"IPv6"或"Neither"
        
    Example:
        >>> validate_ip_address("172.16.254.1")
        'IPv4'
    """
    def is_valid_ipv4(ip: str) -> bool:
        """验证IPv4"""
        parts = ip.split('.')
        if len(parts) != 4:
            return False
        
        for part in parts:
            if not part or (len(part) > 1 and part[0] == '0'):
                return False
            if not part.isdigit():
                return False
            num = int(part)
            if num < 0 or num > 255:
                return False
        
        return True
    
    def is_valid_ipv6(ip: str) -> bool:
        """验证IPv6"""
        parts = ip.split(':')
        if len(parts) != 8:
            return False
        
        hex_chars = set('0123456789abcdefABCDEF')
        for part in parts:
            if not part or len(part) > 4:
                return False
            if not all(c in hex_chars for c in part):
                return False
        
        return True
    
    if '.' in queryIP:
        return "IPv4" if is_valid_ipv4(queryIP) else "Neither"
    elif ':' in queryIP:
        return "IPv6" if is_valid_ipv6(queryIP) else "Neither"
    else:
        return "Neither"


# 自动生成Solution类（无需手动编写）
Solution = create_solution(validate_ip_address)
