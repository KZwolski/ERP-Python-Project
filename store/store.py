""" Store module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    store_table = data_manager.get_table_from_file('store/games.csv')
    options = ["Show Table",
                "Add",
                "Remove",
                "Update",
                "How many games are in the manufacture",
                "Average amount of games in stock"]
    while True:
        ui.print_menu("Store Menu", options, "Return to main menu")
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == "1":
            show_table(store_table)
        elif option == "2":
            store_table = add(store_table)
        elif option == "3":
            id_ = ui.get_inputs([""], "Please type ID to remove: ")[0]
            store_table = remove(store_table, id_)
        elif option == "4":
            id_ = ui.get_inputs(["ID: "], "Please type ID to update: ")[0]
            store_table = update(store_table, id_)
        elif option == "5":
            ui.print_result(get_counts_by_manufacturers(store_table),"Counts by Manufacturer: ")
        elif option == "6":
            manufacturer = ui.get_inputs(["Manufacturer: "], "Please type manufacturer: ")[0]
            ui.print_result(get_average_by_manufacturer(store_table,manufacturer), f'Average amounts of products made by {manufacturer} manufacturer  ')
        elif option == "0":
            break
        else:
            ui.print_error_message("Theres no such option")

def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """
    title_list = ["Id", "Title", "Manufacturer", "Price", "In_Stock"]
    ui.print_table(table,title_list)
   
def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """
    new_data = ui.get_inputs(["Title", "Manufacturer", "Price", "In_Stock"], "Please enter data for new record!")
    new_data.insert(0, common.generate_random(table))
    table.append(new_data)
    data_manager.write_table_to_file('store/games.csv',table)
    return table
    
def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """
    check = False
    for i in range(len(table)):
        if table[i][0] == id_:
            del table[i]
            check = True
    if check == False:
        ui.print_error_message("Theres no such ID in the file")
    data_manager.write_table_to_file('store/games.csv', table)
    return table
    
def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    # your code
    check = False
    updated_product = ui.get_inputs(["Title: ", "Manufacturer", "Price ", "In_Stock "], "Please provide product information")
    for i in range(len(table)):
        if table[i][0] == id_:
            table[i][1] = updated_product[0]
            table[i][2] = updated_product[1]
            table[i][3] = updated_product[2]
            table[i][4] = updated_product[3]
            check = True
    if check == False:
        ui.print_error_message("Theres no such ID to be updated")
    data_manager.write_table_to_file('store/games.csv', table)
    return table


# special functions:
# ------------------
def get_counts_by_manufacturers(table):
    """
    Question: How many different kinds of game are available of each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
         dict: A dictionary with this structure: { [manufacturer] : [count] }
    """
    my_dict = {}
    for element in table:
        my_dict.setdefault(element[2], []).append(element[1])
    new_dict = {}
    for k in my_dict:
        new_dict[k] = len(my_dict[k])
    return new_dict

def get_average_by_manufacturer(table, manufacturer):
    """
    Question: What is the average amount of games in stock of a given manufacturer?

    Args:
        table (list): data table to work on
        manufacturer (str): Name of manufacturer

    Returns:
         number
    """
    in_stock_counter =0
    manufacture_occurence =0
    for i in range(len(table)):
        if table[i][2] == manufacturer:
            in_stock_counter += int(table[i][4])
            manufacture_occurence += 1
    average = in_stock_counter/manufacture_occurence
    return average


    
