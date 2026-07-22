import anthropic
from anthropic.types import ThinkingConfigEnabledParam, ThinkingConfigParam

client = anthropic.Anthropic()

thinking: ThinkingConfigParam = {
    "budget_tokens": 10000,
    "type": "enabled"
}  



with client.messages.stream(
    model="claude-sonnet-4-6",
    max_tokens=16000,
    thinking=thinking,
    messages=[
        {
            "role": "user",
            "content": "What is the greatest common divisor of 1071 and 462?"
        }
    ]
) as stream:
    thinking_started = False
    response_started = False

    for event in stream:
        if event.type == "content_block_start":
            print(f"\nStarting {event.content_block.type} block...")
            # Reset flags for each new block
            thinking_started = False
            response_started = False
        elif event.type == "content_block_delta":
            if event.delta.type == "thinking_delta":
                if not thinking_started:
                    print("Thinking: ", end="", flush=True)
                    thinking_started = True
                print(event.delta.thinking, end="", flush=True)
            elif event.delta.type == "text_delta":
                if not response_started:
                    print("Response: ", end="", flush=True)
                    response_started = True
                print(event.delta.text, end="", flush=True)
        elif event.type == "content_block_stop":
            print("\nBlock complete.")
