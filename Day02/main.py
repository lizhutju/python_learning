import csv
from pathlib import Path


def load_students(file_path):
    with open(file_path, newline="", encoding="utf-8-sig") as f:
        # 按表头 name、score 读取，避免把表头当作学生数据。
        reader = csv.DictReader(f)
        students = {row["name"]: int(row["score"]) for row in reader}
    return students


if __name__ == "__main__":
    # 使用脚本所在目录，不受运行命令时所在目录的影响。
    csv_path = Path(__file__).resolve().parent / "students.csv"
    students = load_students(csv_path)
    print(students)

def calculate_statistics(students):
    num = len(students)
    ave = sum(students.values()) / num
    max_score = max(students.values())
    return num, ave, max_score

def rank_students(students):
    rank = sorted(students.values(), reverse=True)
    return rank

def print_statistics(num,ave,max_score,rank):
    print("Number of students:", num)
    print("Average score:", ave)
    print("Maximum score:", max_score)
    print("Ranked scores:", rank)

print_statistics(*calculate_statistics(students), rank_students(students))