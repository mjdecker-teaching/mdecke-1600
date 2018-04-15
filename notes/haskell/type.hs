{--
 - @file type.hs
 - 
 - Types in Haskell
 - Based on: https://en.wikibooks.org/wiki/Yet_Another_Haskell_Tutorial/Language_basics
 -}

-- :type or :t get type of an expression
:t 'a' == 'b'
:t 'a' == "b"

-- specifies type
:t 42 :: Integer
:t 42 :: Double
-- What do you think it is?
-- Num p => p - if p is an instance of Num class, then 42 can be p
-- Which makes no sense until we talk about type classes
:t 42

-- Warning this is less coding and more theoretical.
-- First lets talk about polymorphic types.
-- Haskell has a polymorphic type system, which basically means
-- it has type variables
-- tail function has a polymorphic types
-- [a] -> [a] take a list of any type
-- and returns a value (->) consisting of a list of that same type
:t tail

-- I alluded to the strictness of fst
-- What do you think this means, (a, b) -> a pair of any types
-- a and b and returns type a
:t fst

-- type classes (like interface/abstract class)
-- Take equality (both sides same type) and supporting overloading
-- (i.e., taking different types)
-- It is defined for some, but not all types
-- This overloading (of equality) can be a problem
-- for static type checking (type checker does not
-- know which types it is defined for)
-- In Haskell, the solution is type classes
-- Define a type class (Eq), associate it with a function
-- If for a type, all functions are implemented
-- then it is an instance of the type class
-- (so basically inheritence/polymorphism)
-- As an example, Int is an instance of Eq.
-- Int/Double are instances of Num (from before),
--    numeric constants can be overloaded (associated to Num)
-- Show class determines what/how certain types are displayed
--:t show is  show :: Show a => a -> String

-- A bit of lambda (a word we heard before
-- calculus (wiki: formal system in mathematical
-- logic for expressing computation based on function
-- abstraction and application using variable binding and substitution
-- For us, simple system for representing functions

-- ƛx.x*x, ƛx means we take a value called x and (after .) multiply by itself.
-- ƛ is the lambda abstraction. lambdas generally take one parameter
-- For two parameter: ƛxƛy.2*x + y
-- lambda are applied by specifying a value to outer lambda like:
-- (ƛx.x*x)5 remove lambda and replace paremeter to get (5 * 5)

-- This is implemented almost directly in Haskell
-- (replace ƛ with \ and . with ->)
square = \x -> x * x
square 5
line = \x y -> 2 * x + y
line 3 4

-- or anonymously
(\x -> x * x)5
(\x y -> 2 * x + y) 3 4

-- "Higher-Order Types" is the name given to those types whose elements are functions. 
-- function types mimick lambda calculus representations
-- *Simplied to be Int type instead of Num type class*
--\x.x*x if x is an Int,then it is a function that takes an Int and produces an Int
-- writen as Int -> Int
-- \x\y.2*x+y - takes an x (Int) produces (a function that takes a y and returns an int)
-- Int -> (Int -> Int) == Int -> Int -> Int

-- What do you think the type of head is? First, think about what it takes and returns
-- then convert to Haskell notation
-- :t head
-- head :: [a] -> a
-- How about snd
-- :t head
-- snd :: (a, b) -> b (not this exact object, just means same type as second argument)
-- +?
-- :t (+) -- paren required because infix
-- (+) :: Num a => a -> a -> a

-- :t putStrLn
-- :t readFile
-- String -> IO() -- IO() is formatted a bit differently to indicate this is not a function
-- they are IO Actions.  IO operations are not pure. Each time user input/read from file
-- it may be different.
main = do
    str <- readFile "read.hs" -- <- gets the string/return out of the IO action/object 
    let out = "read.hs\n" ++ str -- notice no in (not used in do)
    putStrLn out

-- Not functions because they react with "real world" (not my words)
-- Found hilarious, kind of like saying, Haskell, were purely-functional and
-- so, we can't be used to solve any real problems

-- IO () - IO (action) results in () (nothing)
-- do only applies to that scope/block and not sub-scope/blocks
guessing_game num = do
  putStrLn "Enter your guess:"
  guess <- getLine
  case compare (read guess) num of
    LT -> do putStrLn "Too low!"
             guessing_game num
    GT -> do putStrLn "Too high!"
             guessing_game num
    EQ -> putStrLn "You Win!"

-- remember no return-statement, well there is a function return
-- it wraps something in an IO action
let x = return 4
:t x
let x = return 4 in do { y <- x; print y }
4

-- function declarations - may be written separately from definition
-- does not work in ghci
square :: Num a => a -> a
-- considered by some to be good programming practice
-- provide documentation, and can help in clarifying, efficiency, and debugging
square x = x * x
-- can also restrict function to types (specific type may be faster)
square :: Int -> Int

-- May also formally specify parameter type (with -XScopedTypeVariables)
square (x::Int) = x * x -- What's its type?
:t square

-- What about a function argument?  Lets work through map.
-- Take a function, second argument is a list [a], and produces a list
-- so function takes a and produces a b
-- How does this looks?
map :: (a -> b) -> [a] -> [b]
:t map

-- Data Type
-- try with lower pair
-- data defines a data type with name Pair with two "type" parameters.
-- after is the constructor(s), Pair can be different name, but 
-- makes more sense as only constructor
-- says, constructor takes two values (a, b)
data Pair a b = Pair a b
:t Pair -- Pair :: a -> b -> Pair a b
:t Pair 'a' -- Just asking type, won't work as expression otherwise
:t Pair 'A' '1'


-- Can write sanely named functions
-- this is pattern matching the contents of the Pair to x/y
first (Pair x y) = x
second (Pair x y) = y

-- lhs defines types, right side how constructed and stored (the work is done for you)
data Foo a = Foo a a a
first (Foo a b c) = a
second (Foo a b c) = b
third (Foo a b c) = c

first (Foo 3 4 5)
second (Foo 3 4 5)
third (Foo 3 4 5)

-- Some predefined Haskell data types and multiple constructors
-- Something that may contain a value (~ std::optional)
-- Nothing and Just constructor, impl
-- data Maybe a = Nothing -- null constructor
--  | Just a

isNothing Nothing
isJust (Just 1)
fromJust (Just 1)

-- application, searching - it can fail, do not want to crash
find :: Eq a => a -> [a] -> Maybe a
find element [] = Nothing
find element (x:xs) = 
    if x == element
        then Just element
        else find element xs
-- returns Maybe use fromMaybe

-- datatype for one or other
data Either a b = Left a | Right b

-- unit type
data () = () -- like C++ void useful if we get to more complicated IO

-- recursive datatype
data List a = Nil | Concat a (List a)
list_head (Concat first rest) = first
list_tail (Concat first rest) = rest
-- list_head (list_tail (Concat 1 (Concat 2 Nil)))

-- data for declararing enumerated types (multiple constructors)
data Color = Red | Blue | Green -- | Custom Int Int Int

-- type class
class Equal a where 
  -- if operator need in ()
  -- equal     :: a -> a -> Bool
  -- not_equal :: a -> a -> Bool
  equal, not_equal :: a -> a -> Bool
  -- default method for not equal
  x `not_equal` y                =  not (x `equal` y)

-- Instance declarations - declare instance is member of class (type class)
-- Eq type class 

-- minimal complete definition - minimum number of functions that need implemented for class definition to be satisfied
-- Eq requires either of these (negation implements other)
instance Equal Color where
    Red `equal` Red = True
    Blue `equal` Blue = True
    Green `equal` Green = True
    _ `equal` _ = False


instance Eq Color where
    Red == Red = True
    Blue == Blue = True
    Green == Green = True
    _ == _ = False


-- TODO for possibly for someother offering
-- Continuation Passing Style