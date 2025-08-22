from dishka import Provider, Scope, make_container, provide


class Greeter:
    def greet(self, name: str) -> str:
        return f"Hello, {name}!"


class MyProvider(Provider):
    scope = Scope.APP

    # Simple case: no dependencies, just create the object
    provide_greeter = provide(Greeter)


container = make_container(MyProvider())

greeter = container.get(Greeter)
print(greeter.greet("World"))
