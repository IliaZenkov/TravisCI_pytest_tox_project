#!/usr/bin/env python3
class substring():
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
        print(f'Substrings of "{self.string}": {self.list}')
        print(f'There are {self.count} substrings in {self.string}')

        return self.list, self.count


# driver code
#string = input("enter string: ")
#substring_object = substring(string)
#print(substring_object.list)
#print(substring_object.count)
