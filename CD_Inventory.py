#------------------------------------------#
# Title: CD_Inventory.py
# Desc: Assignnment 08 - Working with classes, OOP
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# Maricha Friedman, 8/29/21, completed assignment, adding code to pseudocode
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD():
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:
        __str__: to return a formatted string for writing to file.
        CDList: count of how many object instantiatons there are.
        __incrementCount: private method to add to the new object counter.

    """
    # -- Fields --#
    __numCDs = 0
    # -- Constructor -- #
    def __init__(self, cd_id, cd_title, cd_artist):
        # -- Attributes -- #
        self.__cd_id = cd_id
        self.__cd_title = cd_title
        self.__cd_artist = cd_artist
        CD.__incrementCount()
    # -- Properties -- #
    @property
    def cd_id(self):
        return self.__cd_id
    
    @property
    def cd_title(self):
        return self.__cd_title
    
    @property
    def cd_artist(self):
        return self.__cd_artist
    
    @cd_id.setter
    def cd_id(self, val):
        if val is not int:
            raise Exception('The track position must be an integer.')
        else:
            self.__cd_id = val
            
    # -- Methods --#
    def __str__(self):
        cd = '{},{},{}\n'.format(self.cd_id, self.cd_title, self.cd_artist)
        return cd
    
    @staticmethod # since it's static method, we can't use "self" to call methods...
    def CDList():
        return '\nThere are {} CDs entered.'.format(CD.__numCDs)
    
    @staticmethod
    def __incrementCount():
        CD.__numCDs += 1
    
# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:
        None

    methods:
        save_inventory(file_name, table): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    def error_read_file(file_name):
        '''Evaluates if the file to be read exists in the directory.
        
        Args: 
            file_name (string): name of file used to write the data to
            
        Returns:
            Result (Boolean): True if file is in directory, False if not.
        '''
        try:
            with open(file_name, 'rb'):
                print('File found. Loading...')
                result = True
        except FileNotFoundError:
            print('File', file_name, 'not found.')
            result = False
        return result
    
    def load_inventory(file_name, table):
        '''Load inventory from .txt file and add to in-memory list
        
        arguments:
            file_name: .txt file to load data from
            table: the list of objects (CD Data) in memory
        Returns:
            None
        '''
        table.clear()
        objFile = open(file_name, 'r')
        for line in objFile:
            data = line.strip().split(',')
            load_cd = CD(data[0], data[1], data[2])
            table.append(load_cd)
        objFile.close()
        
    def save_inventory(file_name, table):
        '''Writes the in-memory inventory to a .txt file
        
        Args:
            file_name (string): name of file used to write the data to
            table (list of objects): the list of objects (CD Data) in memory
            
        Returns:
            None.
        '''
        objFile = open(file_name, 'w')
        for row in table:
            row = str(row)
            objFile.write(row)
        objFile.close()

# -- PRESENTATION (Input/Output) -- #
class IO:
    '''Handling Input / Output
    
    Methods:
        print_menu: displays menu options to user
        menu_choice: gets user input for menu selection
        show_inventory: Displays current inventory table
        inp_newcd: Gets user input to add new CD information to inventory.
        add_cd: Adds individual CD data to 2D list in memory
    '''
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] exit\n')
   
    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice


    @staticmethod
    def show_inventory(table):
        """Displays current inventory table

        Args:
            table (list of objects): the list of objects (CD Data) in memory

        Returns:
            None.

        """
        print('---------- The Current Inventory: ----------')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            row = str(row)
            row = row.strip()
            rowlst = row.split(',')
            print('{0}\t{1} \t(by: {2})\n'.format(*rowlst))
        print('--------------------------------------------')
        print(CD.CDList())
        print()# for better display spacing


    @staticmethod
    def inp_newcd():
        '''Gets user input to add new CD information to inventory.
        
        Args:
            None
            
        Returns:
            strID (integer): ID no. of CD
            strTitle (string): Title of CD
            strArtist (string): CD Artist's name
        '''
        while True:
            strID = input('Enter ID: ')
            try:
                int(strID)
                break
            except ValueError:
                print('That is not an integer, please try again. ')
        strID = strID.strip()
        strTitle = input('What is the CD\'s title? ').strip()
        strArtist = input('What is the Artist\'s name? ').strip()
        return strID, strTitle, strArtist
    
    def add_cd(table):
        '''Adds individual CD data to 2D list in memory
        
        Args:
            table: list of objects that holds the data during runtime.
            
        Retuns:
            cdObj: Instantiated CD object
        '''
        strID, strTitle, strArtist = IO.inp_newcd()
        cdObj = CD(strID, strTitle, strArtist)
        table.append(cdObj)
        return cdObj

# -- Main Body of Script -- #
# Load data from file into a list of CD objects on script start
if FileIO.error_read_file(strFileName) == True:
    FileIO.load_inventory(strFileName, lstOfCDObjects)
else: 
    print('No existing inventory file found. Inventory is empty.')

while True:
# Display menu to user
    IO.print_menu()
    strChoice = IO.menu_choice()
    # let user exit program
    if strChoice == 'x':
        break
    # let user load inventory from file
    if strChoice == 'l':
        if FileIO.error_read_file(strFileName) == True:
            print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
            strYesNo = input('type \'yes\' to continue and reload from file. Otherwise, reload will be canceled: ')
            if strYesNo.lower() == 'yes':
                print('reloading...')
                FileIO.load_inventory(strFileName, lstOfCDObjects)
                IO.show_inventory(lstOfCDObjects)
            else:
                input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
                IO.show_inventory(lstOfCDObjects)
        else:
            print('File not found. No data will be loaded.')
            continue
    # let user add data to the inventory
    elif strChoice == 'a':
        IO.add_cd(lstOfCDObjects)
        IO.show_inventory(lstOfCDObjects)
        continue
    # show user current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue
    # let user save inventory to file
    elif strChoice == 's':
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            FileIO.save_inventory(strFileName, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue
    else:
        print('General Error')
