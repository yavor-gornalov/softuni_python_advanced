from project.student_report_card import StudentReportCard

from unittest import TestCase, main


class StudentReportCardTests(TestCase):
    def setUp(self):
        self.student_report_card = StudentReportCard("John", 12)

    def test_constructor(self):
        self.assertEqual("John", self.student_report_card.student_name)
        self.assertEqual(12, self.student_report_card.school_year)
        self.assertEqual({}, self.student_report_card.grades_by_subject)

    def test_empty_student_name_raises_ve(self):
        with self.assertRaises(ValueError) as ve:
            self.student_report_card.student_name = ""
        expected = "Student Name cannot be an empty string!"
        self.assertEqual(expected, str(ve.exception))

    def test_valid_student_name(self):
        self.student_report_card.student_name = "George"
        self.assertEqual("George", self.student_report_card.student_name)

    def test_school_year_below_limit_raises_ve(self):
        with self.assertRaises(ValueError) as ve:
            self.student_report_card.school_year = 0
        expected = "School Year must be between 1 and 12!"
        self.assertEqual(expected, str(ve.exception))

    def test_school_year_above_limit_raises_ve(self):
        with self.assertRaises(ValueError) as ve:
            self.student_report_card.school_year = 13
        expected = "School Year must be between 1 and 12!"
        self.assertEqual(expected, str(ve.exception))

    def test_school_year_in_expected_range(self):
        self.student_report_card.school_year = 1
        self.assertEqual(1, self.student_report_card.school_year)
        self.student_report_card.school_year = 12
        self.assertEqual(12, self.student_report_card.school_year)

    def test_add_grade_subject_not_in_list(self):
        self.student_report_card.add_grade("Mathematics", 5.5)
        self.assertEqual({"Mathematics": [5.5]}, self.student_report_card.grades_by_subject)

    def test_add_another_grade_to_existing_subject(self):
        self.student_report_card.add_grade("Mathematics", 5.50)
        self.student_report_card.add_grade("Mathematics", 6.00)
        self.assertEqual({"Mathematics": [5.5, 6.0]}, self.student_report_card.grades_by_subject)

    def test_average_grade_by_subject(self):
        self.student_report_card.add_grade("Mathematics", 5.00)
        self.student_report_card.add_grade("Mathematics", 6.00)
        self.student_report_card.add_grade("Physics", 6.00)
        self.assertEqual({"Mathematics": [5.0, 6.0], "Physics": [6.0]}, self.student_report_card.grades_by_subject)

        result = self.student_report_card.average_grade_by_subject()
        expected = "Mathematics: 5.50\nPhysics: 6.00"
        self.assertEqual(expected, result)

    def test_overall_average_grade(self):
        self.student_report_card.add_grade("Mathematics", 5.00)
        self.student_report_card.add_grade("Mathematics", 6.00)
        self.student_report_card.add_grade("Physics", 6.00)
        self.assertEqual({"Mathematics": [5.0, 6.0], "Physics": [6.0]}, self.student_report_card.grades_by_subject)

        result = self.student_report_card.average_grade_for_all_subjects()
        expected = "Average Grade: 5.67"
        self.assertEqual(expected, result)

    def test_repr_method(self):
        self.student_report_card.add_grade("Mathematics", 5.00)
        self.student_report_card.add_grade("Mathematics", 6.00)
        self.student_report_card.add_grade("Physics", 6.00)

        expected = f"Name: John\n" \
                   f"Year: 12\n" \
                   f"----------\n" \
                   f"Mathematics: 5.50\n" \
                   f"Physics: 6.00\n" \
                   f"----------\n" \
                   f"Average Grade: 5.67"
        result = str(self.student_report_card)
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
