"""
Simple Dishka Dependency Injection Example

This example demonstrates how Dishka automatically manages dependencies between services.
Think of it like ordering food - you just ask for a sandwich, and the kitchen
automatically gets bread, meat, and vegetables to make it for you.
"""

from dishka import Provider, Scope, make_container, provide


# === STEP 1: DEFINE SERVICES (What we need) ===


class Database:
    """
    This is like a 'storage room' where user data lives.
    It represents any external service (database, API, file system, etc.)
    """

    def __init__(self):
        print("Database connected!")  # This shows when the database is created

    def get_user(self, user_id: int) -> str:
        """Simulate getting a user from the database"""
        return f"User_{user_id}"


class UserService:
    """
    This is like a 'helper' that knows how to work with user data.
    IMPORTANT: It NEEDS a Database to work (it can't work alone).
    """

    def __init__(self, database: Database):
        # UserService depends on Database - it needs one to function
        self.database = database

    def get_user_info(self, user_id: int) -> str:
        """Get user information by asking the database"""
        user = self.database.get_user(user_id)
        return f"Info for {user}"


class Greeter:
    """
    This creates friendly greetings for users.
    IMPORTANT: It NEEDS a UserService to work.
    """

    def __init__(self, user_service: UserService):
        # Greeter depends on UserService - it needs one to function
        self.user_service = user_service

    def greet_user(self, user_id: int) -> str:
        """Create a greeting for a specific user"""
        user_info = self.user_service.get_user_info(user_id)
        return f"Hello, {user_info}!"


# === STEP 2: CREATE PROVIDER (Recipe book for making everything) ===


class MyProvider(Provider):
    """
    This is like a 'recipe book' that tells Dishka how to create each service.
    scope = Scope.APP means 'make one of each service and reuse them throughout the app'
    """

    scope = Scope.APP

    @provide
    def provide_database(self) -> Database:
        """
        Recipe for Database: Just create a new Database()
        This is the simplest case - no dependencies needed
        """
        return Database()

    @provide
    def provide_user_service(self, database: Database) -> UserService:
        """
        Recipe for UserService:
        1. First, get me a Database (Dishka will call provide_database)
        2. Then create UserService and give it the database
        """
        return UserService(database)

    @provide
    def provide_greeter(self, user_service: UserService) -> Greeter:
        """
        Recipe for Greeter:
        1. First, get me a UserService (Dishka will call provide_user_service)
        2. Then create Greeter and give it the user_service
        """
        return Greeter(user_service)


# === STEP 3: THE MAGIC HAPPENS ===

# Create the container with our provider (recipe book)
container = make_container(MyProvider())

# Ask for a Greeter - Dishka will automatically:
# 1. Create Database first (because UserService needs it)
# 2. Create UserService (giving it the Database)
# 3. Create Greeter (giving it the UserService)
# 4. Give us the fully-working Greeter
greeter = container.get(Greeter)

# Use our greeter - it now has everything it needs!
print(greeter.greet_user(123))


# ----summary ------
# so now without this dishka we have to crete everything ourself
# Database = Database()
# UserService = UserService(Database)
# Greeter = Greeter(UserService)

# so with the dishka
# greeter = container.get(Greeter) it handles all the things.... for us
