# https://judge.softuni.org/Contests/Practice/Index/3744#2

def students_credits(*args: str):
    courses = {}
    for arg in args:
        # {course name}-{credits}-{max test points}-{diyan's points}
        course_name, course_credits, max_points, points_achieved = arg.split("-")
        if course_name not in courses:
            courses[course_name] = []
        courses[course_name] = int(course_credits) * int(points_achieved) / int(max_points)

    total_credits = sum(courses.values())
    if total_credits >= 240:
        result = f"Diyan gets a diploma with {total_credits:.1f} credits.\n"
    else:
        result = f"Diyan needs {240 - total_credits:.1f} credits more for a diploma.\n"

    for course, credit in sorted(courses.items(), key=lambda x: -x[1]):
        result += f"{course} - {credit:.1f}\n"

    return result


# print(
#     students_credits(
#         "Computer Science-12-300-250",
#         "Basic Algebra-15-400-200",
#         "Algorithms-25-500-490"
#     )
# )

print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)