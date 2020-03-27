COLOUR_DICT = {'DodgerBlue1': '#1e90ff', 'blue1': '#0000ff', 'brown': '#a52a2a', 'chartreuse1': '#7fff00', 'cyan1': '#00ffff', 'DarkOrange': '#ff8c00', 'DarkOrchid': '#9932cc', 'DeepPink1': '#ff1493', 'gold1': '#ffd700', 'gray1': '#030303'}

print(COLOUR_DICT)

colour_choice = input("Enter a colour name: ")

while colour_choice != "":
    if colour_choice in COLOUR_DICT:
        print('The hexadecimal code for the colour {} is {}'.format(colour_choice, COLOUR_DICT[colour_choice]))
    else:
        print("Invalid colour choice")
    colour_choice = input("Enter a colour name: ")
