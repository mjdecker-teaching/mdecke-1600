-- To my chagrin needs to begin with capital (mixing underscores seems silly, so CamelCase)
-- Names: Case has meaning begin lower is function/value, begin upper is type
module FunctionExamples where

-- conditions
-- also when using interactive becomes difficult
-- evaluates condition, then evaluates else or then
-- Reference to standard operators is not easily found...
number_sign num =
    -- Like Python spacing matters try messing with spacing
    if num < 0
        then "negative"
    -- must have then and else, try removing
    else if num > 0
        then "positive"
        else "zero"


number_case num = 
    -- case num of
    --     42 -> "answer"
    --     5 -> "three"
    --     3 -> "five"
    --     _ -> "default"
    -- Spacing matters unless in {} and ; are used, try messing with this
    case num of
        { 42 -> "answer"; 5 -> "three"; 3 -> "five"; _ -> "default" }


-- You can also piece meal a function and have it match to the correct value
-- Do not try with REPL, how I lost hours of my life...
-- Order is important try swapping order in both of these (both are important)
-- this is equivalent to the case example (translated to case) 
piecemeal_func 42 = "answer"
piecemeal_func 5 = "three"
piecemeal_func 3 = "five"
piecemeal_func _ = "default"

-- Recursion
-- loops are destructive, instead use recursion
-- piece meal (this is kind of nice about Haskell)
factorial 1 = 1
factorial n = n * factorial (n - 1)

-- infinite fibonacci, what is it good for???
fibo prev next = [next] ++ fibo next (prev + next)
