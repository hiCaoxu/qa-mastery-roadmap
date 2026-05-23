# 创建日期：2026/5/22
"""
知识点：


"""

# ========== 练习代码 ==========
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print('{:2d} * {:2d} = {:2d}'.format(j, i, i*j), end=" ")
#     print()


# def print_nine_nine_table():
#
#     """打印标准的九九乘法表"""
#
#     for i in range(1, 10):
#         for j in range(1, i + 1):
#             print(f'{j:2d} * {i:2d} = {i*j:2d}', end=" ")
#         print()


def bubble_sort(arr):
    n = len(arr)
    # 外层循环控制比较轮数
    for i in range(n - 1):
        # 内层循环进行相邻比较，每轮最后一个是最大的，所以范围逐轮缩小
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
# ========== 运行验证 ==========


if __name__ == "__main__":

    # print_nine_nine_table()
    list_ = bubble_sort([1, 3, 55, 2, 3, 1, 78, 54])
    print(list_)
# ========== 我犯过的错 / 心得 ==========
# -
