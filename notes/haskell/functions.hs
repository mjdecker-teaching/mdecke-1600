
---
-- @file functions.hs
--
-- Functions in Haskell programming based on: 
--  * https://en.wikipedia.org/
--  * https://www.haskell.org
--      * https://www.haskell.org/documentation
--      * https://wiki.haskell.org/Haskell_in_5_steps
--  * https://en.wikibooks.org/wiki/Yet_Another_Haskell_Tutorial
--  * http://www.seas.upenn.edu/~cis194/fall16/lectures (person really loves Haskell)
-- @author Michael John Decker, Ph.D.

-- import
-- say we want to sort
-- not defined..
sort [5, 4, 3, 2, 1]

-- we need to import it first or call by full name
-- https://downloads.haskell.org/~ghc/latest/docs/html/libraries/
Data.List.sort [5, 4, 3, 2, 1]
import Data.List
sort [5, 4, 3, 2, 1]

-- simple list functions 

-- map is same as Python
-- map function_name list
map (+1) [1, 2, 3, 4, 5]
map Data.Char.toUpper "loud noises"


-- filter - create a list filtering out based on function
-- filter function_name list
filter Data.Char.isLower "Eiffel Tower"

-- folding  run through a list applying a function and accumulating a result
-- sort of like taking list expanded form (3 : 8 : 12 : 5 : []) 
-- and replacing : with function parameter and [] with initial value (for foldr, : is right associative)

-- foldr - accumulate from right
-- fold operation initial list
foldr (+) 0 [8, 6, 7, 5, 3, 0, 9]
-- 8 + 6 + 7 + 5 + 3 + 0 + 9 + 0

-- What about associativity?
-- fold goes right to left (right-associative)
-- non-associtive op
foldr (-) 1 [8, 6, 7, 5, 3, 0, 9]
--  (8 - (6 - (7 - (5 - (3 - (0 - (9 - 1)))))))

-- What if we want left-associate
-- foldl - accumulate from left
-- same as + is associative
foldl (+) 0 [8, 6, 7, 5, 3, 0, 9]

-- different as - is not associative
foldl (-) 1 [8, 6, 7, 5, 3, 0, 9]
-- (((((((1 - 8) - 6) - 7) - 5) - 3) - 0) - 9)

-- foldl is generally more efficient (but does not force eval until), but can't work on infinite lists (foldr can).  More on this later...
-- do not apply foldl to large list (story of breaking my computer)

-- function defining
-- name args = body
-- notice there is no explicit return statement,
-- just this is what it evaluate to
square x = x * x
square 13

-- multiple parameters
add x y = x + y
add 9 3

-- :load function_examples (or :l or :reload or :r) (or pass on command line)
-- if-statement
number_sign 42
number_sign 0
-- number_sign -1
-- need () as things number_sign - 1
number_sign (-1)

-- case
number_case 42
number_case 3
number_case 5
number_case 100000

-- piece meal function
piecemeal_func 42
piecemeal_func 3
piecemeal_func 5
piecemeal_func 100000

-- . operator (function composition)
-- creates new function applying right to left
sub1 x = x - 1
(sub1 . square) 5
(square . sub1) 5

-- other functions
-- is list empty
null []
null [1]

1 == 1
-- this is not equal (!=), not divide equal
3 /= 5

-- let function (make sure exit enter ghci)
let add x y = x + y in add 1 2
-- add does not exit

-- infix
-- + (and other symbols) are infix
-- to call like function
(+) 3 5

-- non-infix made infix with back ticks
(+1) `map` [1,2,3,4,5]

-- Recursion
factorial 1
factorial 10

-- basic pattern matching
-- What does x : xs?  What might you think if applied to 
-- to a single array (as pattern). We get the head and tail!
list_head (x:xs) = x
list_tail (x:xs) = xs

list_head [1,2,3]
list_tail [1,2,3]

-- Lazy fibonacci, infinitely long, but only use a little (never fully evaluated) only portion used calculated
-- Never ends
-- fibo 0 1
-- only needs 10 computes (reads only first 10)
-- might be represented as cyclic graph, so small memory usage, values generated when read
take 10 (fibo 0 1)
