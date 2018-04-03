module Main where

import Function
import Test.HUnit

test1 = TestCase (assertEqual "split_char \"\" ','" [""] (split_char "" ','))

test2 = TestCase (assertEqual "split_char \"a\" ','" ["a"] (split_char "a" ','))
test3 = TestCase (assertEqual "split_char \"abc\" ','" ["abc"] (split_char "abc" ','))
test4 = TestCase (assertEqual "split_char \"abc\" 'b'" ["a", "c"] (split_char "abc" 'b'))
test5 = TestCase (assertEqual "split_char \"abcdef\" 'd'" ["abc", "ef"] (split_char "abcdef" 'd'))

test6 = TestCase (assertEqual "split_char \"Name,ID,Midterm,Final\" ','" ["Name", "ID", "Midterm", "Final"] (split_char "Name,ID,Midterm,Final" ','))

test7 = TestCase (assertEqual "split_char \",ab,c\" ','" ["", "ab", "c"] (split_char ",ab,c" ','))
test8 = TestCase (assertEqual "split_char \"ab,,c\" ','" ["ab", "", "c"] (split_char "ab,,c" ','))
test9 = TestCase (assertEqual "split_char \"ab,c,\" ','" ["ab", "c", ""] (split_char "ab,c," ','))

test10 = TestCase (assertEqual "split_char \"abaaca\" 'a'" ["", "b", "", "c", ""] (split_char "abaaca" 'a'))

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
        TestLabel "test7" test9, 
        TestLabel "test8" test10
    ]

main = do 

    runTestTT tests



