# Intermediate Patterns - Advanced Dishka Techniques

Once you've mastered the basics, these examples show more sophisticated patterns and techniques.

## Examples in this folder:

### `provider_aliases.py`
**Flexible service registration**
- Using aliases for different implementations
- Configuration-based service selection
- Multiple providers for the same interface

### `provide_all_pattern.py`
**Bulk service registration**
- Register multiple related services at once
- Automatic service discovery patterns
- Reducing boilerplate code

## When to Use These Patterns

- **Provider Aliases**: When you need different implementations based on configuration (e.g., dev vs prod databases)
- **Provide All**: When you have many similar services to register (e.g., all your repository classes)

## Key Concepts You'll Learn

- **Service Aliases**: Multiple names for the same service type
- **Bulk Registration**: Efficient ways to register many services
- **Provider Composition**: Combining multiple providers effectively

## Running the Examples

```bash
# From the project root
python examples/02-intermediate/provider_aliases.py
python examples/02-intermediate/provide_all_pattern.py
```
