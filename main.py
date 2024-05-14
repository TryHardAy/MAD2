import csv


def import_from_csv(path: str):
    """
    Imports data from CSV file

    Args:
        path (str): Path to file

    Returns:
        list: data
        list: data column names
    """

    with open(path, 'r') as fileHandle:
        data = list(csv.reader(fileHandle))
        fileHandle.close()
    
    return data[1:], data[0]


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
