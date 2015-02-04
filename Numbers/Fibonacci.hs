-- This program will generate the Fibonacci sequence up to the nth term
-- n is given to the program as a command line argument.

import System.Environment
import System.Exit

usage = do name <- getProgName
           putStrLn $ "Usage: " ++ name ++ " n"
exit = exitWith ExitSuccess
die  = exitWith $ ExitFailure 1

fib n a b
    | n > 0 = a:fib (n-1) b (b+a)
    | otherwise = []
fibonacci n = fib n 1 1

main = do
    args <- getArgs
    if 1 /= length args
    then
        usage >> exit
    else do
        let n = read $ head args :: Int
        print $ fibonacci n
        exit
