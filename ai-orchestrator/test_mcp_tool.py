from mcp_client import call_tool_sync

result = call_tool_sync(
    "extract_metadata",
    {"file_path": "/Users/martinenke/Desktop/test.png"}
)

print(result)