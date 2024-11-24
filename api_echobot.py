import asyncio
import fastapi_poe as fp

# Create an asynchronous function to encapsulate the async for loop
async def get_responses(api_key, messages):
    async for partial in fp.get_bot_response(messages=messages, bot_name="ax-echobot", api_key=api_key):
        print(partial)
 
# Replace <api_key> with your actual API key, ensuring it is a string.
api_key = "4lufBqnEJIThIo6YZYPhV9ZjGy3yfwIox25PNUNAQZI"
message = fp.ProtocolMessage(role="user", content="Give me a simple project")

# Run the event loop
# For Python 3.7 and newer
asyncio.run(get_responses(api_key, [message]))

# For Python 3.6 and older, you would typically do the following:
# loop = asyncio.get_event_loop()
# loop.run_until_complete(get_responses(api_key))
# loop.close()