
## Helper functions
def gcd(_a,_b):
    ### 這邊就是一般的binary gcd, base case 是相等的時候要小心XD
    ### 這個if是方便起見，如果都>0才要算gcd, 一個是0的話就直接return 1就好，因為是拿來約分用的
    if _a > 0 and _b > 0:
        return _gcd(_a, _b)
    else:
        return 1

def simplify(up, down): # 約分
    up_down_gcd = gcd(up, down)
    return up//up_down_gcd, down//up_down_gcd # 應該單純到不用馬吧…XD

# 把 float string 轉換，return int_value 和 float string 的 長度
# 這個函數是會接收到 例如 "1.2" 用 split('.') 的 latter one 然後回傳 value=2, len=1
# "1." 的case就要小心惹 要回傳啥呢？
def handle_float(float_num_str): 
    # ...
    return float_num, float_len
# 題目敘述的第一種，整數直接轉換然後分母放1（應該不用馬XD
def convert_type1(s): # int
    return int(s), 1

# 題目敘述的第二種，單純的拆成 整數部分、小數部分來處理
def convert_type2(s): # no repeat
    # split 成 整數、小數
    integer_part, float_part = s.split('.')
    # 整數
    integer_part = int(integer_part)
    # 小數
    non_repeating_part, non_repeating_len = handle_float(non_repeating_part)
    # 從整數和小數算出假分數的 分子up、分母down
    down = ...
    up = ...
    return simplify(up, down) # 最後回傳

# 題目敘述的第三種，拆成 整數、小數、循環小數來處理
def convert_type3(s): # with repeat
    # split 成 整數、小數
    integer_part, float_part = s.split('.')
    # 整數
    integer_part = int(integer_part)
    # 拆成小數、循環小數
    non_repeating_part, repeating_part = float_part.split('(')
    # 處理小數
    non_repeating_part, non_repeating_len = handle_float(non_repeating_part)
    # 處理循環小數
    repeating_part, repeating_len = handle_float(repeating_part[:-1]) # -1 for stripping ')'
    # handle .(0) or .() 
    ...
    # 然後從整數和小數算出假分數的 分子up、分母down
    down = ...
    up = ...
    return simplify(up, down)

# entry function: 單純判斷字串裡有啥特徵就call哪個
def convert(s):
    ...

# 下面就題目給的template 然後就call上面的function
class Solution:

    def isRationalEqual(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s_up, s_down = convert(S)
        t_up, t_down = convert(T)
        return (s_up == t_up) and (s_down == t_down) # 回傳的value和"分子分母都一樣"等價
        