import asyncio 
import websockets 

async def hello(websocket):
    name = await websocket.recv()

    print("Server received: ", name)

    greeting = "Hello " + name + "!"

    await websocket.send(greeting)
    print("Server sent: ", greeting)

async def main():  
    async with websockets.serve(hello, "0.0.0.0", 8765):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())