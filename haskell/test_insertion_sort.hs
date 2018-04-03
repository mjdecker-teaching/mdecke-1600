module Main where

import Function
import Test.HUnit

test1 = TestCase (assertEqual "insetion_sort []:" [] (insertion_sort []::[Int]))
test2 = TestCase (assertEqual "insetion_sort [1]:" [1] (insertion_sort [1]))
test3 = TestCase (assertEqual "insetion_sort [1, 2]:" [1, 2] (insertion_sort [1, 2]))
test4 = TestCase (assertEqual "insetion_sort [2, 1]:" [1, 2] (insertion_sort [2, 1]))

test5 = TestCase (assertEqual "insetion_sort [11, 10, 7, 0, -1, -10]:" [-10, -1, 0, 7, 10, 11] (insertion_sort [11, 10, 7, 0, -1, -10]))
test6 = TestCase (assertEqual "insetion_sort [15, 11, 10, 7, 0, -1, -10]:" [-10, -1, 0, 7, 10, 11, 15] (insertion_sort [15, 11, 10, 7, 0, -1, -10]))

test7 = TestCase (assertEqual "insetion_sort [0, 7, 11, 10, -1, -10]:" [-10, -1, 0, 7, 10, 11] (insertion_sort [0, 7, 11, 10, -1, -10]))
test8 = TestCase (assertEqual "insetion_sort [0, 7, 15, 11, 10, -1, -10]:" [-10, -1, 0, 7, 10, 11, 15] (insertion_sort [0, 7, 15, 11, 10, -1, -10]))


tests = TestList 
    [
        TestLabel "test1" test1, 
        TestLabel "test2" test2,
        TestLabel "test3" test3, 
        TestLabel "test4" test4,
        TestLabel "test5" test5, 
        TestLabel "test6" test6,
        TestLabel "test7" test7, 
        TestLabel "test8" test8
    ]

main = do 

    runTestTT tests



