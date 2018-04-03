module Main where

import Function
import Test.HUnit

list_one = [0, 1, 2, 3, 4, 5, 6, 7, 8]
test1 = TestCase (assertEqual "binary_search list_one, 4, 0: " 4 (binary_search list_one 4 0))

test2 = TestCase (assertEqual "binary_search list_one 0 0: " 0 (binary_search list_one 0 0))
test3 = TestCase (assertEqual "binary_search list_one 8 0: " 8  (binary_search list_one 8 0))
test4 = TestCase (assertEqual "binary_search list_one (-1) 0: " (-1) (binary_search list_one (-1) 0))
test5 = TestCase (assertEqual "binary_search list_one 9 0: " (-1) (binary_search list_one 9 0))

list_two = [0, 1, 2, 3, 4, 5, 6, 7]
test6 = TestCase (assertEqual "binary_search list_two 3 0: " 3 (binary_search list_two 3 0))
test7 = TestCase (assertEqual "binary_search list_two 4 0: " 4 (binary_search list_two 4 0))
test8 = TestCase (assertEqual "binary_search list_two 0 0: " 0 (binary_search list_two 0 0))
test9 = TestCase (assertEqual "binary_search list_two 7 0: " 7 (binary_search list_two 7 0))
test10 = TestCase (assertEqual "binary_search list_two (-1) 0: " (-1) (binary_search list_two (-1) 0))
test11 = TestCase (assertEqual "binary_search list_two 8 0: " (-1) (binary_search list_two 8 0))

list_three = [1, 5, 9, 13]
test12 = TestCase (assertEqual "binary_search list_three 3 0: " (-1) (binary_search list_three 3 0))
test13 = TestCase (assertEqual "binary_search list_three 7 0: " (-1) (binary_search list_three 7 0))
test14 = TestCase (assertEqual "binary_search list_three 11 0: " (-1) (binary_search list_three 11 0))


list_four = [1, 5, 9, 13, 17]
test15 = TestCase (assertEqual "binary_search list_four 3 0: " (-1) (binary_search list_four 3 0))
test16 = TestCase (assertEqual "binary_search list_four 7 0: " (-1) (binary_search list_four 7 0))
test17 = TestCase (assertEqual "binary_search list_four 11 0: " (-1) (binary_search list_four 11 0))
test18 = TestCase (assertEqual "binary_search list_four 15 0: " (-1) (binary_search list_four 15 0))

tests = TestList 
    [
        TestLabel "test1" test1, 
        TestLabel "test2" test2,
        TestLabel "test3" test3, 
        TestLabel "test4" test4,
        TestLabel "test5" test5, 
        TestLabel "test6" test6,
        TestLabel "test7" test7, 
        TestLabel "test8" test8,
        TestLabel "test9" test9, 
        TestLabel "test10" test10,
        TestLabel "test11" test11, 
        TestLabel "test12" test12,
        TestLabel "test13" test13, 
        TestLabel "test14" test14,
        TestLabel "test15" test15, 
        TestLabel "test16" test16,
        TestLabel "test17" test17, 
        TestLabel "test18" test18
    ]

main = do 

    runTestTT tests



