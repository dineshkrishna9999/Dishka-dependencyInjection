# provide_all is a helper function which can be used instead of repeating provide call with just class passed and same scope.
from dishka import Provider, Scope, make_container, provide_all, provide

# === SERVICES ===

class Database:
    def __init__(self):
        self.name = "Main"
        print(f"{self.name} Database created")

    def get_data(self) -> str:
        return f"Data from {self.name} Database"

class Logger:
    def __init__(self):
        self.level = "INFO"
        print(f"{self.level} Logger created")

    def log(self, message: str):
        print(f"[{self.level}] {message}")

# === PROVIDER USING PROVIDE_ALL ===

class SimpleProvider(Provider):
    scope = Scope.APP

    services = provide_all(
        Database,
        Logger
    )
    # Alternative for more control:
    # @provide_all
    # def provide_services(self) -> tuple[Database, Logger]:
    #     print("Factory creating both services...")
    #     db = Database("Main")
    #     logger = Logger("INFO")
    #     return db, logger

# === EXECUTION ===

def main():
    print(">>> provide_all Example")
    print("=" * 30)

    # Create DI container
    container = make_container(SimpleProvider())

    print("\n-- Retrieving Database --")
    db = container.get(Database)
    print(f"Received: {db.get_data()}")

    print("\n-- Retrieving Logger --")
    logger = container.get(Logger)
    logger.log("Hello from Logger!")

    print("\nBoth services were provided via a single `provide_all` definition!")

if __name__ == "__main__":
    main()
