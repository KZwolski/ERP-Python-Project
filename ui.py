""" User Interface (UI) module """


def print_table(table, title_list):
    """
    Prints table with data.

    Example:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    column_width = list()
    for i in range(len(title_list)):
        column_width.append(len(title_list[i]))
    for i in range(len(table)):
        for j in range(len(title_list)):
            if len(table[i][j]) > column_width[j]:
                column_width[j]=len(table[i][j])
    table_size = 0
    for element in column_width:
        table_size += (element + 3)
    print('/'+ ('-' * (table_size-1)) +'\\')
    for i in range(len(title_list)):
        if i == 0:
            print('|', end="")
        print(' {0:^{1}} |'.format(title_list[i],column_width[i]), end="")
    for items in table:
        print('\n' + '|' + ('-' * (table_size-1)) + '|')
        for i in range(len(items)):
            if i == 0:
                print('|', end="")
            print(' {0:^{1}} |'.format(str(items[i]), column_width[i]), end="")
    print('\n'+ '\\' + ('-' * (table_size-1)) + '/')



def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, number, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    print("\n" + label)
    if type(result) == list:
        print("")
        for element in result:
            print(element)
        print("")
    elif type(result) == dict:
        for key, value in result.items():
            print(key, value)
        print("")
    else:
        print(result)
        print("")

def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    print(title)
    for i in range(len(list_options)):
        print(f' ({i+1}) {list_options[i]}')
    print(f' (0) {exit_message}')

    # your code


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>
    
    Args:
        list_labels (list): labels of inputs
        title (string): title of the "input section"

    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    inputs = []
    print(title)
    for element in list_labels:
        input_data = input(element)
        inputs.append(input_data)
    return inputs


def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code
    print(message)