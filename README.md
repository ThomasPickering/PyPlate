# PyPlate
PyPlate is an attempt to make a python cli boilerplate.

The boilderplate includes:
- Menu with 2 submenus
- System Information
- Help
- clear screen module

## Why does this script exist ?
The scipt started out as my first really Python project. I quickly realised, that I was starting the whole project by doing a kind of boilderplate.
Therefore - here is my take on a python CLI Boilerplate.

The boilerplate is the product of 1 week of YouTube, Google and ChatGPT-4...

Please keep in mind that I am new to Python (at the time of writing), which means there are probably quite a few improvements that could be added to the script.

Let me know what you think - Have fun!

## Usage/Notes
### Menu
Below is the treesctructure of the menu

```
=== Main menu ===
[1]: Option 1
        === Sub menu 1 ===
        [1]: Option 1.1
        [2]: Option 1.2
        [B]: Back
[2]: Option 2
         === Sub menu 2 ===
        [1]: Option 2.1
        [2]: Option 2.2
        [B]: Back
[S]: System Information
        Python version
        Requirements
[H]: Help
        Print Help + Tips & Tricks
[Q]: Quit
        Exit program/script
```

Please notice, that there are 2 way 2 navigate back to the main menu:

 - Choice 1 returns to the sub menu
 - Choise 2 returns direcly to the main menu by calling `main_menu()`

```python
    if choice == "1":
        print('\n Option 1.1')
        input('\nTo return to {}Sub Menu 1{} hit {}<Enter>'.format(Fore.CYAN, Style.RESET_ALL, Fore.MAGENTA))
        # Returning to Sub menu 1

    elif choice == "2":
        print('\n Option 1.2')
        input('\nTo return to {}Main Menu{} hit {}<Enter>'.format(Fore.CYAN, Style.RESET_ALL, Fore.MAGENTA))
        main_menu() # Returning to the main menu
```
### Clear screen
Before the main menu is called, the screen is cleared. the defifition is in the `modules.py` file.
```python
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
```

## Requirements
- Python v3.10
- Colorama v0.4.6

## Useful links
- [colorama 0.4.6](https://pypi.org/project/colorama/ "pypi.org")

## Version History
* 1.1
    * Updated README.md file
    * Various bug fixes and optimizations
* 1.0
    * Initial Release

## License
Distributed under the MIT License. See `LICENSE.txt` for more information.

# Screenshots
## Main menu
![Skærmbillede 2023-04-13 kl  11 48 47](https://user-images.githubusercontent.com/6802324/231722455-22ec126c-5885-442f-96d1-09074929bf47.png)
### Sub menu 1
Sub menu 1 selected >> Option 1.1
![Skærmbillede 2023-04-13 kl  11 49 57](https://user-images.githubusercontent.com/6802324/231722872-22a3f2c1-336e-4dcb-88ea-75dfdc336198.png)


