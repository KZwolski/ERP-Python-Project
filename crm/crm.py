""" Customer Relationship Management (CRM) module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * email (string)
    * subscribed (int): Is she/he subscribed to the newsletter? 1/0 = yes/no
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
    crm_table = data_manager.get_table_from_file("crm/customers.csv")
    options = ["Show Table",
                "Add",
                "Remove",
                "Update",
                "Get longest name",
                "Get subscribed emails"]
    while True:
        ui.print_menu("CRM Menu", options, "Return to main menu")
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == "1":
            show_table(crm_table)
        elif option == "2":
            crm_table = add(crm_table)
        elif option == "3":
            id_ = ui.get_inputs([""], "Please type ID to remove: ")[0]
            crm_table = remove(crm_table, id_)
        elif option == "4":
            id_ = ui.get_inputs(["ID: "], "Please type ID to update: ")[0]
            crm_table = update(crm_table, id_)
        elif option == "5":
            ui.print_result(get_longest_name_id(crm_table),"Lowest price item: ")
        elif option == "6":
            ui.print_result(get_subscribed_emails(crm_table), "Emails with subscription:  ")
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
    title_list = ["Id", "Name" , "Email", "Subscribed"]
    ui.print_table(table,title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """
    new_data = ui.get_inputs([ "Name" , "Email", "Subscribed"], "Please enter data for new record!")
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
    updated_product = ui.get_inputs(["Name" , "Email", "Subscribed"], "Please provide product information")
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
def last_alphabetical_sorted_person(table):
    for i in range(len(table)):
            for j in range(len(table)):
                if table[j]>table[i]:
                    temp = table[i]
                    table[i] = table[j]
                    table[j] = temp
    return table[-1]

def get_longest_name_id(table):
    """
        Question: What is the id of the customer with the longest name?

        Args:
            table (list): data table to work on

        Returns:
            string: id of the longest name (if there are more than one, return
                the last by alphabetical order of the names)
        """
    names = []
    names_lenght = []
    longest_names_persons = []
    for i in range(len(table)):
        names.append(table[i][1])
    for i in range(len(names)):
        names_lenght.append(len(names[i]))
    max_lenght = max(names_lenght)
    for i in range(len(table)):
        if len(table[i][1]) == max_lenght:
            longest_names_persons.append(table[i][1])
    for i in range(len(table)):
        if table[i][1] == last_alphabetical_sorted_person(longest_names_persons):
            id_ = table[i][0]
    return id_

    # your code


# the question: Which customers has subscribed to the newsletter?
# return type: list of strings (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):
    """
        Question: Which customers has subscribed to the newsletter?

        Args:
            table (list): data table to work on

        Returns:
            list: list of strings (where a string is like "email;name")
        """

    subs_mail = []
    for i in range(len(table)):
        if table[i][-1] == "1":
            subs_mail.append(str(table[i][2] + ";" + table[i][1]))
    return subs_mail
