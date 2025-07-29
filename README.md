# hedys_mcp MCP server

"Hedy's MCP server project"

## Components

### Resources

The server implements a simple note storage system with:
- Custom note:// URI scheme for accessing individual notes
- Each note resource has a name, description and text/plain mimetype

### Prompts

The server provides a single prompt:
- summarize-notes: Creates summaries of all stored notes
  - Optional "style" argument to control detail level (brief/detailed)
  - Generates prompt combining all current notes with style preference


### Tools

The server implements several tools:
- add-note: Adds a new note to the server
  - Takes "name" and "content" as required string arguments
  - Updates server state and notifies clients of resource changes
- update-note: Updates an existing note
- delete-note: Deletes a note
- get-joke: Fetches a random joke from the internet
- deborahs_jokes: Returns a random joke from Deborah's personal collection

## HTTP API (Streaming/ASGI mode)

When running with Uvicorn (ASGI/streaming mode), the following endpoints are available:

- `GET /notes` — List all note names
- `GET /notes/{name}` — Get a note's content
- `POST /notes` — Add a note (JSON: `{ "name": ..., "content": ... }`)
- `PUT /notes` — Update a note (JSON: `{ "name": ..., "new_content": ... }`)
- `DELETE /notes/{name}` — Delete a note
- `GET /joke` — Get a random joke from Deborah's personal collection

Example to get a joke:

    curl http://127.0.0.1:8000/joke

Response:

    { "joke": "Why did the scarecrow win an award? Because he was outstanding in his field!" }

## Configuration

[TODO: Add configuration details specific to your implementation]

## Quickstart

### Install

#### Claude Desktop

On MacOS: `~/Library/Application\ Support/Claude/claude_desktop_config.json`
On Windows: `%APPDATA%/Claude/claude_desktop_config.json`

<details>
  <summary>Development/Unpublished Servers Configuration</summary>
  ```
  "mcpServers": {
    "hedys_mcp": {
      "command": "uv",
      "args": [
        "--directory",
        "C:\Users\fravolih\Documents\hedy_mcp_test",
        "run",
        "hedys_mcp"
      ]
    }
  }
  ```
</details>

<details>
  <summary>Published Servers Configuration</summary>
  ```
  "mcpServers": {
    "hedys_mcp": {
      "command": "uvx",
      "args": [
        "hedys_mcp"
      ]
    }
  }
  ```
</details>

## Development

### Building and Publishing

To prepare the package for distribution:

1. Sync dependencies and update lockfile:
```bash
uv sync
```

2. Build package distributions:
```bash
uv build
```

This will create source and wheel distributions in the `dist/` directory.

3. Publish to PyPI:
```bash
uv publish
```

Note: You'll need to set PyPI credentials via environment variables or command flags:
- Token: `--token` or `UV_PUBLISH_TOKEN`
- Or username/password: `--username`/`UV_PUBLISH_USERNAME` and `--password`/`UV_PUBLISH_PASSWORD`

### Debugging

Since MCP servers run over stdio, debugging can be challenging. For the best debugging
experience, we strongly recommend using the [MCP Inspector](https://github.com/modelcontextprotocol/inspector).


You can launch the MCP Inspector via [`npm`](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) with this command:

```bash
npx @modelcontextprotocol/inspector uv --directory C:\Users\fravolih\Documents\hedy_mcp_test run hedys-mcp
```


Upon launching, the Inspector will display a URL that you can access in your browser to begin debugging.