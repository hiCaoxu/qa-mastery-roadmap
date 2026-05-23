# 创建日期：2026/5/21
"""
知识点：
print(元素)
将括号内的元素打印在控制台


"""


# ========== 练习代码 ==========
# print('hello world !')
# i = 0
# while i < 5:
#     print('我喜欢你')
#     i += 1

# def salary():
#     salary_one = 1234
#
#     salary_two = 123
#
#     salary_three = 231
#
#     salary_ = salary_three + salary_two + salary_one
#
#     print("我的薪资是{}".format(salary_))

# def salary(salary_three, salary_two, salary_one):
#
#     salary_ = salary_three + salary_two + salary_one
#
#     print("我的薪资是{}".format(salary_))


# def salary(salary_three, salary_two, salary_one=2000):
#
#     salary_ = salary_three + salary_two + salary_one
#
#     print("我的薪资是{}".format(salary_))

# def salary(salary_three, salary_two, *args, salary_one=2000):
#     print("第3薪资：", {salary_three})
#     print("第2薪资：", {salary_two})
#     print("第1薪资：", {salary_one})
#     print("第0薪资：", {*args})
#     salary_ = salary_three + salary_two + salary_one
#     for i in args:
#         salary_ += i
#     print("我的薪资是{}".format(salary_))


# def salary(salary_three, salary_two, salary_one, **kwargs):
#
#     salary_ = salary_three + salary_two + salary_one
#     for i in kwargs:
#         salary_ += kwargs[i]
#     print("我的薪资是{}".format(salary_))

def salary(salary_three, salary_two, *args, salary_one=1000, **kwargs):
    """
     salary_three:
    """
    salary_ = salary_three + salary_two + salary_one
    for i in args:
        salary_ += i
    for i in kwargs:
        salary_ += kwargs[i]
    # print("我的薪资是{}".format(salary_))
    return salary_

# ========== 运行验证 ==========


if __name__ == "__main__":
    result = salary(12000, 3000, 2000, salary_one=200, c=500, b=800)
    print("我的薪资是：", result)

# ========== 我犯过的错 / 心得 ==========
# -
