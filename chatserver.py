import asyncio
import websockets
import json

connected_clients = set()

async def handler(websocket):
    connected_clients.add(websocket)
    print("New client connected.")
    try:
        async for message in websocket:
            print(f"Received raw message: {message}")
            try:
                data = json.loads(message)  # Parse JSON message
                sender = data['sender']
                text = data['text']
                broadcast_message = json.dumps({ 'sender': sender, 'text': text })
                
                for client in connected_clients:
                    await client.send(broadcast_message)  # Send structured JSON
            except json.JSONDecodeError:
                print("Received non-JSON message. Ignored.")
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected.")
    finally:
        connected_clients.remove(websocket)

async def main():
    async with websockets.serve(handler, "localhost", 6789):
        print("WebSocket Server running on ws://localhost:6789")
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())
