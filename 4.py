"""Написать программу, которая сортирует список строк по длине, сначала
 по возрастанию, а затем по убыванию."""


from typing import List

def sort_strings_len(strings: List[str]) -> List[str]:
    strings.sort(key=len)
    return strings

def sort_strings_len_reverse(strings: List[str]) -> List[str]:
    strings.sort(key=len, reverse=True)
    return strings

def main():
    string_input = input('Введите список строк: ')
    strings_list = string_input.split()
    print(sort_strings_len(strings_list))
    print(sort_strings_len_reverse(strings_list))

if __name__ == '__main__':
    main()
