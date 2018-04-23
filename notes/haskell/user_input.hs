{--
 - @file user_input.hs
 - 
 - Shows interactive IO in Haskell
 - Based on: https://en.wikibooks.org/wiki/Yet_Another_Haskell_Tutorial/Language_basics
 -}
module Main where

import System.IO
import System.Random

-- Is a function that takes input a function.  No.

-- do-expression (sequence of 'statements') allows specify order of operations 
-- Due to lazy evaluation, normally unspecified order
-- do block allows, 1) computation binding to a variable  with <-,
-- 2) ignoring returns, 3) let without an in to introduce binding
main = do
  hSetBuffering stdin LineBuffering
  putStrLn "What's your name?"
  -- <- instead of = to highlight getLine is not a function
  -- IO action
  name <- getLine
  putStrLn ("Your name is " ++ name)
  -- needs to be on own line before
  -- ::Int specifies type
  --number <- randomRIO (1::Int, 100)
  --putStrLn ("Your luck number is: " ++ show(number))
-- another example of not a function, is one that returns a random value


