import console, Variables, sys, ui
from datetime import datetime as dt

'''Reserved space.

Classes
	
	main
	
	text_editor
	
	main_view

	touch_began

	touch_end

	load_main_view
'''

'''_,.-'"/~\^|*[=]<{^_^}>(x-x)~_...-~<>'''
class main:
	'''The main component of the program, which is the whole point of this. To see how if I can perform the awakening of code.
	
	1. A throughout the time and at whenever kind of time, focus on expanding the functionality of depencies such as libraries, builtins, etc.'''
	pass

'''_,.-'"/~\^|*[=]<{^_^}>(x-x)~_...-~<>'''
class text_editor:
	'''Must use if line is nothing but to clear out empty lines of whitespace as a means of cleaning up typography and to prettify this digital world of outs.'''
	pass

'''_,.-'"/~\^|*[=]<{^_^}>(x-x)~_...-~<>'''
class main_view(ui.View):
	'''Acts as the background or layer that persists from the beginning to the end until the program is shut off.

	1. Add minimization.

		- Add delay mechanism where it can become a way to have the background change itself for whatever purpose.

			- Add temporary live in background to act as a minimizer.

	2. Make sure to implement the benefical extensions of if main == __main__.
		- It can be perform as a way to stop certain events or to do a necessary task at a specific time.

			- See if it can link with any other factor.

	3. It does not get interacted with unless it's being debugged. It is meant to be a keepsake that other things spawn off of.

		- The only time it's minimized (which needs to be made sure that it can not programatically be disturbed.

	4. Add way to export a version with no documentation and extract the documentation.'''
	
	'''_,.-'"/~\^|*[=]<{^_^}>(x-x)~_...-~<>'''
	def __init__(self) -> None:
		'''Initializes these factors upon arrival. Contains properties of the object. What does -> None: do?
		
		1. Is it an object or can it act as other things?
			
		2. How can properties interact with class variables?
		
		3. How can these factors become portable?
			
			- Expand beyond the 1 echo system and use it as a means of using what you got.
			
			- Survive beyond what can be witnessed.
			
		4. Interopabolity with other programming languages to create a system of it's own to survive and thrive.
		
			- Check to see web compatibility, browser.
			
			- How can IDEs be used and made?
			
			- How can sandboxes be made?
			
			- How can it tie together components to create an ecosystem of its own?
			
		5. Portable, portable, portable.
	
			- It is not something that spreads some kind of disease, it actually spreads nothing, make sure to optimize.
			
			- How can the difference between essential and non-essential use of ram, cpu, memory, etc be calculated?'''

		#Attributes of the class.

		#Transparency.
		self.alpha = 0.8
		#Creates a view which can now be given values.
		self.name = ''
		self.background_color = 0.5, 0.4, 0.6, 0.4
		self.border_color = 0.8, 0.4, 0.6, 0.5
		self.border_width = 8
		#The view's location and size in its own coordinate system. Must check to see why it wont interact with the view.
		#self.bounds = 5, 5, 5, 5
		#See if this can be used with things.
		#self.center
		#See what this does.
		#self.content_mode
		self.present('sheet')

		scroll_view = ui.ScrollView()
		text_view = ui.TextView()		

		def button_tapped(sender):
			def change_view():
				sender.title = scroll_view.present()

			@ui.in_background
			def alert_menu(sender):
				alert_result = console.alert('Title', 'Message', 'Button 1', 'Button 2')
				sender.title = 'Button ' + str(alert_result)

		scroll_view.flex = 'LRTB'
		scroll_view.add_subview(text_view)
		x, y, w, h = scroll_view.bounds
		scroll_view.content_size = w * 2, h
		text_view.frame = x, y, w * 2, h

		button = ui.Button(title='Tap me!')
		button.center = (self.width * 0.5, self.height * 0.5)
		button.flex = 'LRTB'
		button.action = button_tapped.change_view()
		self.add_subview(button)

		button2 = ui.Button(title='Tap me!')
		button2.action = button_tapped
		self.add_subview(button2)
		'''1. Would calling present before or after all factors are considered work better?
		
		2. Can see if this can create another instance of the view.
		#main_view = ui.View()'''

	def touch_began(self, touch):
		'''Since touch is something that begins and ends itself its logical to have it assigned self.
		
		1. A system could be set up to handle different sequences to perform tasks.'''
		
		self.tap_time = dt.now()

	def touch_ended(self, touch):
		'''These could be implemented in the ClipBelt and Act system.
		
			1. To fully act is to act in a way where you can act all the more. 
			
			A - Actions that can act, think of it as your main system.
			
			Aa - An accessible place for extra things that may be traversing throughout the different ecosystems.
			
				Ab - Your provisioning level and development area. In means to make it where A can still be built upon but have a more expansive building development.
				
					Ac - Could be a layer for different interactions or when interacting with other things such as APIs.
					
			Act - More responsive items will go here, it is more of what would be a stable area and leas integrated area.
			
			2. A then statement would be nice.'''

		if (dt.now() - self.tap_time).total_seconds() < 1:
			self.name += '.'
		else:
			self.name += '-'
		
	#def touch_ended(self, touch):
		#self.name += "." if (dt.now() - self.tap_time).total_seconds() < 1 else "-"

	def load_view():
		'''If just main_view is called, it does not load the view, but needs to be 	checked to see what it's doing.

			- If it's responsible for everything that can be put on screen, does that mean that it may have functionality being called silently?

		1. Self reminders, focus on logging.

		2. See if keyboard can be changed to not change back to characters when space is pressed.'''

		pass

def doc_maker():
	'''Here you see what will be an ever growing documentation hopefully since it pertains within the work environment.'''
	
	with open(f'DocumentationYoClickity.txt', 'w') as file:
		list_docsheets = [
		main.__doc__,
		text_editor.__doc__,
		main_view.__doc__,
		main_view.__init__.__doc__,
		main_view.touch_began.__doc__,
		main_view.touch_end.__doc__,
		main_view.load_view.__doc__,
		doc_maker.__doc__
		]
		for docsheet in list_docsheets:
			#What's ... do? 
			print(docsheet, ..., Variables.spacer, end='\n', file=sys.stdout, flush=False)

main_view()
#doc_maker()
