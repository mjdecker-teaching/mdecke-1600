##
# @file test_insertion_sort.py
#
# Test driver for insertion sort
#
# @author Michael John Decker, Ph.D.
from function import insertion_sort

test_cases = 0
test_passed = 0

def run_test(input, expected) :

    answer = input[:]
    insertion_sort(answer)

    print('insertion_sort(' + str(input) + '): ', answer, '==', expected)

    globals()['test_cases'] += 1
    if answer == expected :
        globals()['test_passed'] += 1

def print_test_results(str) :
    print(str, 'results:', globals()['test_passed'], 'out of', globals()['test_cases'])

run_test([], [])
run_test([1], [1])
run_test([1, 2], [1, 2])
run_test([2, 1], [1, 2])

run_test([11, 10, 7, 0, -1, -10], [-10, -1, 0, 7, 10, 11])
run_test([15, 11, 10, 7, 0, -1, -10], [-10, -1, 0, 7, 10, 11, 15])

run_test([0, 7, 11, 10, -1, -10], [-10, -1, 0, 7, 10, 11])
run_test([0, 7, 15, 11, 10, -1, -10], [-10, -1, 0, 7, 10, 11, 15])

print_test_results('insertion_sort')
