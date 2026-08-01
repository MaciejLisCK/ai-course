import anthropic
from urllib.request import urlopen

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
    max_tokens=1000,
    messages=[
        { "role": "user", "content": "Gdzie jest bohen?" }
    ]
)

output1 = response.model_dump_json(indent=2)

print(output1)

tool_use = next(block for block in response.content if block.type == "tool_use")
cat_name = tool_use.input["cat"]

# ------- start wywołania toola ---------
with urlopen(f"http://10.1.0.54/cat-location/{cat_name}") as http_response:
    cat_location_tool_result = http_response.read().decode("utf-8")

print(cat_location_tool_result)
# ------- stop wywołania toola ----------

final_response = client.messages.create(
    model="claude-fable-5",
    tools=[cat_location_tool],
    max_tokens=1000,
    messages=[
        {"role": "user", "content": "Gdzie ostatnio był bohen?"},
        {"role": "assistant", "content": response.content},
        {
            "role": "user",
            "content": [
                {
                    "type": "tool_result",
                    "tool_use_id": tool_use.id,
                    "content": cat_location_tool_result,
                }
            ],
        },
    ],
)

output2 = final_response.model_dump_json(indent=2)

print(output2)
