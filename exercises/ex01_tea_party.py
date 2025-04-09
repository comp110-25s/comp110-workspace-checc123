"""Calculate the number of tea bags, treats, and expected cost of the tea party"""

__author__: str = "730549548"


def main_planner(guests: int) -> None:
    """To calculate items needed and cost of items for my tea party"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    # print(f"A Cozy Tea Party for {guests} People!")
    print("Tea bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print("Cost: $" + str(cost(tea_bags(people=guests), treats(people=guests))))


def tea_bags(people: int) -> int:
    """This function calculates the number of tea bags needed based on number of guests"""
    return people * 2

    print(tea_bags(people=334))


def treats(people: int) -> int:
    """This function calculates the number of treats neeeded based on number of teas"""
    return int(tea_bags(people=people) * 1.5)

    print(treats(people=334))


def cost(tea_count: int, treat_count: int) -> float:
    """Calculate cost of tea bags and treats combined"""
    return float(tea_count * 0.50) + float(treat_count * 0.75)

    print(cost(tea_count=668, treat_count=1002))


# main_planner(guests=0)
# main_planner(guests=2)
# main_planner(guests=334)

if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
