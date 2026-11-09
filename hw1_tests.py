"""CSC 1001 - Programming Assignment 1: student-written unit tests.

Create at least TWO separate, meaningful unit tests for each function.
The sixteen methods below are ONLY PLACEHOLDERS: they are not real tests.

Replace each self.fail(...) with test inputs, a call to the appropriate
hw1 function, and unittest assertions about its expected output.
Use methods like self.assertEqual(...) or self.assertAlmostEqual(...).

IMPORTANT: The initial test failures are intentional until you write tests
and implement the functions in hw1.py. Do not simply delete the tests.
"""

import unittest

import data
import hw1


class TestHomework1(unittest.TestCase):

    # Part 1: vowel_count
    def test_vowel_count_case_insensitive(self):
        self.assertEqual(2, hw1.vowel_count("Apple"))

    def test_vowel_count_empty_string(self):
        self.assertEqual(0, hw1.vowel_count(""))

    # Part 2: short_lists
    def test_short_lists_mixed_lengths(self):
        self.assertEqual([[2, 3], [7, 8]], hw1.short_lists([[1], [2, 3], [], [4, 5, 6], [7, 8]]))

    def test_short_lists_no_matching_lengths(self):
        self.assertEqual([], hw1.short_lists([[], [1], [2, 3, 4]]))

    # Part 3: ascending_pairs
    def test_ascending_pairs_reversed_pairs(self):
        self.assertEqual([[2, 9], [3, 1, 2], [5, 5]], hw1.ascending_pairs([[9, 2], [3, 1, 2], [5, 5]]))

    def test_ascending_pairs_other_lengths_unchanged(self):
        self.assertEqual([[1], [3, 2, 1], []], hw1.ascending_pairs([[1], [3, 2, 1], []]))

    # Part 4: add_prices
    def test_add_prices_no_cents_carry(self):
        self.assertEqual(data.Price(5, 70), hw1.add_prices(data.Price(3, 20), data.Price(2, 50)))

    def test_add_prices_with_cents_carry(self):
        self.assertEqual(data.Price(6, 25), hw1.add_prices(data.Price(3, 75), data.Price(2, 50)))

    # Part 5: rectangle_area
    def test_rectangle_area_standard_rectangle(self):
        rectangle = data.Rectangle(data.Point(1, 5), data.Point(4, 1))
        self.assertEqual(12, hw1.rectangle_area(rectangle))



    def test_rectangle_area_negative_coordinates(self):
        rectangle = data.Rectangle(data.Point(-4, 3), data.Point(2, -2))
        self.assertEqual(30, hw1.rectangle_area(rectangle))

    # Part 6: books_by_author
    def test_books_by_author_matching_authors(self):
        book_one = data.Book(["Ada"], "First Book")
        book_two = data.Book(["Ada", "Grace"], "Second Book")
        book_three = data.Book(["Grace"], "Third Book")
        books = [book_one, book_two, book_three]

        self.assertEqual([book_one, book_two], hw1.books_by_author("Ada", books))

    def test_books_by_author_no_matches(self):
        self.assertEqual([], hw1.books_by_author("Linus", []))

    # Part 7: circle_bound
    def test_circle_bound_square(self):
        rectangle = data.Rectangle(data.Point(0, 2), data.Point(2, 0))
        expected = data.Circle(data.Point(1, 1), 2 ** 0.5)
        self.assertEqual(expected, hw1.circle_bound(rectangle))

    def test_circle_bound_non_square_rectangle(self):
        rectangle = data.Rectangle(data.Point(-2, 3), data.Point(4, -1))
        expected = data.Circle(data.Point(1, 1), 13 ** 0.5)
        self.assertEqual(expected, hw1.circle_bound(rectangle))

    # Part 8: below_pay_average
    def test_below_pay_average_different_pay_rates(self):
        employees = [data.Employee("Alex", 10), data.Employee("Blair", 20), data.Employee("Casey", 30),]

        self.assertEqual(["Alex"], hw1.below_pay_average(employees))

    def test_below_pay_average_empty_list(self):
        self.assertEqual([], hw1.below_pay_average([]))

if __name__ == '__main__':
    unittest.main()
