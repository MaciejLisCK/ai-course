# # end turn
# import anthropic

# client = anthropic.Anthropic()

# response = client.messages.create(
#     model="claude-fable-5",
#     messages=[
#         { "role": "user", "content": "Kim jesteś?" }
#     ]
# )

# output = response.model_dump_json(indent=2)

# print(output)



# # max tokens
# import anthropic

# client = anthropic.Anthropic()

# response = client.messages.create(
#     model="claude-fable-5",
#     max_tokens=10,
#     messages=[
#         { "role": "user", "content": "Kim jesteś?" }
#     ]
# )

# output = response.model_dump_json(indent=2)

# print(output)


# # stop sequence
# import anthropic

# client = anthropic.Anthropic()

# response = client.messages.create(
#     model="claude-fable-5",
#     max_tokens=100,
#     stop_sequences=["7", "siedem"],
#     messages=[
#         { "role": "user", "content": "Wymień liczby od 1 do 100" }
#     ]
# )

# output = response.model_dump_json(indent=2)

# print(output)



# # tool use

import anthropic

client = anthropic.Anthropic()

cat_location_tool = {
    "name": "cat_location_tool",
    "description": "Get the last cat location in user home.",
    "input_schema": {
        "type": "object",
        "properties": {
            "cat": {"type": "string", "enum": ["paczek", "bohen"], "description": "Cat name."},
        },
        "required": ["cat"],
    },
}

response = client.messages.create(
    model="claude-fable-5",
    tools=[cat_location_tool],
    max_tokens=100,
    messages=[
        { "role": "user", "content": "Gdzie jest bohen?" }
    ]
)

output = response.model_dump_json(indent=2)

print(output)
