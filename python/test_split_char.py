##
# @file test_split_char.py
#
# Test driver for split char
#
# @author Michael John Decker, Ph.D.
from function import split_char

test_cases = 0
test_passed = 0

def run_test(input, expected) :

    answer = split_char(*input)

    print('split_char(' + repr(input[0]) + ', ' + repr(input[1]) + '): ', answer, '==', expected)

    globals()['test_cases'] += 1
    if answer == expected :
        globals()['test_passed'] += 1

def print_test_results(str) :
    print(str, 'results:', globals()['test_passed'], 'out of', globals()['test_cases'])

run_test(('', ','), [''])

run_test(('a', ','), ['a'])
run_test(('abc', ','), ['abc'])
run_test(('abc', 'b'), ['a', 'c'])
run_test(('abcdef', 'd'), ['abc', 'ef'])

run_test(('Name,ID,Midterm,Final', ','), ['Name', 'ID', 'Midterm', 'Final'])

run_test((',ab,c', ','), ['', 'ab', 'c'])
run_test(('ab,,c', ','), ['ab', '', 'c'])
run_test(('ab,c,', ','), ['ab', 'c', ''])

run_test(('abaaca', 'a'), ['', 'b', '', 'c', ''])



print_test_results('split_char')
