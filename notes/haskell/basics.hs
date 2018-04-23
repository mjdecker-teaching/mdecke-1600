---
-- @file basics.hs
--
-- Basic Haskell programming based on: 
--  * https://en.wikipedia.org/
--  * https://www.haskell.org
--      * https://www.haskell.org/documentation
--      * https://wiki.haskell.org/Haskell_in_5_steps
--  * https://en.wikibooks.org/wiki/Yet_Another_Haskell_Tutorial
--  * http://www.seas.upenn.edu/~cis194/fall16/lectures (person really loves Haskell)
-- @author Michael John Decker, Ph.D.
--

-- Python gave us an intepretted and dynamically typed language
-- Python also had functional constructs which will give us a 
-- nice segue into a functional programming language (Haskell)
-- Warning: Some Haskel programmers tend to have exaggerated love for language.
--          Some caution may be warranted.
--
-- Haskell:
--  * Created in 1990
--  * Uses the file extensions: hs and lhs
--  * Purely functional:
--      * Treats all computation as the evaluation of mathematical functions
--      * Forbids changing-state and mutable data
--  * Expressions are referential transparent
--      * expression can always be replaced with its value without changing behavior
--
--  *   These mean that: no side, calling same function with same arguments
--      always results in same answer
--  * Evaluates Lazily - expressions not evaluated until results required/referenced
--      * Can avoid repeated evaluation due to sharing
--  * Statically typed, which means?
--  * Strongly typed
--
-- A benefit of this is that it is easy to parallelize

-- Install
-- Haskell Platform - https://www.haskell.org/downloads
--  * Windows (un-developer friendly OS) - Full
--
-- Warning the REPL (ghci) is terrible for multiple line code (not using it will save hours of your life)
-- 

-- I showed LISP syntax previously, in contrast to the beautifully simple
-- LISP syntax, Haskell is much more syntax


{- 
 Hello World
 This be a function, notice parenthesis are not required
-}
main = putStrLn "Hello World"

-- Compiling: ghc basics.hs -o basics (windows basics.exe)
-- Generates .hi (Interface file; contains information about exported symbols), .o (object file)

-- Haskell as a Calculator
-- quit with :quit
-- Supports +, -, /, ^ (exponent), sqrt
-- Order?  Typical. Will not show table for now as uses unfamilar words.
3 - 5 * 9
2^16 - 1
-- discovery/proof of irrational numbers may have caused the death of some people
sqrt 2
-- Which evaluates first function or * (can use parenthesis to make clearer)
sqrt 4 * 4
-- can group by parenthesis
(3 - 5) * 9
-- What do we get?
3 / 7
-- What does this tell you?
2^9001
-- Three Numeric types: Int (machine-sized), Integer (infinite precision), Double (double precision floating point)
-- We will get back to figuring out types

-- is a comment
3 / 7 -- also a comment

{- 
    This is a block comment.
    {- They can be nested -}
-}

-- let binds a variable allowing you to reference it more than once
-- let var = expression in body
let answer = 42 in print answer
let length = 4 in length * length
-- You can have multiple variables
let base = 2; exponent = 16 in base ^ exponent



-- lists
[42, 9001, 3]
3 : []
2 : [3]
1 : [2, 3]
-- right to left (function cons, taken from lisp)
1 : 2 : []
-- Syntactic sugar for 1 : 2 : []
[1, 2, 3]
1 : 2 : [] == [1, 2, 3]

-- What this type? Yep, a Char
'c'
:type 'c'

-- concat
[1, 2] ++ [3, 4]

-- Strings are syntactic sugar for Char lists
'a' : 'b' : 'c' : []
['a', 'b', 'c']
"abc"
'a' : 'b' : 'c' : [] == "abc"
['a', 'b', 'c'] == "abc"
:type "abc"

-- concat
"Hello " ++ "World!!!"

-- to/from string
"Answer = " ++ show (7 * 6)
read "7" * 6
-- can't convert error
-- read "foo"


-- How about this statement? lists elements must be same type
-- [1, 'a']

-- simple list functions (get random numbers from students)
length [1, 2, 3, 4, 5]
-- lisp (car list)
head [1, 2, 3, 4, 5]
-- lisp (cdr list)
tail [1, 2, 3, 4, 5]
-- What does this give?
head (tail [1, 2, 3, 4, 5])
-- without (), treats tail as arg
-- head tail [1, 2, 3, 4, 5]

-- Tuples
(3060, "Programming Languages")
-- Get first/second of a pair
-- Do you think fst and snd are good names
-- No, not really, although there are claims it must be short because its used often
-- But, that is why should not be shortened...
fst (3060, "Programming Languages")
snd (3060, "Programming Languages")

-- Tuples are variable in size
(3060, "Programming Languages", "Michael John Decker")
-- Error: fst (3060, "Programming Languages", "Michael John Decker")

-- Lists are homonogeneous, tuples heterogeneous
-- Lists and tuples can contain lists or tuples
([4], (2, "word")) -- a concordance entry?
[[1, 2], [3, 4]]
[(1, "fish"), (2, "fish")]
-- What do you think happens here? Not same element type
[(1, "two"), ("three", 4)]
