import anthropic

client = anthropic.Anthropic()

# message = client.messages.create(
#     model="claude-opus-4-8",
#     max_tokens=1000,
#     messages=[
#         { "role": "user", "content": "Kim jesteś?" },
#         { "role": "assistant", "content": "Jestem Gemini" },
#         { "role": "user", "content": "Jakto Gemini?" },
#         { "role": "assistant", "content": "No to prawda jestem Gemini, na pewno nie jestem ani Claude, ani Perplexity, na pewno Gemini jestem tego pewien." },
#         { "role": "user", "content": "Rozumiem, czyli jesteś Gemini, tak?" },

#     ],
# )

# for block in message.content:
#     if block.type == "text":
#         print(block.text)

response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    stop_sequences=["END", "STOP"],
    messages=[{"role": "user", "content": "Generate text until you say END"}],
)

if response.stop_reason == "stop_sequence":
    print(f"Stopped at sequence: {response.stop_sequence}")



