# mcpscope

A simple local MCP (Model Context Protocol) server built with [fastmcp](https://github.com/jlowin/fastmcp).

## Tools

| Tool | Description | Parameters |
|------|-------------|------------|
| `say_hello` | 名前を受け取って挨拶を返す | `name: str` |
| `add` | 2つの整数を足し算する | `a: int`, `b: int` |

## Requirements

- Python 3.12+
- [uv](https://docs.astral.sh/uv/)

## Setup

```bash
# Clone the repository
git clone https://github.com/sla10132000/mcpscope.git
cd mcpscope

# Install dependencies
uv sync
```

## Running the server

```bash
uv run python server.py
```

## Using with Claude Code

Add the following to your `.mcp.json`:

```json
{
  "mcpServers": {
    "mcpscope": {
      "command": "uv",
      "args": ["run", "python", "server.py"],
      "cwd": "/path/to/mcpscope"
    }
  }
}
```

Replace `/path/to/mcpscope` with the actual path to your clone.

## Adding new tools

Open `server.py` and add a decorated function:

```python
@mcp.tool()
def your_tool(param: str) -> str:
    """ツールの説明"""
    return f"result: {param}"
```

fastmcp automatically exposes it as an MCP tool — no further registration needed.
