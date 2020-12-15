# ------------------------------------------------------------------------ #
# Title: Assignment 09 Yong Son
# Description: Working with Modules
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# YSon, 12.12.2020, Add Main module to run other Classes on main module
# ------------------------------------------------------------------------ #
# TODO: Import Modules
if __name__ == "__main__":
    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of employee objects when script starts
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of employee objects
    # Let user add data to the list of employee objects
    # let user save current data to file
    # Let user exit program

# Main Body of Script  ---------------------------------------------------- #

try:
    strFileName = 'EmployeeData.txt'
    lstTable = []
    while True:
        # Show user a menu of options
        Eio.print_menu_items()
        # Get user's menu option choice
        strChoice = Eio.input_menu_options()
        if strChoice.strip() == '1':
            # Show user current data in the list of product objects
            lstFileData = Fp.read_data_from_file(strFileName)
            lstTable.clear()
            for line in lstFileData:
                lstTable.append(Emp(line[0], line[1], line[2].strip()))
            Eio.print_current_list_items(lstTable)
            continue
        elif strChoice.strip() == '2':
            # Let user add data to the list of product objects
            lstTable.append(Eio.input_employee_data())
            Eio.print_current_list_items(lstTable)
            continue
        elif strChoice.strip() == '3':
            # let user save current data to file and exit program
            Fp.save_data_to_file(strFileName, lstTable)
            Eio.print_current_list_items(lstTable)
            continue
        elif strChoice.strip() == '4':
            break

except Exception as e:
    print("There was an error! Check file permissions.")
    print(e, e.__doc__, type(e), sep='\n')

