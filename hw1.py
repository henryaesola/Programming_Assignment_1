"""CSC 1001 - Programming Assignment 1.

Student starter file. Implement the eight required functions below.
The provided data types live in data.py; do not edit data.py.

For EVERY function, replace the TODO documentation with a short comment
explaining its purpose, input(s), and output. You may write helper functions.
"""

import data
import math


# Part 1: vowel_count
def vowel_count(text: str) -> int:
    total = 0
    for char in text:
        if char in "aeiouAEIOU":
         total += 1 
    return total
# Purpose: Count the vowels in a string.
# Input(s): text is the string whose characters will be checked.
# Output: Returns the number of lowercase and uppercase vowels in text.


# Part 2: short_lists
def short_lists(items: list[list[int]]) -> list[list[int]]:
    new_list = []
    
    for nested_list in items:
        if len(nested_list) == 2:
            new_list.append(nested_list)

    return new_list
# Purpose: Create a list containing only nested lists with exactly two integers.
# Input(s): items is a list of lists of integers to examine.
# Output: Returns a new list containing the nested lists from items whose length is 2.


# Part 3: ascending_pairs
def ascending_pairs(items: list[list[int]]) -> list[list[int]]:
    new_list = []
        
    for nested_list in items:
        if len(nested_list) == 2:
            if nested_list[0] > nested_list[1]:
                nested_list[0], nested_list[1] = nested_list[1], nested_list[0]

        new_list.append(nested_list)

    return new_list
# Purpose: Return nested lists with all two-item lists in non-descending order.
# Input(s): items is a list of lists of integers to process.
# Output: Returns a new outer list with each two-item nested list sorted ascending.


# Part 4: add_prices
def add_prices(first: data.Price, second: data.Price) -> data.Price:
    dollars = first.dollars + second.dollars
    cents = first.cents + second.cents

    if cents >= 100:
        dollars += 1
        cents -= 100

    return data.Price(dollars, cents)
# Purpose: Add two prices together.
# Input(s): first and second are Price objects to add.
# Output: Returns a new Price object representing their combined value.


# Part 5: rectangle_area
def rectangle_area(rectangle: data.Rectangle) -> float:
    width = rectangle.bottom_right.x - rectangle.top_left.x
    height = rectangle.top_left.y - rectangle.bottom_right.y
    area = width*height

    return area
# Purpose: Calculate the area of an axis-aligned rectangle.
# Input(s): rectangle is a Rectangle object with top-left and bottom-right points.
# Output: Returns the rectangle's area as a float.


# Part 6: books_by_author
def books_by_author(author: str, books: list[data.Book]) -> list[data.Book]:
    matching_books = []

    for book in books:
        if author in book.authors:
            matching_books.append(book)

    return matching_books
 # Purpose: Find all books written by a specified author.
# Input(s): author is the name to find; books is a list of Book objects to search.
# Output: Returns a list of Book objects whose authors include author.


# Part 7: circle_bound
def circle_bound(rectangle: data.Rectangle) -> data.Circle:
    center_x = (rectangle.top_left.x + rectangle.bottom_right.x) / 2
    center_y = (rectangle.top_left.y + rectangle.bottom_right.y) / 2
    center = data.Point(center_x, center_y)

    x_distance = rectangle.top_left.x - center_x
    y_distance = rectangle.top_left.y - center_y
    radius = math.sqrt(x_distance ** 2 + y_distance ** 2)

    return data.Circle(center, radius)
# Purpose: Create the smallest circle that encloses a rectangle.
# Input(s): rectangle is an axis-aligned Rectangle object.
# Output: Returns a Circle centered at the rectangle's center with a radius
# equal to the distance from that center to a corner.


# Part 8: below_pay_average
def below_pay_average(employees: list[data.Employee]) -> list[str]:
    if employees == []:
        return []

    total_pay = 0
    for employee in employees:
        total_pay += employee.pay_rate

    average_pay = total_pay / len(employees)

    below_average_names = []
    for employee in employees:
        if employee.pay_rate < average_pay:
            below_average_names.append(employee.name)

    return below_average_names
# Purpose: Find the employees whose pay rate is below the average pay rate.
# Input(s): employees is a list of Employee objects to examine.
# Output: Returns a list containing the names of employees paid below average.