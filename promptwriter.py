import pyperclip;
from time import sleep; 
input_loop = True;
word_loop = False;

while input_loop == True:
    print("To cancel the application, type 'end_input_loop'");
    prompt_phrase = input("Please type your input: ");
    if prompt_phrase == 'end_input_loop':
        input_loop = False
        print("Application successfully closed")
        break;
    if prompt_phrase.find("{}") > -1:
        word_loop = True;
        print("To leave this loop and restart the application, type 'end_word_loop'");
        while word_loop == True:
            prompt_req = input("Please type your prompt request: ");
            if prompt_req == 'end_word_loop':
                word_loop = False;
                print("Application restarted successfully!");
                break;
            else:
                string1 = prompt_phrase[:prompt_phrase.find("{")];
                string2 = prompt_phrase[prompt_phrase.find("}") + 1:];
                print(f"{string1}{prompt_req}{string2}");
                pyperclip.copy(f"{string1}{prompt_req}{string2}");
                print("Successfully copied to clipboard!");
                sleep(1.0);
                


