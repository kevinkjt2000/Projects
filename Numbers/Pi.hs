-- This program will display pi to the nth digit.
-- n is given to the program as a command line argument.

import System.Environment
import System.Exit

usage = do name <- getProgName
           putStrLn $ "Usage: " ++ name ++ " n"
exit = exitWith ExitSuccess
die  = exitWith $ ExitFailure 1

piToThe n = 3

main = do
    args <- getArgs
    if 1 /= length args
    then
        usage >> exit
    else do
        let n = read $ head args :: Int
        print $ piToThe n
        exit
