# -*- coding: UTF-8 -*-
"""Refactoring.

This excercise is very similar to week 2, exercise 2. It contains a complete
and working example, but it's very poorly written.

Your job is to go through it and make it as good as you can.

That means making it self-documenting wherever possible, adding comments where
it isn't. Take repeated code and make it into a function. Also use functions
to encapsulate concepts. If something is done many times, maybe a map or a loop
is called for. Etc.

The resulting file should feel as close to english as possible.
It must also pass the linter.

This is the first file that will be run against the pydocstyle checker. If
you've run the week5_system_prep.sh file you should be getting blue linter dots
that show you where lintere errors are. If they aren't working, you should be
getting the errors in the test output.

Some functions will have directions as external comments, once you think you
are on top of it, take these comments out. Others won't have comments and
you'll need to figure out for yourself what to do.
"""

from __future__ import division
from __future__ import print_function
import math


# return a lit of countdown messages, much like in the bad function above.
# It should say something different in the last message.
def countdown(message, start, stop, completion_message):
    """Countdown to start."""
    for number in range(9, 0, -1):
        print(message + str(number))
    print(completion_message)


# TRIANGLES

# This should be a series of functions that are ultimatly used by
# triangle_master
# It should eventually return a dictionary of triangle facts. It should
# optionally print information as a nicely formatted string. Make printing
# turned off by default but turned on with an optional argument.
# The stub functions are made for you, and each one is tested, so this should
# hand hold quite nicely.
def calculate_hypotenuse(base, height):
    """Calculate hypotenuse."""
    hypotenuse = math.sqrt(base**2 + height**2)
    return hypotenuse


def calculate_area(base, height):
    """Calcuate area."""
    area = (0.5 * int(base) * int(height))
    return area


def calculate_perimeter(base, height):
    """Calculate perimeter."""
    perimeter = (base + height + calculate_hypotenuse)
    return perimeter


def calculate_aspect(base, height):
    """Calculate aspect."""
    if height > base:
        return "tall"
    elif height == base:
        return "equal"
    else:
        return "wide"


# Make sure you reuse the functions you've already got
# Don't reinvent the wheel
def get_triangle_facts(base, height, units="mm"):
    """Get triangle facts."""
    return {"area": calculate_area,
            "perimeter": calculate_perimeter,
            "height": height,
            "base": base,
            "hypotenuse": calculate_hypotenuse,
            "aspect": calculate_aspect,
            "units": units}


# this should return a multi line string that looks a bit like this:
#
# 15
# |
# |     |\
# |____>| \  17.0
#       |  \
#       |   \
#       ------
#       8
# This triangle is 60.0mm²
# It has a perimeter of 40.0mm
# This is a tall triangle.
#
# but with the values and shape that relate to the specific
# triangle we care about.
def tell_me_about_this_right_triangle(facts_dictionary):
    """Ask right triangle."""
    tall = """
            {height}
            |
            |     |\\
            |____>| \\  {hypotenuse}
                  |  \\
                  |   \\
                  ------
                  {base}"""
    wide = """
            {hypotenuse}
             ↓         ∕ |
                   ∕     | <-{height}
               ∕         |
            ∕------------|
              {base}"""
    equal = """
            {height}
            |
            |     |⋱
            |____>|  ⋱ <-{hypotenuse}
                  |____⋱
                  {base}"""

    pattern = ("This triangle is {area}{units}²\n"
               "It has a perimeter of {perimeter}{units}\n"
               "This is a {aspect} triangle.\n")

    facts = pattern.format(**facts_dictionary)
    height = facts_dictionary["height"]
    base = facts_dictionary["base"]

    if height > base:
        ret = tall.format(**facts_dictionary)
    elif height == base:
        ret = equal.format(**facts_dictionary)
    else:
        ret = wide.format(**facts_dictionary)

    ret = ret + "\n" + facts
    return ret


def triangle_master(base,
                    height,
                    return_diagram=False,
                    return_dictionary=False):
    """Triangle master."""
    dictionary = get_triangle_facts(base, height)
    diagram = tell_me_about_this_right_triangle(dictionary)
    if return_diagram and return_dictionary:
        return {"diagram": diagram, "facts": dictionary}
    elif return_diagram:
        return diagram
    elif return_dictionary:
        return dictionary
    else:
        print("You're an odd one, you don't want anything!")


def wordy_pyramid():
    """Wordy pyramid."""
    pyramid_list = list_of_words_with_lengths(range(3, 21, 2))
    pyramid_list2 = list_of_words_with_lengths(range(20, 3, -2))
    return (pyramid_list + pyramid_list2)


def get_a_word_of_length_n(length):
    """Word length."""
    baseURL = "http://www.setgetgo.com/randomword/get.php?len="
    if length >= 3 and isinstance(length, int):
        try:
            r = requests.get(baseURL + str(length)).text
            return r
        except Exception:
            pass


def list_of_words_with_lengths(list_of_lengths):
    """Word length."""
    wordList = []
    for length in list_of_lengths:
        word = get_a_word_of_length_n(length)
        wordList.append(word)
    return wordList


if __name__ == "__main__":
    print("Gay")
