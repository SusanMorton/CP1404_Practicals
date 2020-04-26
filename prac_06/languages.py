""""uses the class programming language"""

from prac_06.programming_language import ProgrammingLanguage

def main():

    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(ruby)
    print(python)
    print(visual_basic)

    language_list = [ruby, python, visual_basic]

   # print(language_list)

    print("The dynamically typed languages are:")
    for language in language_list:
        if language.is_dynamic():
            print(language.name)



main()