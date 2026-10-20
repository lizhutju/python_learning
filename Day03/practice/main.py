# 完成四个任务：
# 1. 找出所有成绩不低于 90 分的学生。
# 2. 按成绩从高到低排序，成绩相同的学生都应保留。
# 3. 统计出现过多少种不同成绩，尝试使用 set。
# 4. 把成绩统计函数写入 statistics_utils.py，然后从 main.py 中通过 import 调用。

import statistics_utils 

students = [
    {"name": "张三", "score": 85},
    {"name": "李四", "score": 92},
    {"name": "王五", "score": 76},
    {"name": "赵六", "score": 92}
]


def filter_students(students, threshold=90):
    for i in range(len(students)):
        if students[i]["score"] >= threshold:
            yield students[i]["name"]

print(list(filter_students(students)))

def sort_students(students):
    return sorted(students,key=lambda x:x["score"],reverse=True)

print(sort_students(students))


print(statistics_utils.count_unique_scores(students))