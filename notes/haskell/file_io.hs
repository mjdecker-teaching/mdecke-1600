module Main where

import System.IO

main = do {
    in_filename <- getLine;
    out_filename <- getLine;

    in_file <- openFile in_filename ReadMode;
    out_file <- openFile out_filename WriteMode;

    copy_file in_file out_file;

    hClose in_file;
    hClose out_file;
}

copy_file in_file out_file = do {
--  hGetContents closes the file
    -- contents <- hGetContents in_file;
    -- hPutStr out_file contents;

    -- contents <- hGetLine in_file;
    -- hPutStrLn out_file contents;

    contents <- hGetChar in_file;
    hPutChar out_file contents;

    -- does not work with hGetContents as closes file
    -- hIsEOF may not be called on closed file
    done <- hIsEOF in_file;
    if not done
    then copy_file in_file out_file;
    else return ()
}
