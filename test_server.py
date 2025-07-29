import pytest
from src.hedys_mcp import server
import asyncio

@pytest.mark.asyncio
async def test_deborahs_jokes_tool():
    result = await server.handle_call_tool("deborahs_jokes", {})
    assert isinstance(result, list)
    assert isinstance(result[0].text, str)
    assert len(result[0].text) > 0

@pytest.fixture(autouse=True)
def clear_notes():
    server.notes.clear()


# Ensure notes are cleared before each test
import pytest

@pytest.fixture(autouse=True)
def clear_notes():
    server.notes.clear()

@pytest.mark.asyncio
async def test_mcp_tools():
    # Add note via tool
    result = await server.handle_call_tool("add-note", {"name": "toolnote", "content": "Tool content"})
    assert any("Added note" in r.text for r in result)
    # Update note via tool
    result = await server.handle_call_tool("update-note", {"name": "toolnote", "new_content": "Updated tool content"})
    assert any("Updated note" in r.text for r in result)
    # Delete note via tool
    result = await server.handle_call_tool("delete-note", {"name": "toolnote"})
    assert any("Deleted note" in r.text for r in result)

@pytest.mark.asyncio
async def test_list_resources_empty():
    resources = await server.handle_list_resources()
    assert isinstance(resources, list)
    assert len(resources) == 0

@pytest.mark.asyncio
async def test_add_read_update_delete_note():
    note_name = "testnote"
    content = "This is a test note."
    # Add
    await server.handle_create_resource(note_name, content)
    resources = await server.handle_list_resources()
    assert any(note_name == r.uri.path.lstrip("/") for r in resources)
    from pydantic import AnyUrl
    uri = AnyUrl(f"note://internal/{note_name}")
    note_content = await server.handle_read_resource(uri)
    assert note_content == content
    # Update
    new_content = "Updated content."
    await server.handle_update_resource(note_name, new_content)
    updated_content = await server.handle_read_resource(uri)
    assert updated_content == new_content
    # Delete
    await server.handle_delete_resource(note_name)
    resources = await server.handle_list_resources()
    assert all(note_name != r.uri.path.lstrip("/") for r in resources)
