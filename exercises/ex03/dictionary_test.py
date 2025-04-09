"""EX03: Dictionary Functions Unit Tests"""

__author__: str = "730549548"



from exercises.ex03.dictionary import invert
from exercises.ex03.dictionary import favorite_color
from exercises.ex03.dictionary import count
from exercises.ex03.dictionary import bin_len

def test_invert_use1() -> None:
    """Test for inverting a dictionary with unique values"""
    values = {"x": "1", "y": "2", "z": "3"}
    inverted = {"1": "x", "2": "y", "3": "z"}
    assert invert(values) == inverted


def test_invert_use2() -> None:
    """Test for inverting a dictionary with unique values"""
    values = {"Comp": "110", "Geog": "567", "Data": "130"}
    inverted = {"110": "Comp", "567": "Geog", "130": "Data"}
    assert invert(values) == inverted

def test_invert_edge1() -> None:
    """Test for inverting with empty dictionary"""
    values = {}
    assert invert(values) == {}

def test_count_use1() -> None:
    """Test count with a unique list of strings"""
    original: list[str] = ["a", "b", "a"]
    assert count(original) == {"a": 2, "b": 1}

def test_count_use2() -> None:
    """Test count with duplicates in the list"""
    original: list[str] = ["vanilla","vanilla","vanilla", "chocolate" ]
    assert count(original) == {"vanilla": 3, "chocolate": 1}

def test_count_edge1() -> None:
    """Test count with empty list"""
    original = []
    assert count(original) == {}

def test_favorite_color_use1() -> None:
    """Test favorite_color for value associated with fav color"""
    original = {"me": "blue", "you": "red", "other": "blue"}
    assert favorite_color(original) == "blue"

def test_favorite_color_use2() -> None:
    """Test favorite_color for value associated with first fav color if amount is tied, """
    original = {"me": "blue", "you": "red"}
    assert favorite_color(original) == "blue"

def test_favorite_color_edge1() -> None:
    """Test favorite_color with empty dictionary"""
    original = {}
    assert favorite_color(original) == ""

def test_bin_len_use1():
    """Test bin_len for correct word length in corresponding sets"""
    original = ["cats", "animals", "dogs"]
    assert bin_len(original) == {4: {"cats", "dogs"}, 7: {"animals"}}

def test_bin_len_use2():
    """Test bin_len for correct word length given words with variety of lengths"""
    original = ["the", "house", "was", "very", "big"]
    assert bin_len(original) == {3: {"the", "was", "big"}, 4: {"very"}, 5: {"house"}}

def test_bin_len_edge1():
    """Test bin_len with empty list"""
    original = []
    assert bin_len(original) == {}