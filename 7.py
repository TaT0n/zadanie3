# Реализовать замыкание
def mul(a):
    def helper(b):
        return a * b

    return helper


print(mul(5)(2))

mul5 = mul(5)
print(mul5(7))
