# MCP Samples
An example project that provides several Model-Context-Protocol implmenetations using FastMCP for different use cases.

## What you'll need
1. This project repository: 
2. Python 3.11 or higher
3. [uv](https://docs.astral.sh/uv/getting-started/installation/)
4. [LM Studio](https://lmstudio.ai/download)  Get LM Studio... not Bionic for this exercise.
5. A tool enabled model like `google/gemma-4-e4b` or `qwen/qwen3-vl-4b` (or any other tool enabled model you have access to)

## Getting Started
1. Clone this repository to your local machine.
2. Start the MCP service by running `uv run mcp.py` from the root of this repository.
3. Start LM Studio
4. Load a Tool enabled model (I'd suggest `google/gemma-4-e4b`)
5. In LM Studio got to `Integrations` on the right side and click `Install`
6. Choose `Edit mcp.json`
7. Under the `mcpServers` section, add the following:
```json
    "mcp-samples": {
      "url": "http://localhost:8001/mcp"
    },
```
8. Save the file
9. Turn on the `mcp/mcp-samples` tool in LM Studio

## Usage
Start a chat with the Tool enabled model
Try some prompts like:

`I'm hungry for something with chicken, can you suggest anything?`

Next find one of the suggestions and ask the model to provide recipe details:

`Ooo... {selected recipe name} sounds interesting.  How do I make that?`

To exercise `No as a Service` try:

`I really don't want to do all that cooking.  Help me create a reason to refuse`

You can also ask it to provide a random recipe:

`I don't care what I eat, just give me a random recipe and details on how to make it.`