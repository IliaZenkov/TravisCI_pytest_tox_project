from src.find_substrings.find_substrings import substring


def test_hello():
    string = "hello"
    substrings = substring(string)
    assert substrings.list == [
        
        "h",
        "he",
        "hel",
        "hell",
        "hello",
        "e",
        "el",
        "ell",
        "ello",
        "l",
        "ll",
        "llo",
        "l",
        "lo",
        "o",
    ]
    assert substrings.count == 15


def test_test():
    string = "test"
    substrings = substring(string)
    assert substrings.list == [
        "t",
        "te",
        "tes",
        "test",
        "e",
        "es",
        "est",
        "s",
        "st",
        "t",
    ]
    assert substrings.count == 10


def test_substring_print(capsys):
    string = "test"
    substring(string)
    captured = capsys.readouterr()
    assert (
        captured.out
        == "There are 10 or less substrings in 'test', we don't need to know what they are.\n"
    )

    string = "hello"
    substring(string)
    captured = capsys.readouterr()
    print(captured.out)
    assert (
        captured.out
        == "There are 15 substrings in 'hello'\n"
        + "Substrings of 'hello': ['h', 'he', 'hel', 'hell', 'hello', 'e', 'el', 'ell', 'ello', 'l', 'll', 'llo', 'l', 'lo', 'o']\n"
    )
