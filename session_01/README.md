# Session 01

Python examples for calling Gemini and OpenAI models with LangChain, defining
tools, using structured output, and creating a Deep Agent.

## Requirements

- Windows
- Python 3.13 or newer
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- A Google Gemini API key for the Gemini examples
- An OpenAI API key for `tools.py`

## Set up

From the repository root, open PowerShell and run:

```powershell
Set-Location .\session_01
uv python install 3.13
uv sync
```

Create a `.env` file in this directory and add the keys for the examples you
want to run:

```dotenv
GEMINI_API_KEY=your-gemini-api-key
OPENAI_API_KEY=your-openai-api-key
```

`GEMINI_API_KEY` is used by `demo.py`, `messages.py`, `structured_output.py`,
`templates.py`, and `deep_agents.py`. `OPENAI_API_KEY` is used by `tools.py`.
`demo.py` can also use `LANGSMITH_API_KEY` if LangSmith tracing is configured.
Keep real keys in `.env`; do not commit them.

## Run an example

Run commands from `session_01`:

```powershell
uv run python demo.py
uv run python messages.py
uv run python structured_output.py
uv run python templates.py
uv run python deep_agents.py
```

`tools.py` uses `langchain-openai`, which is not part of the project's declared
dependencies. Run it with that package supplied for this invocation:

```powershell
uv run --with langchain-openai python tools.py
```

Each script makes live model requests and may incur provider charges. Run one
script at a time; these are independent examples, not a single application.
