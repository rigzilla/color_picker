import maya.cmds as cmds
from functools import partial


# this script brings up an interface, that lets the user choose the drawing overrides color
# for any object in his maya scene. Especially when creating controllers, this comes in handy.
# For any questions, feedback and critique regarding this script, feel free to send me a mail at mail@rigzilla.co.uk
# Author: Stefan Wezel, April 2015
# For further information on this script, use pythons help function and read the docstrings


class Color_Picker():
	"""
	in order to run the script either just execute it in the script editor,
	or save it to your maya scripts directory 
	(default is: C:\Users\Swagosaur\Documents\your version\scripts) under color_picker.py
	and then execute following lines:

	import color_picker as cp
	reload(cp)
	cp.Color_Picker()

	from the script editor, or make a shelf button from it
	"""


	def __init__(self):

		#class var
		self.widgets = {}


		#call on the build UI method
		self.build_UI()


	def build_UI(self):
		"""
		creates the UI
		"""

		if cmds.window("color_picker_UI", exists = True):

			cmds.deleteUI("color_picker_UI")


		self.widgets["window"] = cmds.window("color_picker_UI", title = "Color", w = 400, h = 120, mnb = False, mxb = False)


		self.widgets["mainLayout"] = cmds.columnLayout(w = 400, h = 120)
		cmds.rowColumnLayout( numberOfColumns = 10 )
		


		#create buttons
		self.widgets["colourButton"] = cmds.button(label = "", w = 40, h = 40, bgc = [0, 0, 0], c = partial(self.pick_color, [1] ) )
		self.widgets["colourButton"] = cmds.button(label = "", w = 40, h = 40, bgc = [.722, .722, .722], c = partial(self.pick_color, [3] ) )
		self.widgets["colourButton"] = cmds.button(label = "", w = 40, h = 40, bgc = [0.502, .502, .502], c = partial(self.pick_color, [2] ) )
		self.widgets["colourButton"] = cmds.button(label = "", w = 40, h = 40, bgc = [.804, 0, .2], c = partial(self.pick_color, [4] ) )
		self.widgets["colourButton"] = cmds.button(label = "", w = 40, h = 40, bgc = [0, 0, .396], c = partial(self.pick_color, [5] ) )
		self.widgets["colourButton"] = cmds.button(label = "", w = 40, h = 40, bgc = [.02, .02, .957], c = partial(self.pick_color, [6] ) )
		self.widgets["colourButton"] = cmds.button(label = "", w = 40, h = 40, bgc = [0, .294, 0], c = partial(self.pick_color, [7] ) )
		self.widgets["colourButton"] = cmds.button(label = "", w = 40, h = 40, bgc = [.196, 0, 294], c = partial(self.pick_color, [8] ) )
		self.widgets["colourButton"] = cmds.button(label = "", w = 40, h = 40, bgc = [.784, 0, .784], c = partial(self.pick_color, [9] ) )
		self.widgets["colourButton"] = cmds.button(label = "", w = 40, h = 40, bgc = [.588, .294, .196], c = partial(self.pick_color, [10] ) )
		self.widgets["colourButton"] = cmds.button(label = "", w = 40, h = 40, bgc = [.234, .188, .188], c = partial(self.pick_color, [11] ) )
		self.widgets["colourButton"] = cmds.button(label = "", w = 40, h = 40, bgc = [.706, .196, 0], c = partial(self.pick_color, [12] ) )
		self.widgets["colourButton"] = cmds.button(label = "", w = 40, h = 40, bgc = [.980, .024, .024], c = partial(self.pick_color, [13] ) )
		self.widgets["colourButton"] = cmds.button(label = "", w = 40, h = 40, bgc = [.027, .973, .027], c = partial(self.pick_color, [14] ) )
		self.widgets["colourButton"] = cmds.button(label = "", w = 40, h = 40, bgc = [0, .294, .588], c = partial(self.pick_color, [15]) ) 	
		self.widgets["colourButton"] = cmds.button(label = "", w = 40, h = 40, bgc = [.980, .980, .02], c = partial(self.pick_color, [17] ) )
		self.widgets["colourButton"] = cmds.button(label = "", w = 40, h = 40, bgc = [.02, .980, .980], c = partial(self.pick_color, [18] ) )
		self.widgets["colourButton"] = cmds.button(label = "", w = 40, h = 40, bgc = [.02, .980, .784], c = partial(self.pick_color, [19] ) )
		self.widgets["colourButton"] = cmds.button(label = "", w = 40, h = 40, bgc = [.961, .706, .706], c = partial(self.pick_color, [20] ) )
		self.widgets["colourButton"] = cmds.button(label = "", w = 40, h = 40, bgc = [.961, .706, .501], c = partial(self.pick_color, [21] ) )
		self.widgets["colourButton"] = cmds.button(label = "", w = 40, h = 40, bgc = [.973, .973, .413], c = partial(self.pick_color, [22] ) )
		self.widgets["colourButton"] = cmds.button(label = "", w = 40, h = 40, bgc = [0, .686, .392], c = partial(self.pick_color, [23] ) )
		self.widgets["colourButton"] = cmds.button(label = "", w = 40, h = 40, bgc = [.588, .392, .196], c = partial(self.pick_color, [24] ) )
		self.widgets["colourButton"] = cmds.button(label = "", w = 40, h = 40, bgc = [.672, .672, .169], c = partial(self.pick_color, [25] ) )
		self.widgets["colourButton"] = cmds.button(label = "", w = 40, h = 40, bgc = [.392, .588, .196], c = partial(self.pick_color, [26] ) )
		self.widgets["colourButton"] = cmds.button(label = "", w = 40, h = 40, bgc = [.196, .672, .354], c = partial(self.pick_color, [27] ) )
		self.widgets["colourButton"] = cmds.button(label = "", w = 40, h = 40, bgc = [.173, .627, .627], c = partial(self.pick_color, [28] ) )
		self.widgets["colourButton"] = cmds.button(label = "", w = 40, h = 40, bgc = [.173, .392, .620], c = partial(self.pick_color, [29] ) )
		self.widgets["colourButton"] = cmds.button(label = "", w = 40, h = 40, bgc = [.427, .176, .627], c = partial(self.pick_color, [30] ) )
		self.widgets["colourButton"] = cmds.button(label = "", w = 40, h = 40, bgc = [.627, .176, .400], c = partial(self.pick_color, [31] )  ) 


		#show window
		cmds.showWindow(self.widgets["window"])



	#define partial function
	def pick_color(self, colors, *args):
		"""
		checks if anything is selected, then draws overrideEnabled
		"""
		
		sel = cmds.ls(sl = True)


		#check if any valid object is selected
		#check for type additionally!! 
		if len(sel) == 0:
			cmds.warning("Please select at least One valid object")
			return
			

		
		#loop selection and put in colors
		for obj in sel:
			for color in colors:
				cmds.setAttr(obj + '.overrideEnabled', 1)
				cmds.setAttr(obj + '.overrideColor', color)




if __name__ == "__main__":
	Color_Picker()
