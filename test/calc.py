# 缴费10年， 60岁一次性拿
total = 0
base = 1.04329 # 利率
money = 0.96 # 单位：万

for exponent in range(15, 25):
    total += (base ** exponent) * money

print(total)  # 输出: 22.1164      实际上 22.1170     复利: 3.715%     如果是 20%   4.329%

# 缴费10年， 拿到80岁
total = 0
base = 1.0264 # 利率

for exponent in range(35, 45):
    total += (base ** exponent) * money
print(total)  # 输出: 27.0092      实际上 27.0117     复利: 2.342%     如果是 20%   2.64%

# 缴费10年， 拿到70岁 意外了
total = 0
base = 1.0172 # 利率

for exponent in range(25, 35):
    total += (base ** exponent) * money
print(total)  # 输出: 15.9125      实际上 15.8945     复利: 1.32%       如果是 20%   1.72%


# 因为是保证拿20年，所以万一60岁意外了
total = 0
base = 1.0366 # 利率

for exponent in range(15, 25):
    total += (base ** exponent) * money
print(total) # 输出: 19.4749      实际上 19.4542     复利: 3.05%        如果是 20%   3.66%

