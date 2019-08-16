#第二个练习 - 使用raise语句抛出异常
def division():
    print("=====================分苹果了=====================")
    apple = int(input("请输入苹果的个数："))
    children = int(input("请输入来了几个小朋友："))
    if apple < children:
        raise ValueError("苹果太少了，不够分...")
    result = apple // children
    remain = apple - result * children
    if remain > 0:
        print(apple, "个苹果，平均分给", children, "个小朋友，每人分", result, "个，剩余", remain, "个。")
    else:
        print(apple, "个苹果，平均分给", children, "个小朋友，每人分", result, "个。")
if __name__ == '__main__':
    try:
        division()
    except ZeroDivisionError:
        print("出错了~~~，苹果不能被0个小朋友分。")
    except ValueError as e:
        print("输入错误：", e)
    else:
        print("分苹果顺利完成。")
    finally:
        print("进行了一次苹果分配。")