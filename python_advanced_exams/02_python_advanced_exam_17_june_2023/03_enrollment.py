# https://judge.softuni.org/Contests/Practice/Index/4081#2

def gather_credits(needed_credits: int, *args: [str, int]):
    courses_enrolled = {}
    for course_name, course_credits in args:
        if needed_credits <= 0:
            break
        if course_name not in courses_enrolled:
            courses_enrolled[course_name] = course_credits
            needed_credits -= course_credits

    if needed_credits <= 0:
        return (f"Enrollment finished! Maximum credits: {sum(courses_enrolled.values())}.\n"
                f"Courses: {', '.join(c for c in sorted(courses_enrolled))}")

    return f"You need to enroll in more courses! You have to gather {needed_credits} credits more."


print(gather_credits(
    80,
    ("Basics", 27),
))

print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))

print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))
