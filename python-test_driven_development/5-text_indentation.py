#!/usr/bin/python3
def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    
    flag = 0
    for char in text:
        if flag == 1:
            if char == " ":
                continue
            flag = 0
        print(char, end="")
        if char in ".?:":
            print("\n")
            flag = 1
    print()
