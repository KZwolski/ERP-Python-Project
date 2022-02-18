""" Human resources module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * birth_year (number)
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
    hr_table = data_manager.get_table_from_file("hr/persons.csv")
    options = ["Show Table",
                "Add",
                "Remove",
                "Update",
                "Oldest person",
                "Persons closest to average age"]
    while True:
        ui.print_menu("HR Menu", options, "Return to main menu")
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == "1":
            show_table(hr_table)
        elif option == "2":
            hr_table = add(hr_table)
        elif option == "3":
            id_ = ui.get_inputs([""], "Please type ID to remove: ")[0]
            hr_table = remove(hr_table, id_)
        elif option == "4":
            id_ = ui.get_inputs(["ID: "], "Please type ID to update: ")[0]
            hr_table = update(hr_table, id_)
        elif option == "5":
            ui.print_result(get_oldest_person(hr_table),"Lowest price item: ")
        elif option == "6":
            ui.print_result(get_persons_closest_to_average(hr_table), "Titles sold between given dates ")
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
    title_list = ["ID","Name","Birth Year"]
    ui.print_table(table,title_list)



def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """
    new_data = ui.get_inputs(["Name","Birth Year"], "Please enter data for new record!")
    new_data.insert(0, common.generate_random(table))
    table.append(new_data)
    data_manager.write_table_to_file("hr/persons.csv",table)
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
    data_manager.write_table_to_file("hr/persons.csv", table)
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
    updated_product = ui.get_inputs(["Name","Birth Year"], "Please provide new information")
    for i in range(len(table)):
        if table[i][0] == id_:
            table[i][1] = updated_product[0]
            table[i][2] = updated_product[1]
            table[i][3] = updated_product[2]
            table[i][4] = updated_product[3]
            check = True
    if check == False:
        ui.print_error_message("Theres no such ID to be updated")
    data_manager.write_table_to_file("hr/persons.csv", table)
    return table


# special functions:
# ------------------

def get_oldest_person(table):
    """
    Question: Who is the oldest person?

    Args:
        table (list): data table to work on

    Returns:
        list: A list of strings (name or names if there are two more with the same value)
    """
    age_list = []
    oldest_persons = []
    for list in table:
        age_list.append(int(list[2]))
    lowest_year = min(age_list)
    str_year = str(lowest_year)
    for list in table:
        if str_year in list[2]:
            oldest_persons.append(list[1])
    return oldest_persons

    # your code


def get_persons_closest_to_average(table):
    """
    Question: Who is the closest to the average age?

    Args:
        table (list): data table to work on

    Returns:
        list: list of strings (name or names if there are two more with the same value)
    """
    years = []
    years_substraction = []
    persons_list = []
    summarry = 0
    for i in range(len(table)):
        years.append(int(table[i][2]))
    for i in range(len(years)):
        summarry += years[i]
    average_year = summarry/len(years)
    for i in range(len(years)):
        years_substraction.append(abs(average_year - years[i]))
    closest_value = min(years_substraction)
    for i in range(len(table)):
        if abs(average_year - int(table[i][2])) == closest_value:
            persons_list.append(table[i][1])
    return persons_list
    
