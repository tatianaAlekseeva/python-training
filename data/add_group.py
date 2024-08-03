from generator.data_generators import random_string_with_prefix
from model.group import Group


testdata = [
    Group(name=name, header=header, footer=footer)
    for name in ["", random_string_with_prefix("name", 10)]
    for header in ["", random_string_with_prefix("header", 15)]
    for footer in ["", random_string_with_prefix("footer", 15)]
]