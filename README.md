# PyPlate
Python CLI BoilerPlate


Main Menu

![Skærmbillede 2023-04-13 kl  11 48 47](https://user-images.githubusercontent.com/6802324/231722455-22ec126c-5885-442f-96d1-09074929bf47.png)

Sub menu 1 selected >> Option 1.1
![Skærmbillede 2023-04-13 kl  11 49 57](https://user-images.githubusercontent.com/6802324/231722872-22a3f2c1-336e-4dcb-88ea-75dfdc336198.png)

Please notice, that there are 2 way 2 navigate back to the main menu:

Choice 1 returns to the sub menu

Choise 2 returns direcly to the main menu

        if choice == "1":
            print('\n Option 1.1')
            input('\nTo return to {}Sub Menu 1{} hit {}<Enter>'.format(Fore.CYAN, Style.RESET_ALL, Fore.MAGENTA))
            # Returning to Sub menu 1
        
        elif choice == "2":
            print('\n Option 1.2')
            input('\nTo return to {}Main Menu{} hit {}<Enter>'.format(Fore.CYAN, Style.RESET_ALL, Fore.MAGENTA))
            main_menu() # Returning to the main menu
