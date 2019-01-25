
def gcd(_a,_b):
    def _gcd(a, b):
        if a % 2 == 0 and b % 2 == 0:
            return 2 * gcd(a//2,b//2)
        elif a % 2 != 0 and b % 2 == 0:
            return gcd(a,b//2)
        elif a % 2 == 0 and b % 2 != 0:
            return gcd(a//2,b)
        else: # all odd
            if a > b:
                return gcd((a-b)//2, b)
            elif b > a:
                return gcd((b-a)//2, a)
            else: # base case
                return a
    if _a > 0 and _b > 0:
        return _gcd(_a, _b)
    else:
        return 1

def simplify(up, down):
    up_down_gcd = gcd(up, down)
    return up//up_down_gcd, down//up_down_gcd
    
def handle_float(float_num_str):
    if float_num_str == "":
        float_num = float_len = 0
    else:
        float_len = len(float_num_str)
        float_num = int(float_num_str)
    return float_num, float_len

def convert_type1(s): # int
    return int(s), 1

def convert_type2(s): # no repeat
    integer_part, non_repeating_part = s.split('.')
    integer_part = int(integer_part)
    non_repeating_part, non_repeating_len = handle_float(non_repeating_part)
    down = 10**non_repeating_len
    up = integer_part * down + non_repeating_part
    return simplify(up, down)

def convert_type3(s): # with repeat
    integer_part, float_part = s.split('.')
    integer_part = int(integer_part)
    
    non_repeating_part, repeating_part = float_part.split('(')
    
    non_repeating_part, non_repeating_len = handle_float(non_repeating_part)
    
    repeating_part, repeating_len = handle_float(repeating_part[:-1])
    if repeating_part == 0 or repeating_len == 0:
        repeating_9s = 1  # handle .(0) or .()
    else:
        repeating_9s = ( 10**repeating_len-1 )
    
    down = 10**non_repeating_len * repeating_9s
    up = integer_part * down + non_repeating_part * repeating_9s + repeating_part
    return simplify(up, down)

def convert(s):
    if "(" in s:
        return convert_type3(s)
    elif "." in s: 
        return convert_type2(s)
    return convert_type1(s)

class Solution:

    def isRationalEqual(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s_up, s_down = convert(S)
        t_up, t_down = convert(T)
        return (s_up == t_up) and (s_down == t_down)
        