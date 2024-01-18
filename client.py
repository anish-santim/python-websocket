import asyncio 
import websockets

async def hello():
    url = "ws://localhost:8765"
    async with websockets.connect(url) as websocket:
        name = input("What is your name? ")

        await websocket.send(name)

        print("Client sent: ", name)

        greeting = await websocket.recv()

        print("Client received: ", greeting)

if __name__ == "__main__":
    asyncio.run(hello())
