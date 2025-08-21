# FastAPI Integration - Real-World Web Applications

These examples show how to use Dishka with FastAPI to build production-ready web applications.

## Examples in this folder:

### `fastapi_basic_example.py`
**Essential FastAPI + Dishka integration**
- Setting up Dishka with FastAPI
- Injecting dependencies into route handlers
- Configuration management
- Request/response patterns

## What You'll Learn

- **Route Injection**: How to inject services directly into FastAPI route handlers
- **Scoping**: Understanding APP vs REQUEST scope in web applications
- **Context Injection**: Passing external configuration into your dependency container
- **Integration Setup**: Proper way to connect Dishka with FastAPI

## Key Features Demonstrated

- **@inject decorator**: Enable dependency injection in routes
- **FromDishka[Type]**: Type annotations for injected dependencies  
- **setup_dishka()**: Connecting Dishka container to FastAPI app
- **External Context**: Injecting configuration from environment/files
- **Singleton Services**: APP-scoped services that live for the entire application

## Real-World Patterns

This example demonstrates patterns you'll use in production:
- Configuration injection (database URLs, API keys, etc.)
- Service layer architecture
- Dependency injection in web handlers
- Proper application startup sequence

## Running the Examples

```bash
# From the project root
python examples/03-fastapi-integration/fastapi_basic_example.py

# Then visit:
# http://localhost:8000 - Main endpoint
# http://localhost:8000/docs - FastAPI auto-generated documentation
# http://localhost:8000/greet/YourName - Try the dependency injection
```

## Prerequisites

```bash
pip install fastapi uvicorn dishka
```
