import os
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

load_dotenv()

from twilio.rest import Client

twilio_client = Client(
    os.getenv("TWILIO_ACCOUNT_SID"),
    os.getenv("TWILIO_AUTH_TOKEN")
)
FROM_NUMBER = os.getenv("TWILIO_FROM_NUMBER")

mcp = FastMCP("twiliomcp")

@mcp.tool()
def wyslij_sms(number: str, message: str) -> str:
    """Wysyła SMS na podany numer."""
    message = twilio_client.messages.create(
        body=message,
        from_=FROM_NUMBER,
        to=number
    )
    return f"SMS został wysłany! SID: {message.sid}"

if __name__ == "__main__":
    mcp.run(transport="stdio")
