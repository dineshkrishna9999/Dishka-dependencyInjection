#one class can be accessed by multiple types
#
# SUMMARY:
# - Alias allows registering the same implementation for multiple interfaces
# - One Console class implements both Logger and Printer interfaces  
# - Using alias() makes the same instance available under different types
# - All references (Console, Logger, Printer) point to the same singleton object
# - Useful when a class implements multiple interfaces or needs multiple names

from dishka import Provider, Scope, make_container, provide, alias
from abc import ABC, abstractmethod

# === SIMPLE INTERFACES ===

class Logger(ABC):
    @abstractmethod
    def log(self, message: str) -> None:
        pass

class Printer(ABC):
    @abstractmethod
    def print_text(self, text: str) -> None:
        pass

# === CONCRETE CLASS ===

class Console:
    """One class that can act as both Logger and Printer"""
    
    def __init__(self):
        print("Console created")
    
    def log(self, message: str) -> None:
        print(f"[LOG] {message}")
    
    def print_text(self, text: str) -> None:
        print(f"[PRINT] {text}")

# === PROVIDER WITH ALIASES ===

class SimpleProvider(Provider):
    scope = Scope.APP
    
    # Provide the concrete class
    console = provide(Console)
    
    # Create aliases - same Console instance available as different types
    logger = alias(source=Console, provides=Logger)
    printer = alias(source=Console, provides=Printer)

# === EXECUTION ===

def main():
    print(">>> Simple Alias Example")
    print("=" * 25)
    
    container = make_container(SimpleProvider())
    
    # Get the same instance in different ways
    console = container.get(Console)
    logger = container.get(Logger)
    printer = container.get(Printer)
    
    # Use as Console
    console.log("Direct console log")
    
    # Use as Logger
    logger.log("Via Logger interface")
    
    # Use as Printer
    printer.print_text("Via Printer interface")
    
    # Verify they're the same instance
    print(f"\nSame instance? {console is logger is printer}")

if __name__ == "__main__":
    main()
