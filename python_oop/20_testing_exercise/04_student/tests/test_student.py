from project.student import Student

from unittest import TestCase, main


class StudentTests(TestCase):
    def setUp(self) -> None:
        self.student = Student("No Name", {"Math": ["note0"]})

    def test_constructor_without_initial_courses(self):
        student = Student("No Name")
        self.assertEqual("No Name", student.name)
        self.assertEqual({}, student.courses)

    def test_constructor_with_course_added(self):
        self.assertEqual("No Name", self.student.name)
        self.assertEqual({'Math': ['note0']}, self.student.courses)

    def test_enroll_to_existing_course(self):
        result = self.student.enroll("Math", ["note1", "note2"])
        expected = "Course already added. Notes have been updated."
        self.assertEqual(expected, result)
        self.assertEqual(["note0", "note1", "note2"], self.student.courses["Math"])

    def test_enroll_in_non_existing_course_with_notes(self):
        result = self.student.enroll("Flask", ["note1", "note2"])
        expected = "Course and course notes have been added."
        self.assertEqual(expected, result)
        self.assertTrue(self.student.courses.get("Flask"))
        self.assertEqual(["note1", "note2"], self.student.courses["Flask"])

    def test_enroll_in_non_existing_course_with_notes_Y(self):
        result = self.student.enroll("Flask", ["note1", "note2"], "Y")
        expected = "Course and course notes have been added."
        self.assertEqual(expected, result)
        self.assertTrue(self.student.courses.get("Flask"))
        self.assertEqual(["note1", "note2"], self.student.courses["Flask"])

    def test_enroll_in_non_existing_course_without_notes(self):
        result = self.student.enroll("Flask", None, "N")
        expected = "Course has been added."
        self.assertEqual(expected, result)
        self.assertIsNotNone(self.student.courses.get("Flask"))
        self.assertEqual([], self.student.courses["Flask"])

    def test_add_notes_to_non_existing_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("Flask", "note")
        expected = "Cannot add notes. Course not found."
        self.assertEqual(expected, str(ex.exception))

    def test_add_notes_to_existing_course(self):
        self.student.enroll("Flask", None, "N")
        result = self.student.add_notes("Flask", "note")
        expected = "Notes have been updated"
        self.assertEqual(expected, result)
        self.assertEqual(["note"], self.student.courses.get("Flask"))

    def test_leave_non_existing_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("Physics")
        expected = "Cannot remove course. Course not found."
        self.assertEqual(expected, str(ex.exception))

    def test_leave_course(self):
        result = self.student.leave_course("Math")
        expected = "Course has been removed"
        self.assertEqual(expected, result)
        self.assertIsNone(self.student.courses.get("Math"))


if __name__ == "__main__":
    main()
