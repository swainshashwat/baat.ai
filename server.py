import asyncio
import websockets

# Define a callback function to handle incoming messages
async def handle_message(websocket, message):
    # Process the message and generate a response
    if message:
        response = message + " lol"
    else:
        response = None

    # Send the response back to the client
    if response:
        print("[DEBUG] Server got message: " + message)
        await websocket.send(response)

# Define the WebSocket server handler
async def server(websocket, path):
    async for message in websocket:
        await handle_message(websocket, message)

# Start the WebSocket server
start_server = websockets.serve(server, "localhost", 8000)
print("Started Server")
# Run the server indefinitely
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
