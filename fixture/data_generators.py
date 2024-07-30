import random
import string


def random_string(maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_string_with_prefix(prefix, maxlen):
    return prefix + random_string(maxlen)


def random_name(maxlen):
    symbols = string.ascii_lowercase
    first_letter = random.choice(string.ascii_uppercase)
    return first_letter + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_email(maxlen, postfix):
    symbols = string.ascii_lowercase + string.digits + "-" * 5 + "_" * 2
    return "".join([random.choice(symbols) for i in range(random.randrange(2, maxlen))]) + postfix


def random_phone(prefix, maxlen):
    symbols = string.digits + "-" * 3
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
