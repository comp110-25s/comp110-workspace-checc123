"""My first exercise in COMP110"""

__author__ = "730549548"


def greet(name_string: str) -> str:
    """A welcoming first function definition."""
    return "Hello," + name_string + "!"


if __name__ == "__main__":
    print(greet(name_string=input("What is your name?")))
