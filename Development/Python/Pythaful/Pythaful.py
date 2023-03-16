import os, pathlib

'''
1. Confirm things end and are successful.
'''
spacer = '''
_,.-'"/~\^|*[=]<{^_^}>(x-x)~_...-~<>
'''
print(spacer)
root_list = []
file_list = []
dir_list = []
view_files = pathlib.Path()
safe_place = '/private/var/mobile/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3'
storage_place = '/private/var/mobile/Containers/Shared/AppGroup/DEBEE495-E92F-4067-A4CD-D91DC8759AC7/Pythonista3/Documents/Storage'
storage_file = '/private/var/mobile/Containers/Shared/AppGroup/DEBEE495-E92F-4067-A4CD-D91DC8759AC7/Pythonista3/Documents/Storage/filestorage.txt'


'''_,.-'"/~\^|*[=]<{^_^}>(x-x)~_...-~<>'''
class browser():
	'Explore the file system.'

#Views items in current directory.
#Add way to store variables.
#Add way to store file system in a structured form that stays up to date.
	def view_items():
		number = 0
		try:
			print(f'Current Directory\n\n{os.getcwd()}\n')
			
		except PermissionError:
			os.chdir(safe_place)
			print('Directory Files.\n')
		
		for item in view_files.iterdir():
			print(f'{number} - {item} - {"dir" if item.is_dir() else "file"}')
			number = number + 1
		print(spacer)

#Saves the root and items bwithin.
	

#Walks recursively through each item.
	def walk_directory():
		for root, dirs, files in os.walk(os.getcwd(), topdown=True):
			print('Root', root, '\n')
			print('Dirs', dirs, '\n')
			print('Files', files, '\n')
			dir_list.append(dirs)
			file_list.append(files)
			root_list.append(root)
	print(spacer)
	
#Saves the walk.
	def save_walk():
		file_list
		with open(storage_file, 'a') as file:
			for item in file_list:
				file.write(str(item))

#Moves to the parent directory of the current.
	def move_back():
		parent_directory = os.path.split(os.getcwd())
		os.chdir(parent_directory[0])
		
	print(spacer)
		
#Changes the directory or selects a file.
	def file_change_by_path():
		input = input('Name of file.\n')
		new_path = os.chdir(input)

	print(spacer)
class file_messer:
	'Messes with files.'

#See if it can make other files.
	def make_directory():
		os.mkdir(file)
		#os.makedirs() if it fails.
#See if it can remove other files.
	def remove_file():
		os.remove()
		#os.removedirs()
	
	def rename_file():
		os.rename()

	
'''_,.-'"/~\^|*[=]<{^_^}>(x-x)~_...-~<>'''
class file_handling:
	'Handles all files.'

#Write options.
	def write():
		write_input = input('''
What type of file write?
1. Blank
2. Write
''')
	#Writes a blank file.
		def write_blank():
			with open(input, 'w') as write_blank_file:
				write_blank_file
	#Writes in to a file.
		def write_write():
			with open(input, 'w') as write_file:
				write_file.write(input('What to write?'))
#Appends to a new line in a file.
	def append():
		with open(input, 'a') as append_file:
			append_file.write('\n')
			append_file.write(input('What to append?'))
#Reads each line in a file.
	def read():
		with open(input, 'r') as read_file:
			print(read_file.readlines())
#Copies a file to another.
	def copy():
		input = input('Copy to where?\n')
		open(input, 'w')

#Menus
'''_,.-'"/~\^|*[=]<{^_^}>(x-x)~_...-~<>'''
menu_flag = False
while menu_flag == False:
	menu = input('''
0. Exit
1. File Browser
2. File Handler
3. Browsedit
''')
	menu = int(menu)
	print(spacer)

	if menu == 0:
		menu_flag = True
	if menu == 1:
		browser_flag = False
		while browser_flag == False:
			browser_menu = input('''
0. Back
1. View Files
2. Walk Files
3. Save Walk
4. Move Back
5. Change Directory
''')
			browser_menu = int(browser_menu)

			if browser_menu == 0:
				browser_flag = True
			if browser_menu == 1:
				browser.view_items()
			if browser_menu == 2:
				browser.walk_directory()
			if browser_menu == 3:
				browser.save_walk()
			if browser_menu == 4:
				browser.move_back()
			if browser_menu == 5:
				browser.file_changer()

		print(spacer)
	
	if menu == 2:
		handler_flag = False
		while handler_flag == False:
			file_name = input('Name and extension.')
			handler_menu = input('''
0. Back
1. Write
2. Append
3. Read
4. Copy
5. Make Dir
6. 
''')
			handler_menu = int(handler_menu)
			if handler_menu == 0:
				handler_flag = True
			if handler_menu == 1:
				file_handling.write()
			if handler_menu == 2:
				file_handling.Append()
			if handler_menu == 3:
				file_handling.Read()
			if handler_menu == 4:
				file_handling.Copy()
				
	if menu == 3:
		browsedit_flag = False
		while browsedit_flag == False:
			browsedit_menu = input('''
0. Back
1. Remove Folders
2. Rename Folders
3. Make Directory
''')
			browsedit_menu = int(browsedit_menu)
			if browsedit_menu == 0:
				browsedit_flag = True
			if browsedit_menu == 1:
				file_messer.make_directory()
			if browsedit_menu == 2:
				file_messer.rename_file()
			if browsedit_menu == 3:
				file_messer.rename_file()
