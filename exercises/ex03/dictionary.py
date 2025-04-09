"""EX03: Dictionary Functions"""

__author__: str = "730549548"


def invert(input: dict[str, str]) -> dict[str, str]:
    """function that inverts the keys and values in the dictionary"""
    invert_dict = {}  # initalizes an empty dictionary

    for key in input:  # goes through the keys in the input
        value = input[key]  # finding the associated value of each key
        if (
            value in invert_dict
        ):  # if value is already a key in dictionary, give an error
            raise KeyError(f"Duplicate key found: {value}")
        invert_dict[value] = key

    return invert_dict


def count(original: list[str]) -> dict[str, int]:
    """counting frequency of an item in the list"""
    counts = {}  # initializes an empty list
    for item in original:  # loops through every element in the list
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1

    return counts


def favorite_color(colors: dict[str, str]) -> str:
    """given a dictionary of names and favorite colors, we are looking for the most popular color"""
    color_count = {}  # initializes an empty dictionary
    for name in colors:  # loops through the keys and names in the dictionary
        color = colors[name]  # assigning the color value
        if color in color_count:  # taking a count of the colors
            color_count[color] += 1
        else:
            color_count[color] = 1

    most_pop_color = ""  # storing the most popular color here
    total = 0

    # looping over the colors in the given dictionary
    for colors in color_count:
        if color_count[colors] > total:
            total = color_count[colors]
            most_pop_color = colors

    return most_pop_color


def bin_len(bins: list[str]) -> dict[int, set[str]]:
    """Sorts words into sets according to their length"""
    result = {}  # initializes an empty dictionary
    i = 0   # loop through the list starting at index 0
    while i  < len(bins):   
        word =  bins[i]     # retrieves word that corresponds to whatever index i is at
        key = len(bins[i])  # examines the length of that same word
        if key in result:       # checks if the dictionary already has the key contains the value of the word's length
            result[key].add(word)   # adds word to the corresponding set
        else: 
            result[key] = set()     # if word is not already in dictionary, create empty set
            result[key].add(word)   # add word to empty set
        i += 1
    return result
