import asyncio
import websockets
import streamlit as st

# Establish a WebSocket connection
async def connect():
    uri = "ws://localhost:8000"
    async with websockets.connect(uri) as websocket:
        
        # Get user input
        message = st.text_input("Enter your message")

        # Send the message to the server
        await websocket.send(message)

        if st.button("Submit") and message:
            # Receive and display the response from the server
            response = await websocket.recv()
        else:
            response = None

        if response:
            st.write("You: ", message)
            st.write("Bot:", response)

# Run the client
st.title("WebSocket Chatbot")
st.write("Type a message below and press Enter to send it to the server.")

# Start the WebSocket client
asyncio.run(connect())
