#!/usr/bin/env python3
class substring:
    def __init__(self, string):
        self.string = string
        self.list = []
        self.count = 0
        self.find_substrings()

    def find_substrings(self):
        """
        Finds all substrings of input string
        Sample Input : hello
        Sample Output : ['h', 'he', 'hel', 'hell', 'hello', 'e', 'el', 'ell', 'ello', 'l', 'll', 'llo', 'l', 'lo', 'o']

        :param none / self.string:
        :return: list of substrings as list, count of substrings as int
        """
        # Get all substrings of string and store them in an empty list
        for i in range(len(self.string)):
            for j in range(i + 1, (len(self.string) + 1)):
                self.list.append(self.string[i:j])
                self.count = self.count + 1

        # printing result
        print_substring(self)


class print_substring:
    def __init__(self, substrings):
        # print(substrings)
        if substrings.count > 10:
            print(f"There are {substrings.count} substrings in '{substrings.string}'")
            print(f"Substrings of '{substrings.string}': {substrings.list}")
        else:
            print(f"There are 10 or less substrings in '{substrings.string}', we don't need to know what they are.")
