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

class Solution:
    def nthMagicalNumber(self, N, A, B):
        """
        :type N: int
        :type A: int
        :type B: int
        :rtype: int
        """
        lcm_of_A_B = (A * B // gcd(A, B))
        lcm_magic_num = lcm_of_A_B // A + lcm_of_A_B // B - 1 # magic num of lcm
        lcm_part_sum = lcm_of_A_B * (N // lcm_magic_num)
        N_after_removing_lcm = N % lcm_magic_num

        # N_after_removing_lcm numbers more to go, current sum is lcm_part_sum
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