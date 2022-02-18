""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
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
    sales_table = data_manager.get_table_from_file("sales/sales.csv")
    options = ["Show Table",
                "Add",
                "Remove",
                "Update",
                "Get lowest price item",
                "Items sold between"]
    while True:
        ui.print_menu("Sales Menu", options, "Return to main menu")
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == "1":
            show_table(sales_table)
        elif option == "2":
            sales_table = add(sales_table)
        elif option == "3":
            id_ = ui.get_inputs([""], "Please type ID to remove: ")[0]
            sales_table = remove(sales_table, id_)
        elif option == "4":
            id_ = ui.get_inputs(["ID: "], "Please type ID to update: ")[0]
            sales_table = update(sales_table, id_)
        elif option == "5":
            ui.print_result(get_lowest_price_item_id(sales_table),"Lowest price item: ")
        elif option == "6":
            month_from = ui.get_inputs([""], "Please type starting month: ")[0]
            day_from = ui.get_inputs([""], "Please type starting day: ")[0]
            year_from = ui.get_inputs([""], "Please type starting year: ")[0]
            month_to = ui.get_inputs([""], "Please type ending month: ")[0]
            day_to = ui.get_inputs([""], "Please type ending day: ")[0]
            year_to = ui.get_inputs([""], "Please type ending year: ")[0]
            filtered_table = get_items_sold_between(sales_table, month_from, day_from, year_from, month_to, day_to, year_to)
            ui.print_result(filtered_table, "Titles sold between given dates ")
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
    title_list = ["Id", "Title", "Price", "Month", "Day", "Year"]
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
    new_data = ui.get_inputs(["Title", "Price", "Month", "Day", "Year"], "Please enter data for new record!")
    new_data.insert(0, common.generate_random(table))
    table.append(new_data)
    data_manager.write_table_to_file("sales/sales.py",table)
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
    data_manager.write_table_to_file("sales/sales.py", table)
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
    data_manager.write_table_to_file("sales/sales.py", table)
    return table


# special functions:
# ------------------

def get_lowest_price_item_id(table):
    """
    Question: What is the id of the item that was sold for the lowest price?
    if there are more than one item at the lowest price, return the last item by alphabetical order of the title

    Args:
        table (list): data table to work on

    Returns:
         string: id
    """
    price_list = []
    for list in table:
        price_list.append(int(list[2]))
    lowest_price = min(price_list)
    price_as_string = str(lowest_price)
    for list in table:
        if price_as_string in list[2]:
            result = list[0]
    return result
    



def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    """
    Question: Which items are sold between two given dates? (from_date < sale_date < to_date)

    Args:
        table (list): data table to work on
        month_from (int)
        day_from (int)
        year_from (int)
        month_to (int)
        day_to (int)
        year_to (int)

    Returns:
        list: list of lists (the filtered table)
    """
    filtered_table = []
    month_from = str(month_from)
    month_to = str(month_to)
    day_from = str(day_from)
    day_to = str(day_to)
    year_from = str(year_from)
    year_to = str(year_to)
    if len(month_to) != 2:
        month_to = "0" + month_to
    if len(month_from) != 2:
        month_from = "0" + month_from
    if len(day_to) != 2:
        day_to = "0" + day_to
    if len(day_from) != 2:
        day_from = "0" + day_from
    from_date = year_from + month_from + day_from
    to_date = year_to + month_to + day_to
    
    for i in range(len(table)):
        if len(table[i][3]) == 1:
            table[i][3] = "0" + table[i][3]
        if len(table[i][4]) == 1:
            table[i][4] = "0" + table[i][4]
        sale_date = table[i][5] + table[i][3] + table[i][4]
        if int(sale_date) > int(from_date) and int(sale_date) < int(to_date):
            filtered_table.append(table[i])

    for i in range(len(filtered_table)):
        filtered_table[i][2] = int(filtered_table[i][2])
        filtered_table[i][3] = int(filtered_table[i][3])
        filtered_table[i][4] = int(filtered_table[i][4])
        filtered_table[i][5] = int(filtered_table[i][5])
    return filtered_table