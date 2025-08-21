🧩 Dependency Injection with Dishka

Dishka is a lightweight Dependency Injection (DI) framework for Python that facilitates the management of object creation and their dependencies, promoting loose coupling and enhancing testability.

🔑 Core Concepts
Provider

A Provider is a class that defines how to create dependencies. It contains methods decorated with @provide that instantiate and configure objects.

Scope

Scope defines the lifespan of a dependency:

Scope.APP: The dependency exists for the entire application's lifetime.

Scope.REQUEST: The dependency exists for the duration of a single request or operation.

Container

The Container manages the lifecycle of dependencies. It resolves and provides instances based on the configuration set in providers.

@provide

The @provide decorator marks a method in a provider as a factory for creating a specific dependency. The method's return type indicates what dependency it provides.

@inject

The @inject decorator is used to automatically inject dependencies into functions or methods, based on their type annotations.