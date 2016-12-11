module Main
{- Collatz Conjecture
Start with a number n > 1
Find the number of steps it takes to reach 1
using the following process:
If n is even, divide it by 2.
If n is odd, multiply it by 3 and add 1.
-}

collatz_conjecture : Integer -> Integer
collatz_conjecture n =
  case n `mod` 2 of
       0 => n `div` 2
       1 => n * 3 + 1

collatz_conjecture_counter : Integer -> Integer
collatz_conjecture_counter 1 = 0
collatz_conjecture_counter n = 1 + collatz_conjecture_counter (collatz_conjecture n)

range : Integer -> List Integer
range 0 = []
range x = x :: range (x - 1)

main : IO ()
main = let answers = map collatz_conjecture_counter (range 20) in
  putStrLn $ show answers
 
