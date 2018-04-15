##
# @file test_binary_search.py
#
# Test driver for binary search
#
# @author Michael John Decker, Ph.D.

from function import binary_search

test_cases = 0
test_passed = 0

def run_test(str, answer, expected) :
    print(str, answer, '==', expected)

    globals()['test_cases'] += 1
    if answer == expected :
        globals()['test_passed'] += 1

def print_test_results(str) :
    print(str, 'results:', globals()['test_passed'], 'out of', globals()['test_cases'])

list_one = [0, 1, 2, 3, 4, 5, 6, 7, 8]
run_test('binary_search(list_one, 4, 0) =', binary_search(list_one, 4, 0), 4)
run_test('binary_search(list_one, 0, 0) =', binary_search(list_one, 0, 0), 0)
run_test('binary_search(list_one, 8, 0) =', binary_search(list_one, 8, 0), 8)
run_test('binary_search(list_one, -1, 0) =', binary_search(list_one, -1, 0), None)
run_test('binary_search(list_one, 9, 0) =', binary_search(list_one, 9, 0), None)

list_two = [0, 1, 2, 3, 4, 5, 6, 7]
run_test('binary_search(list_two, 3, 0) =', binary_search(list_two, 3, 0), 3)
run_test('binary_search(list_two, 4, 0) =', binary_search(list_two, 4, 0), 4)
run_test('binary_search(list_two, 0, 0) =', binary_search(list_two, 0, 0), 0)
run_test('binary_search(list_two, 7, 0) =', binary_search(list_two, 7, 0), 7)
run_test('binary_search(list_two, -1, 0) =', binary_search(list_two, -1, 0), None)
run_test('binary_search(list_two, 8, 0) =', binary_search(list_two, 8, 0), None)

list_three = [1, 5, 9, 13]
run_test('binary_search(list_three, 3, 0) =', binary_search(list_three, 3, 0), None)
run_test('binary_search(list_three, 7, 0) =', binary_search(list_three, 7, 0), None)
run_test('binary_search(list_three, 11, 0) =', binary_search(list_three, 11, 0), None)


list_four = [1, 5, 9, 13, 17]
run_test('binary_search(list_four, 3, 0) =', binary_search(list_four, 3, 0), None)
run_test('binary_search(list_four, 7, 0) =', binary_search(list_four, 7, 0), None)
run_test('binary_search(list_four, 11, 0) =', binary_search(list_four, 11, 0), None)
run_test('binary_search(list_four, 15, 0) =', binary_search(list_four, 15, 0), None)

print_test_results('binary_search')
