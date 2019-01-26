def gcd(_a,_b):
# 求 gcd

class Solution:
    def nthMagicalNumber(self, N, A, B):
        """
        :type N: int
        :type A: int
        :type B: int
        :rtype: int
        """
        # 求最小公倍數 lcm
        lcm_of_A_B = ...
        
        # 算出一次 lcm 可以跳過幾個數字
        lcm_magic_num = ...
        
        # 扣掉找剩下要多少
        lcm_part_sum = ...
        N_after_removing_lcm = ...

        # 問題就變成了已經做了 lcm_magic_num 次的 lcm
        # 目前的數字是 lcm_part_sum 
        # 剩下 N_after_removing_lcm 個數字 直接 暴力解
        A_, B_, remain_value = 0, 0, 0
        for _ in range(N_after_removing_lcm):
            if A_ + A < B_ + B:
                A_ += A
                remain_value = A_
            else:
                B_ += B
                remain_value = B_
        return_value = lcm_part_sum + remain_value
        return int(return_value % (1e9 + 7))