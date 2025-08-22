"""
Simple Dishka + FastAPI Example

"""

from fastapi import FastAPI
from dishka import make_async_container, Provider, provide, Scope, from_context
from dishka.integrations.fastapi import setup_dishka, inject, FromDishka
from pydantic import BaseModel
import uvicorn


# Step 1: Create your configuration
# This is just a regular Pydantic model - nothing special about it
class AppSettings(BaseModel):
    app_name: str = "My Dishka App"
    debug: bool = True


# Step 2: Create a service that needs the configuration
# Notice: this service NEEDS AppSettings to work
# Instead of creating AppSettings manually, Dishka will provide it automatically!
class GreetingService:
    def __init__(self, settings: AppSettings):
        self.settings = settings

    def greet(self, name: str) -> str:
        return f"Hello {name} from {self.settings.app_name}!"


# Step 3: Tell Dishka how to create your objects
# This is called a "Provider" - it's like a recipe book for Dishka
class AppProvider(Provider):
    scope = Scope.APP  # APP scope = create once and reuse (singleton)

    # Tell Dishka: "AppSettings will come from outside the container"
    # We'll pass it when creating the container
    settings = from_context(provides=AppSettings, scope=Scope.APP)

    # Tell Dishka: "To create GreetingService, just use its constructor"
    # Dishka will automatically resolve the AppSettings dependency
    greeting_service = provide(GreetingService)


# Step 4: Setup FastAPI and Dishka

# Create FastAPI app (normal FastAPI setup)
app = FastAPI()

# Create your settings object (this could come from environment variables, config files, etc.)
settings = AppSettings()

# Create Dishka container and give it:
# 1. The provider (recipe book)
# 2. The context (external objects like settings)
container = make_async_container(
    AppProvider(),  # Our recipe book
    context={AppSettings: settings},  # Give settings from outside
)

# Connect Dishka to FastAPI
# After this, FastAPI routes can use dependency injection!
setup_dishka(container, app)

# Step 5: Use dependency injection in your FastAPI routes


@app.get("/")
async def root():
    """Regular route - no dependency injection needed"""
    return {"message": "Hello World! Try /greet/YourName or /settings"}


@app.get("/greet/{name}")
@inject  # This decorator enables Dishka dependency injection
async def greet_user(
    name: str,  # Regular FastAPI parameter from URL
    greeting_service: FromDishka[
        GreetingService
    ],  # Dishka will provide this automatically!
):
    """
    Magic happens here!
    - Dishka sees you need GreetingService
    - Dishka creates AppSettings from context
    - Dishka creates GreetingService using AppSettings
    - Dishka gives you the ready-to-use GreetingService
    - You just use it! No manual object creation!
    """
    return {"greeting": greeting_service.greet(name)}


@app.get("/settings")
@inject  # Enable dependency injection
async def get_settings(settings: FromDishka[AppSettings]):
    """
    You can also directly inject the settings object!
    Dishka will get it from the context we provided earlier.
    """
    return {"app_name": settings.app_name, "debug": settings.debug}


# Step 6: Run the application
if __name__ == "__main__":
    print("Starting Dishka + FastAPI example...")
    print("What you'll see:")
    print("   1. Dishka creates GreetingService when first needed")
    print("   2. Same GreetingService instance used for all requests (singleton)")
    print("   3. Dependencies automatically injected into routes")
    print()
    print("Try these URLs:")
    print("   http://localhost:8000/")
    print("   http://localhost:8000/greet/Dinesh")
    print("   http://localhost:8000/settings")
    print("   http://localhost:8000/docs (FastAPI auto-generated docs)")
    print()

    uvicorn.run(app, host="0.0.0.0", port=8000)
