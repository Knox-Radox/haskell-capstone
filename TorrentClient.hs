{-# LANGUAGE OverloadedStrings #-}

import Data.List (dropWhileEnd)
import System.Exit (ExitCode(..))
import System.Process (readProcess)
import System.Process (readProcessWithExitCode)

trimTrailingNewline :: String -> String
trimTrailingNewline = dropWhileEnd (`elem` ['\n', '\r'])

downloadChunk :: String -> IO ()
downloadChunk fileHash = do
    let url = "http://127.0.0.1:8080/get/" ++ fileHash
    peerIP <- fmap trimTrailingNewline (readProcess "curl" ["-s", url] "")
    if peerIP == "Not found"
        then putStrLn "File not found in DHT."
        else do
            let fileUrl = "http://" ++ peerIP ++ "/" ++ fileHash
            (wgetCode, _, wgetErr) <- readProcessWithExitCode "wget" [fileUrl] ""
            case wgetCode of
                ExitSuccess -> putStrLn "Download completed successfully."
                ExitFailure _ -> do
                    putStrLn "Download failed: peer server is unreachable or file is unavailable."
                    putStrLn $ "Try restarting the seed server on " ++ peerIP ++ " and run again."
                    if null wgetErr
                        then pure ()
                        else putStrLn wgetErr

main :: IO ()
main = do
    putStrLn "Enter file hash to download:"
    fileHash <- getLine
    downloadChunk fileHash
