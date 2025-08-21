# Dependency Injection with Dishka

Dishka is a lightweight Dependency Injection (DI) framework for Python that facilitates the management of object creation and their dependencies, promoting loose coupling and enhancing testability.

## Learning Path

This repository contains organized examples that will help you understand Dishka step by step:

### Start Here: Basic Concepts (./examples/01-basic-concepts/)
- Simple dependency injection fundamentals
- Your first Dishka container and providers
- Understanding scopes and dependency resolution

### Level Up: Intermediate Patterns (./examples/02-intermediate/)
- Provider aliases and flexible configurations
- Bulk service registration techniques
- Complex dependency chains and relationships

### Build Real Apps: FastAPI Integration (./examples/03-fastapi-integration/)
- Production-ready web application patterns
- Request scoping and lifecycle management
- Complete FastAPI + Dishka integration

## Quick Start

1. **Install dependencies**:
   ```bash
   # With uv (recommended)
   uv sync
   
   ```

2. **Run your first example**:
   ```bash
   # Using uv run (recommended)
   uv run poe simple-start
   
   ```

3. **See all available examples**:
   ```bash
   uv run poe help
   ```

4. **Follow the learning path** through the examples folders

## Available Tasks (using uv run poe)

Run examples easily with uv and poethepoet:

```bash
# Basic examples
uv run poe simple-start    # Your first Dishka example
uv run poe basic-di        # Core dependency injection patterns

# Intermediate examples  
uv run poe aliases         # Provider aliases example
uv run poe provide-all     # Provide-all pattern example

# FastAPI integration
uv run poe fastapi         # FastAPI + Dishka example

# Development tools
uv run poe format          # Format code with black
uv run poe lint            # Lint code with flake8
uv run poe type-check      # Type check with mypy
```

## Core Concepts

## Provider

A Provider is a class that defines how to create dependencies. It contains methods decorated with @provide that instantiate and configure objects.

## Scope

Scope defines the lifespan of a dependency:

- **Scope.APP**: The dependency exists for the entire application's lifetime.
- **Scope.REQUEST**: The dependency exists for the duration of a single request or operation.

## Container

The Container manages the lifecycle of dependencies. It resolves and provides instances based on the configuration set in providers.

## @provide

The @provide decorator marks a method in a provider as a factory for creating a specific dependency. The method's return type indicates what dependency it provides.

## @inject

The @inject decorator is used to automatically inject dependencies into functions or methods.
## provide_all

The `provide_all` helper function allows you to register multiple classes at once instead of creating separate @provide methods for each. It's useful when you have services without complex dependencies.

```python
services = provide_all(Database, Logger, Cache)
```

## alias

The `alias` function allows you to register the same implementation for multiple types/interfaces. This is useful when a single class implements multiple interfaces or when you want the same service available under different names.

```python
# Same instance available as different types
logger = alias(source=Console, provides=Logger)
printer = alias(source=Console, provides=Printer)
```

## 📁 Examples

- `main.py` - Basic dependency injection example
- `dishka_dependency_injection_example.py` - Comprehensive DI example
- `dishka_provide_all_example.py` - Advanced provide_all usage
- `dishka_provide_all_simple.py` - Simple provide_all demonstration
- `dishka_alias_simple.py` - Simple alias functionality example
- `dishka_related_services_simple.py` - Related services example