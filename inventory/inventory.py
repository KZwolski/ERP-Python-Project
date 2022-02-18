""" Inventory module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string): Name of item
    * manufacturer (string)
    * purchase_year (number): Year of purchase
    * durability (number): Years it can be used
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
    inventory_table = data_manager.get_table_from_file("inventory/inventory.csv")
    options = ["Show Table",
                "Add",
                "Remove",
                "Update",
                "Available Items:",
                "Average durability by manufacturers"]
    while True:
        ui.print_menu("Inventory Menu", options, "Return to main menu")
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == "1":
            show_table(inventory_table)
        elif option == "2":
            inventory_table = add(inventory_table)
        elif option == "3":
            id_ = ui.get_inputs([""], "Please type ID to remove: ")[0]
            inventory_table = remove(inventory_table, id_)
        elif option == "4":
            id_ = ui.get_inputs(["ID: "], "Please type ID to update: ")[0]
            inventory_table = update(inventory_table, id_)
        elif option == "5":
            year = ui.get_inputs(["Year: "], "Please enter Year: ")[0]
            ui.print_result(get_available_items(inventory_table,year), f'Available items in {year} : ')
        elif option == "6":
            ui.print_result(get_average_durability_by_manufacturers(inventory_table), f'Average amounts of products made by manufacturer:  ')
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
    title_list = ["Id", "Name", "Manufacturer", "Purchase Year", "Durability"]
    ui.print_table(table,title_list)

    # your code


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """
    new_data = ui.get_inputs(["Name", "Manufacturer", "Purchase Year", "Durability"], "Please enter data for new record!")
    new_data.insert(0, common.generate_random(table))
    table.append(new_data)
    data_manager.write_table_to_file("inventory/inventory.csv",table)
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
    data_manager.write_table_to_file("inventory/inventory.csv", table)
    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    check = False
    updated_product = ui.get_inputs(["Name", "Manufacturer", "Purchase Year", "Durability"], "Please provide product information")
    for i in range(len(table)):
        if table[i][0] == id_:
            table[i][1] = updated_product[0]
            table[i][2] = updated_product[1]
            table[i][3] = updated_product[2]
            table[i][4] = updated_product[3]
            check = True
    if check == False:
        ui.print_error_message("Theres no such ID to be updated")
    data_manager.write_table_to_file("inventory/inventory.csv", table)
    return table


# special functions:
# ------------------

def get_available_items(table, year):
    """
    Question: Which items have not exceeded their durability yet (in a given year)?

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        list: list of lists (the inner list contains the whole row with their actual data types)
    """
    new_list = []
    for i in range(len(table)):
            if int(table[i][3]) + int(table[i][4]) > int(year) :
                new_list.append(table[i])
    for i in range(len(new_list)):
            new_list[i][3] = int(new_list[i][3])
            new_list[i][4] = int(new_list[i][4])
    return new_list


    # your code
def summarry_function(list):
    sum = 0
    for items in list:
        sum += items
    return sum


def get_average_durability_by_manufacturers(table):
    """
    Question: What are the average durability times for each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
        dict: a dictionary with this structure: { [manufacturer] : [avg] }
    """
    my_dict = {}
    for element in table:
        my_dict.setdefault(element[2], []).append(int(element[4]))
    new_dict = {}
    for k in my_dict:
        new_dict[k] = summarry_function((my_dict[k]))/int(len(my_dict[k]))
    return new_dict