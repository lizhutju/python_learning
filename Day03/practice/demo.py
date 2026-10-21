# 练习：生成器（generator）与列表推导的对比
#
# 运行方式：python3 demo.py

students = [
    {"name": "张三", "score": 85},
    {"name": "李四", "score": 92},
    {"name": "王五", "score": 76},
    {"name": "赵六", "score": 92}
]


def filter_students(students, threshold=90):
    """用 yield 逐个返回达标学生的名字，调用时才真正开始计算。"""
    for student in students:
        if student["score"] >= threshold:
            yield student["name"]


def main():
    # 1. 生成器对象本身不占位结果，需要用 list() 消费它。
    print("生成器结果:", list(filter_students(students)))

    # 2. 列表推导是等价但更紧凑的写法。
    print("列表推导:", [s["name"] for s in students if s["score"] >= 90])

    # 3. 生成器是惰性的：先拿到对象，执行打印语句时还什么都没算。
    gen = filter_students(students)
    print("尚未消费生成器:", gen)
    print("消费后:", next(gen), "->", next(gen))

    # 4. 用 list() 一次性取完剩余部分。
    print("剩余部分:", list(gen))


if __name__ == "__main__":
    main()
