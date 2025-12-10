import unittest
from main import Student, Teacher, AdminStaff

class TestStudent(unittest.TestCase):

    def test_gpa_range(self):
        s = Student("Алексей", 19, "ПМИ-14", 3.8)
        self.assertTrue(0 <= s.gpa <= 4.0)

    def test_student_display(self):
        s = Student("Марина", 20, "ЭК-11", 4.0)
        text = s.display_info()
        self.assertIn("Студент", text)
        self.assertIn("ЭК-11", text)
        self.assertIn("Марина", text)


class TestTeacher(unittest.TestCase):

    def test_teacher_fields(self):
        t = Teacher("Сергей", 45, "Математика", 20)
        self.assertEqual(t.subject, "Математика")
        self.assertEqual(t.experience, 20)

    def test_teacher_display(self):
        t = Teacher("Наталья", 39, "Программирование", 15)
        text = t.display_info()
        self.assertIn("Программирование", text)
        self.assertIn("15", text)


class TestAdminStaff(unittest.TestCase):

    def test_admin_fields(self):
        a = AdminStaff("Игорь", 44, "Завхоз", "Хозяйственный отдел")
        self.assertEqual(a.position, "Завхоз")
        self.assertEqual(a.department, "Хозяйственный отдел")

    def test_admin_display(self):
        a = AdminStaff("Людмила", 41, "HR-специалист", "Отдел кадров")
        text = a.display_info()
        self.assertIn("HR-специалист", text)
        self.assertIn("Отдел кадров", text)


if __name__ == "__main__":
    unittest.main()
