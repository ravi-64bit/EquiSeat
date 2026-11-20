import unittest
from unittest.mock import patch

import arrange_algo


class SeatingArrangementTests(unittest.TestCase):
    @patch("arrange_algo.get_rooms", return_value=[("R1", 2, 2)])
    def test_places_every_student_once(self, _get_rooms):
        students = {
            "A001": {"MATH"},
            "A002": {"SCI"},
            "A003": {"SCI"},
            "A004": {"MATH"},
        }
        result = arrange_algo.arrange(students, ["R1"])
        self.assertEqual(len(result), 1)
        room_name, matrix = result[0]
        self.assertEqual(room_name, "R1")
        seated = [student for row in matrix for student in row if student]
        self.assertCountEqual(seated, students.keys())
        self.assertEqual(len(seated), len(set(seated)))

    @patch("arrange_algo.get_rooms", return_value=[("R1", 1, 1)])
    def test_rejects_insufficient_room_capacity(self, _get_rooms):
        with self.assertRaisesRegex(ValueError, "hold only 1"):
            arrange_algo.arrange(
                {"A001": {"MATH"}, "A002": {"SCI"}}, ["R1"]
            )

    @patch("arrange_algo.get_rooms", return_value=[("R1", 2, 2)])
    def test_avoids_shared_subjects_between_neighbours_when_possible(self, _get_rooms):
        students = {
            "A001": {"MATH"},
            "A002": {"SCI"},
            "A003": {"SCI"},
            "A004": {"MATH"},
        }
        _, matrix = arrange_algo.arrange(students, ["R1"])[0]
        for row in range(2):
            for col in range(2):
                current = students[matrix[row][col]]
                for nr, nc in ((row + 1, col), (row, col + 1)):
                    if nr < 2 and nc < 2:
                        neighbour = students[matrix[nr][nc]]
                        self.assertFalse(current.intersection(neighbour))


if __name__ == "__main__":
    unittest.main()
