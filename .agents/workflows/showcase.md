---
description: Professor-grade showcase for the Hybrid P2P File Sharing System
---
# Haskell P2P Project Showcase (Full-Marks Edition)

This workflow is designed for a polished college presentation where you clearly demonstrate:
- Correct architecture choices
- Working end-to-end behavior
- Separation of concerns (metadata vs file transfer)
- Engineering maturity (validation, cleanup, and risk handling)

## 0. Opening Script (30-45 seconds)
Say this before running commands:

"My project is a Hybrid P2P File Sharing System built in Haskell. The key design idea is that metadata is centralized for fast lookup, while file data transfer is decentralized for scalability. The central DHT server stores only file-hash-to-peer mappings. Actual file bytes move directly between peers. This avoids bottlenecking all traffic through one server and reflects how real systems combine coordination with distributed transfer."

## 1. Pre-Demo Sanity Check (20 seconds)
Run these quickly to avoid live demo surprises.
// turbo
runhaskell --version
// turbo
uv run python --version
// turbo
wget --version

If wget is unavailable in your environment, mention:
"In this prototype, the downloader currently uses wget. Replacing it with an internal Haskell HTTP fetch is a straightforward next hardening step."

## 2. Presenting the Architecture
Start the presentation by bringing up your system design graph. This explains the theory of what you built.
// turbo
uv run python graph1.py

Speak while the graph is visible:
- "The red node is the metadata registry (DHT server)."
- "Blue nodes are peers. They contact the server only for discovery, not for data relay."
- "Green file nodes represent content ownership and distribution across peers."
- "This hybrid pattern gives lookup consistency while preserving peer-to-peer throughput."

## 3. Starting the Backend Infrastructure
We need to spin up the metadata registry (DHT Server). We'll start it in the background so you can continue the demo in this terminal.
// turbo
runhaskell DHTServer.hs > dht.log 2>&1 &

Next, we will simulate a remote peer hosting the file. We'll start a simple HTTP server on port `8000`. 
// turbo
uv run python -m http.server 8000 > server.log 2>&1 &

Now say:
"The DHT registry is now active on port 8080, and Peer A is online as an HTTP seed on port 8000."

Optional quick health checks:
// turbo
curl http://127.0.0.1:8080/get/file123
// turbo
ls -l file123

If the first command returns Not found, explain:
"Not found is expected before registration. It confirms lookup is functioning and empty-state safe."

## 3.5 Build the Peer and Client Binaries (One-time for this demo environment)
In this environment, the `process` package is not exposed by default to `runhaskell`, so compile once and run executables.
// turbo
ghc -package process Peer.hs -o peer_cli
// turbo
ghc -package process TorrentClient.hs -o torrent_cli

## 4. Registering the File (Seeding)
Peer A will now announce to the central DHT directory that it holds `file123` at its IP address.
// turbo
./peer_cli register file123 127.0.0.1:8000

Immediately verify registration:
// turbo
./peer_cli find file123

Narrate:
"The server now returns 127.0.0.1:8000 for this hash, proving metadata registration and lookup both work."

Quick peer-server readiness check before download:
// turbo
curl -I http://127.0.0.1:8000/file123

If this fails, restart the seed server:
// turbo
uv run python -m http.server 8000 > server.log 2>&1 &

## 5. Demonstrating the Client Download
Now you act as Peer B (the downloader). You will run the Torrent Client. 
*(Note: Because this requires you to type an input, run this step manually or use the play button instead of `// turbo` below.)*

```bash
./torrent_cli
```
**Important:** When prompted for "Enter file hash to download:", type **`file123`** and hit Enter!

Say while it runs:
"Peer B queries DHT for location metadata, receives 127.0.0.1:8000, then downloads directly from Peer A using wget. This confirms true P2P data transfer with centralized discovery only."

After download, prove success:
// turbo
ls -l file123

If asked how failure is handled, answer:
"If a hash is not registered, the client receives Not found from DHT and exits gracefully without a broken transfer attempt."

## 6. Technical Defense Talking Points (Use in Q&A)
Use these concise points if your professor asks deeper questions:
- Consistency model: "Current DHT is in-memory for demo speed; persistence can be added with a lightweight embedded store."
- Scalability: "Metadata traffic is small compared to file transfer traffic, so this architecture scales better than full proxying."
- Security: "Next iteration would add hash verification after download and signed peer announcements."
- Fault tolerance: "Replication or sharding of the metadata node can remove single-point dependency."
- Extensibility: "The Peer and Client components are already separated, so chunking, retries, and parallel download can be added incrementally."

## 7. Cleanup
Let's kill the background servers so your terminal is clean after the showcase.
// turbo
pkill -f "^runhaskell DHTServer.hs"
// turbo
pkill -f "^uv run python -m http.server 8000" || pkill -f "^python -m http.server 8000"

Optional log recap if the professor wants evidence:
// turbo
tail -n 20 dht.log
// turbo
tail -n 20 server.log

## 8. Closing Script (15 seconds)
End with this:

"To summarize: I demonstrated architecture, live registration, peer discovery, and direct file transfer. The project proves a working hybrid model where coordination is centralized but data movement is decentralized. This gives a clean foundation for future enhancements like secure hash validation, peer reputation, and multi-source chunk downloading."

Showcase complete.
