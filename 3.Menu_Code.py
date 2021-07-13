# Add controls(widget)

self.__thisTextArea.grid(sticky=N + E + S + W)

# To open new file
self.__thisFileMenu.add_command(label="New",
                                command=self.__newFile)

# To open a already existing file
self.__thisFileMenu.add_command(label="Open",
                                command=self.__openFile)

# To save current file
self.__thisFileMenu.add_command(label="Save",
                                command=self.__saveFile)

# To create a line in the dialog
self.__thisFileMenu.add_separator()

# To terminate
self.__thisFileMenu.add_command(label="Exit",
                                command=self.__quitApplication)
self.__thisMenuBar.add_cascade(label="File",
                               menu=self.__thisFileMenu)

# To give a feature of cut
self.__thisEditMenu.add_command(label="Cut",
                                command=self.__cut)

# To give a feature of copy
self.__thisEditMenu.add_command(label="Copy",
                                command=self.__copy)

# To give a feature of paste
self.__thisEditMenu.add_command(label="Paste",
                                command=self.__paste)

# To give a feature of editing
self.__thisMenuBar.add_cascade(label="Edit",
                               menu=self.__thisEditMenu)

# To create a feature of description of the notepad
self.__thisHelpMenu.add_command(label="About Notepad",
                                command=self.__showAbout)
self.__thisMenuBar.add_cascade(label="Help",
                               menu=self.__thisHelpMenu)

self.__root.config(menu=self.__thisMenuBar)

self.__thisScrollBar.pack(side=RIGHT, fill=Y)

# Scrollbar will adjust automatically
# according to the content
self.__thisScrollBar.config(command=self.__thisTextArea.yview)
self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)
