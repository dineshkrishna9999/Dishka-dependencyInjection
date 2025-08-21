# Basic Concepts - Getting Started with Dishka

This folder contains the fundamental examples to get you started with Dishka dependency injection.

## Examples in this folder:

### `simple_start.py`
**The absolute basics** - Start here!
- Your first Dishka container
- Simple service creation
- Basic dependency resolution

### `basic_dependency_injection.py`
**Core dependency injection patterns**
- Services that depend on other services
- Provider configuration
- Understanding scopes and lifetimes

## Learning Path

1. **First**: Run `simple_start.py` to see Dishka in action
2. **Then**: Study `basic_dependency_injection.py` to understand how services depend on each other

## Key Concepts You'll Learn

- **Container**: The main object that holds all your dependencies
- **Provider**: Classes that tell Dishka how to create your services
- **Scope**: Controls when and how often services are created
- **Dependency Resolution**: How Dishka automatically figures out what your services need

## Running the Examples

```bash
# From the project root
python examples/01-basic-concepts/simple_start.py
python examples/01-basic-concepts/basic_dependency_injection.py
```
