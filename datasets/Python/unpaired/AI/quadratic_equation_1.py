import cmath

def solve_quadratic_equation(a, b, c):
    """二次方程式 ax^2 + bx + c = 0 の解を計算する"""
    # 判別式 D を計算
    D = cmath.sqrt(b**2 - 4*a*c)

    # 二次方程式の解
    x1 = (-b + D) / (2*a)
    x2 = (-b - D) / (2*a)

    return x1, x2

# いくつかのテストケースで方程式の解を計算
# 例: a=1, b=3, c=2 (実数解)
#     a=1, b=2, c=1 (重解)
#     a=1, b=1, c=1 (複素数解)

test_cases = [(1, 3, 2), (1, 2, 1), (1, 1, 1)]
solutions = [solve_quadratic_equation(a, b, c) for a, b, c in test_cases]

solutions

