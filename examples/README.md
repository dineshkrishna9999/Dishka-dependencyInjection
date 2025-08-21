# Dishka Examples

This directory contains organized examples of Dishka dependency injection framework, progressing from basic concepts to advanced integrations.

## Directory Structure

### [01-basic-concepts](./01-basic-concepts/)
Start here if you're new to Dishka! These examples cover the fundamental concepts:
- Simple dependency injection
- Basic provider setup
- Container creation and usage

### [02-intermediate](./02-intermediate/)
Once you understand the basics, explore these intermediate patterns:
- Provider aliases for flexible configurations
- Provide-all patterns for bulk registration

### [03-fastapi-integration](./03-fastapi-integration/)
Real-world integration examples:
- FastAPI with Dishka dependency injection
- Request scoping and lifecycle management
- Production-ready patterns

## How to Use These Examples

1. **Start with basics**: Begin with `01-basic-concepts/` to understand core concepts
2. **Progress gradually**: Move to `02-intermediate/` when you're comfortable with basics
3. **Apply in practice**: Use `03-fastapi-integration/` for real-world applications

Each example is self-contained and can be run independently with:
```bash
# Using uv (recommended)
uv run poe task-name

# Or directly with Python
python examples/folder-name/example-name.py
```

## Prerequisites

Make sure you have the dependencies installed:
```bash
# With uv (recommended)
uv sync

```
