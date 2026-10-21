import csv
from pathlib import Path


def load_students(file_path):
    with open(file_path, newline="", encoding="utf-8-sig") as f:
        # 按表头 name、score 读取，避免把表头当作学生数据。
        reader = csv.DictReader(f)
        students = {row["name"]: int(row["score"]) for row in reader}
    return students


def calculate_statistics(students):
    # 空列表会导致除零错误，这里先做保护。
    if not students:
        return 0, 0.0, 0

    num = len(students)
    ave = sum(students.values()) / num
    max_score = max(students.values())
    return num, ave, max_score


def rank_students(students):
    rank = sorted(students.values(), reverse=True)
    return rank


def print_statistics(num, ave, max_score, rank):
    print("Number of students:", num)
    print("Average score:", ave)
    print("Maximum score:", max_score)
    print("Ranked scores:", rank)


if __name__ == "__main__":
    # 使用脚本所在目录，不受运行命令时所在目录的影响。
    csv_path = Path(__file__).resolve().parent / "students.csv"
    students = load_students(csv_path)
    print(students)
    # __main__ 守卫放在文件末尾，模块被 import 时不会执行这一段。
    print_statistics(*calculate_statistics(students), rank_students(students))
