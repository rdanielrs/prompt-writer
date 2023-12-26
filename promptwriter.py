import pyperclip;
from time import sleep; 
word_loop = False;

"""
while True:
    prompt_phrase = input("Please write your input ")
    print(prompt_phrase)
    if prompt_phrase.find("{}") > -1:
        prompt_req = input("Please type your request")
        print()
"""

"""
prompt_phrase = input ("Please write your input ")
string1 = prompt_phrase[:prompt_phrase.find("{") + 1]
string2 = prompt_phrase[prompt_phrase.find("}"):]

print(string1)
print(string2)
prompt_req = "teste"

print(f"{string1}{prompt_req}{string2}")

"""


while True:
    prompt_phrase = input("Please type your input: ")
    if prompt_phrase.find("{}") > -1:
        word_loop = True;
        print("To leave this loop and restart the application, type 'end_word_loop'")
        while word_loop == True:
            prompt_req = input("Please type your prompt request: ");
            if prompt_req == 'end_word_loop':
                word_loop = False;
                print("Application restarted successfully!")
                break;
            else:
                string1 = prompt_phrase[:prompt_phrase.find("{")];
                string2 = prompt_phrase[prompt_phrase.find("}") + 1:];
                print(f"{string1}{prompt_req}{string2}");
                pyperclip.copy(f"{string1}{prompt_req}{string2}")
                print("Successfully copied to clipboard!");
                sleep(1.0)
                


