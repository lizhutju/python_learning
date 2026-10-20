def count_unique_scores(students):
    scores = set()
    for student in students:
        scores.add(student["score"])
    return len(scores)
