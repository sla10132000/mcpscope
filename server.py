from fastmcp import FastMCP

mcp = FastMCP("mcpscope")


@mcp.tool()
def say_hello(name: str) -> str:
    """名前を受け取って挨拶を返す"""
    return f"Hello, {name}! from mcpscope"


@mcp.tool()
def add(a: int, b: int) -> int:
    """2つの整数を足し算する"""
    return a + b


if __name__ == "__main__":
    mcp.run()
