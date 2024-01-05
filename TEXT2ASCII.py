import pyfiglet
import os

def text_to_ascii_art(text, font='standard'):
    try:
        ascii_art = pyfiglet.figlet_format(text, font=font)
        return ascii_art
    except pyfiglet.FigletError as e:
        return str(e)

if __name__ == "__main__":

    # Clear the terminal
    os.system('clear')
    
    input_text = input("Enter the text you want to convert to ASCII art: ")
    selected_font = input("Enter the font name (press Enter for default 'standard' font): ").strip() or 'standard'

    result = text_to_ascii_art(input_text, font=selected_font)
    print("\nASCII Art:")
    print(result)
