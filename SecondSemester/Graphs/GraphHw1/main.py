# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from UI import UI


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    type_of_graphs_option = input("Enter u for undirected graphs and d for directed graphs")
    user_interface = UI()
    if type_of_graphs_option == 'd':
        user_interface.run_console_d()
    else:
        user_interface.run_console_u()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
