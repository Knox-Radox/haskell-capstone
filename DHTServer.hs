{-# LANGUAGE OverloadedStrings #-}

import Web.Scotty
import Network.Wai.Middleware.RequestLogger (logStdoutDev)
import Control.Monad.IO.Class (liftIO)
import Data.IORef
import Data.List (lookup)
import Data.String (fromString)

type DHT = IORef [(String, String)]  -- Hash Table: file_hash -> peer_ip

upsert :: String -> String -> [(String, String)] -> [(String, String)]
upsert hash ip entries = (hash, ip) : filter ((/= hash) . fst) entries

main :: IO ()
main = do
    dhtRef <- newIORef []
    putStrLn "DHT Node started on port 8080..."
    scotty 8080 $ do
        middleware logStdoutDev

        -- Store a file hash with the peer's IP
        post "/store/:hash/:ip" $ do
            hash <- pathParam "hash" :: ActionM String
            ip <- pathParam "ip" :: ActionM String
            liftIO $ modifyIORef dhtRef (upsert hash ip)
            text $ "Stored " <> (fromString hash) <> " -> " <> (fromString ip)

        -- Retrieve a peer IP by file hash
        get "/get/:hash" $ do
            hash <- pathParam "hash" :: ActionM String
            dht <- liftIO $ readIORef dhtRef
            case lookup hash dht of
                Just ip -> text (fromString ip)
                Nothing -> text "Not found"
