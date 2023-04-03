import tkinter as tk
from tkinter import ttk
from PIL import ImageTk

class View(tk.Tk):
    """
    	The View part of the Pet Detective application.
	Creation date: February 10, 2023
	@author: Matt Ramey

	Attributes
	------
	controller : Controller
		The controller object is the controller part
		of the MVC for the Pet Detective application.
		It is necessary for communication with the
		Controller class.
        size : str
            Desired pet size.
        sound_level : str
            Desired pet noise level.
        activity_level : str
            Desired pet activity level.
        hair_length : str
            Desired pet hair or feather length.
        affection_level : str
            Desired pet affection level.
    """

    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.size = ""
        self.sound_level = ""
        self.activity_level = ""
        self.hair_length = ""
        self.affection_level = ""
        self.results_list = []

        self.search_options = "results ..."

        self.title("Pet Detective")
        self.configure(bg="white")
        self.option_add("*Font", "CenturyGothic 12")
        self.minsize(width=600, height=300)

        # Icon on top of page.
        self.iconbitmap("PetDetectiveIcon.ico")

        # Mainframe logo.
        logo_image = ImageTk.PhotoImage(file="PetDetectiveLogo.png")
        logo_widget = tk.Label(self, image=logo_image, bg="white")
        logo_widget.image = logo_image
        logo_widget.pack(padx=5, pady=5)

    def main(self):
        self.home_page()

    def remove_old_widgets(self, frame):
        """ Removes widgets from a frame.

        Parameters
        ------
        frame:
            Frame that must be cleared.
        """
        for widget in frame.winfo_children():
            # Removes widgets.
            widget.destroy()

    def reset(self):
        """ Resets window to original homepage. """

        # Removes the frames from the main window.
        self.results_button_frame.forget()
        self.results_top_frame.forget()
        self.results_frame.forget()
        # Removes the widgets from the frames in the results page.
        self.remove_old_widgets(self.results_button_frame)
        self.remove_old_widgets(self.results_top_frame)
        self.remove_old_widgets(self.results_frame)
        # Displays the homepage.
        self.home_page()

    def results_page(self):
        """ Displys results page. """

        # Frame holds results and buttons frames.
        self.results_frame = tk.Frame(self, bg="white")
        self.results_frame.pack(padx=5, pady=5)

        # Displays the results.
        results_description_string = "My inspection reveals the following pets ..."
        # Displays the instructions.
        results_description = tk.Label(self.results_frame,
                                              text=results_description_string,
                                              bg="white")
        results_description.pack(padx=5, pady=(20, 5))

        # Frame holds results listbox and scrollbar.
        self.results_top_frame = tk.Frame(self.results_frame)
        # Scrollbar.
        results_text_scrollbar = ttk.Scrollbar(self.results_top_frame, orient="vertical")

        # Calculates the number of pets returned from the pet database.
        number_of_pets = len(self.results_list)
        # The following dynamically determines the height of the text frame widget.
        text_widget_height = 0
        if number_of_pets == 0:
            text_widget_height = 3
        elif number_of_pets < 10:
            text_widget_height = number_of_pets
        # The height of the text frame widget will never exceed 10.
        else:
            text_widget_height = 10

        # Results list text widget.
        results_text = tk.Text(self.results_top_frame, wrap="word",
                                     borderwidth=0,
                                     highlightthickness=0,
                                     width=30,
                                     height=text_widget_height,
                                     yscrollcommand=results_text_scrollbar.set)

        results_text_scrollbar.configure(command=results_text.yview)

        # If there are more than 10 pet results, the scrollbar appears.
        if (number_of_pets == 10):
            results_text_scrollbar.pack(side="right", fill="y")

        results_text.pack()
        self.results_top_frame.pack(padx=10, pady=(20, 10))

        # No results message.
        no_results_message = "Unfortunately, there are no pets that are right for you. "
        no_results_message += "Maybe you should think of getting a plant or a rock."
        # Adds the no results message and centres it.
        if number_of_pets == 0:
            results_text.tag_configure("centre_text", justify="center")
            results_text.insert("1.0", no_results_message)
            results_text.tag_add("centre_text", "1.0", "end")

        # Displays pet database records and centres them.
        for index in range(number_of_pets):
            individual_result = self.results_list[index]
            breed = individual_result[1]
            variety = individual_result[2]
            result_string = breed + ": " + variety + "\n"
            results_text.tag_configure("centre_text", justify="center")
            results_text.insert("1.0", str(result_string))
            results_text.tag_add("centre_text", "1.0", "end")

        # Frame for buttons.
        self.results_button_frame = tk.Frame(self, bg="white")
        self.results_button_frame.pack(padx=10, pady=(20, 30))

        # Reset button image.
        reset_button_image = tk.PhotoImage(file="RESET.png")
        # Reset button.
        reset_button = tk.Button(self.results_button_frame,
                                 image=reset_button_image,
                                 bg="white",
                                 activebackground="white",
                                 borderwidth=0,
                                 cursor="hand2",
                                 command=self.reset)
        reset_button.grid(row=0, column=0, padx=5, pady=5)

        # Exit button image.
        exit_button_image = tk.PhotoImage(file="EXIT.png")
        # Exit button.
        exit_button = tk.Button(self.results_button_frame,
                                image = exit_button_image,
                                bg = "white",
                                borderwidth = 0,
                                cursor="hand2",
                                command=quit)
        exit_button.grid(row=0, column=1, padx=5, pady=5)

        self.mainloop()

    def home_page(self):
        """ Shows home page. """

        # User instructions for application.
        # Frame for instructions.
        self.options_description_frame = tk.Frame(self, bg="white")
        self.options_description_frame.pack()
        # These are the several lines of instructions.
        options_description_line_1 = "The pet detective will deduce which pets are right for you."
        options_description_line_2 = "First, you must tell the pet detective some facts."
        options_description_line_3 = "Please select one characteristic from each of the fields."
        options_description_line_4 = "All fields are required for this investigation."
        # Displays instructions.
        options_description_line_1 = tk.Label(self.options_description_frame,
                                              text=options_description_line_1,
                                              bg="white")
        options_description_line_1.pack(padx=5, pady=(20, 0))
        options_description_line_2 = tk.Label(self.options_description_frame,
                                              text=options_description_line_2,
                                              bg="white")
        options_description_line_2.pack(padx=5, pady=0)
        options_description_line_3 = tk.Label(self.options_description_frame,
                                              text=options_description_line_3,
                                              bg="white")
        options_description_line_3.pack(padx=5, pady=0)
        options_description_line_4 = tk.Label(self.options_description_frame,
                                              text=options_description_line_4,
                                              #fg="black",
                                              bg="white")
        options_description_line_4.pack(padx=5, pady=(0, 20))

        # Frame contains user options.
        self.options_frame = tk.Frame(self, bg="white")
        self.options_frame.pack()

        # There are several options that must be selected before searching
        # the database for the matching pet results.
        # These options will all be available using drop-down menus.
        # In Tkinter ttk these drop-down menus are known as combo boxes.

        # This is the default combo box text.
        default_option = "Pick an option..."

        def search_for_pets():
            """
            Retrieves pet matches.

            This is a helper function for the home_page function.
            """

            # Retrives and stores the combobox options.
            self.size = size_combo.get()
            self.sound_level = sound_combo.get()
            self.activity_level = activity_combo.get()
            self.hair_length = hair_combo.get()
            self.affection_level = affection_combo.get()

            # The following five if statements check to make sure that the combo box options
            # have been selected. If they have not, the unselected options are turned red.
            if self.size == default_option:
                size_label.configure(foreground="red")
                options_description_line_4.configure(fg="red")
            if self.size != default_option:
                size_label.configure(foreground="black")

            if self.sound_level == default_option:
                sound_label.configure(foreground="red")
                options_description_line_4.configure(fg="red")
            if self.sound_level != default_option:
                sound_label.configure(foreground="black")

            if self.activity_level == default_option:
                activity_label.configure(foreground="red")
                options_description_line_4.configure(fg="red")
            if self.activity_level != default_option:
                activity_label.configure(foreground="black")

            if self.hair_length == default_option:
                hair_label.configure(foreground="red")
                options_description_line_4.configure(fg="red")
            if self.hair_length != default_option:
                hair_label.configure(foreground="black")

            if self.affection_level == default_option:
                affection_label.configure(foreground="red")
                options_description_line_4.configure(fg="red")
            if self.affection_level != default_option:
                affection_label.configure(foreground="black")

            # This displays the results page.
            if (self.size != default_option) and (self.sound_level != default_option) and (self.activity_level != default_option) and (self.hair_length != default_option) and (self.affection_level != default_option):
                # Retieves list of pets.
                self.results_list = self.controller.search(self.size,
                                                           self.sound_level,
                                                           self.activity_level,
                                                           self.hair_length,
                                                           self.affection_level)
                # Destroy viewable widgets.
                self.remove_old_widgets(self.options_frame)
                self.remove_old_widgets(self.options_description_frame)
                self.remove_old_widgets(self.options_button_frame)
                # Remove visible frames.
                self.options_frame.forget()
                self.options_description_frame.forget()
                self.options_button_frame.forget()
                # This displays the results page.
                self.results_page()

        # This section is for the size option.
        # This creates the label with the user is asked to choose a size.
        # The question that is asked to the user.
        size_question = "Size"
        # This creates the label.
        size_label = ttk.Label(self.options_frame,
                              text=size_question,
                              background="white",
                              padding=5)
        # This adds the label to the window.
        size_label.grid(row=1, column=0, columnspan=1, sticky="E", padx=5, pady=5)

        # This section creates the drop-down menu for the Size option.

        # These are the only options available for size.
        size_options = ("Small", "Medium", "Large")

        # This creates the actual combo box. It is read-only, so no
        # additional options may be entered by the user. The only
        # available options are contained in the size_options variable.
        size_combo = ttk.Combobox(self.options_frame,
                                 state="readonly",
                                 values=size_options)
        # This sets the default option text.
        size_combo.set(default_option)
        # This adds the combo box to the window.
        size_combo.grid(row=1, column=1, columnspan=1, padx=5, pady=5)

        # This section is for the sound level option.
        # This creates the label with the user is asked to choose a sound level
        # The question that is asked to the user.
        sound_question = "Sound Level"
        # This creates the label.
        sound_label = ttk.Label(self.options_frame,
                               text=sound_question,
                               background = "white",
                               padding = 5)
        # This adds the label to the window.
        sound_label.grid(row=2, column=0, columnspan=1, sticky="E", padx=5, pady=5)

        # This section creates the drop-down menu for the Sound level option.
        # These are the only options available for size.
        sound_options = ("Quiet", "Loud")

        # This creates the actual combo box. It is read-only, so no
        # additional options may be entered by the user. The only
        # available options are contained in the sound_options variable.
        sound_combo = ttk.Combobox(self.options_frame,
                                  state="readonly",
                                  values=sound_options)
        # This sets the default option text.
        sound_combo.set(default_option)
        # This adds the combo box to the window.
        sound_combo.grid(row=2, column=1, columnspan=1, padx=5, pady=5)

        # This section creates the drop-down menu for the activity level option.

        # This creates the label with the user is asked to choose a size.
        # The question that is asked to the user.
        activity_question = "Activity Level"
        # This creates the label.
        activity_label = ttk.Label(self.options_frame,
                                  text=activity_question,
                                  background="white",
                                  padding=5)
        # This adds the label to the window.
        activity_label.grid(row=3, column=0, columnspan=1, sticky="E", padx=5, pady=5)

        # These are the only options available for activity level.
        activity_options = ("Low", "High")

        # This creates the actual combo box. It is read-only, so no
        # additional options may be entered by the user. The only
        # available options are contained in the size_options variable.
        activity_combo = ttk.Combobox(self.options_frame,
                                     state="readonly",
                                     values=activity_options)
        # This sets the default option text.
        activity_combo.set(default_option)
        # This adds the combo box to the window.
        activity_combo.grid(row=3, column=1, columnspan=1, padx=5, pady=5)

        # This section is for the hair or feather length option.
        # This creates the label with the user is asked to choose a hair length.
        # The question that is asked to the user.
        hair_question = "Hair or Feather Length"
        # This creates the label.
        hair_label = ttk.Label(self.options_frame,
                              text=hair_question,
                              background="white",
                              padding=5)
        # This adds the label to the window.
        hair_label.grid(row=4, column=0, columnspan=1, sticky="E", padx=5, pady=5)

        # This section creates the drop-down menu for the hair length option.
        # These are the only options available for size.
        hair_options = ("Bald", "Short", "Long")

        # This creates the actual combo box. It is read-only, so no
        # additional options may be entered by the user. The only
        # available options are contained in the hair_length variable.
        hair_combo = ttk.Combobox(self.options_frame,
                                 state="readonly",
                                 values=hair_options)
        # This sets the default option text.
        hair_combo.set(default_option)
        # This adds the combo box to the window.
        hair_combo.grid(row=4, column=1, columnspan=1, padx=5, pady=5)

        # This section is for the affection level option.
        # This creates the label with the user is asked to choose an affection level.
        # The question that is asked to the user.
        affection_question = "Affection Level"
        # This creates the label.
        affection_label = ttk.Label(self.options_frame,
                                   text=affection_question,
                                   background = "white",
                                   padding = 5)
        # This adds the label to the window.
        affection_label.grid(row=5, column=0, columnspan=1, sticky="E", padx=5, pady=5)

        # This section creates the drop-down menu for the affection level option.
        # These are the only options available for size.
        affection_options = ("Warm", "Cold")

        # This creates the actual combo box. It is read-only, so no
        # additional options may be entered by the user. The only
        # available options are contained in the affection_level variable.
        affection_combo = ttk.Combobox(self.options_frame,
                                      state="readonly",
                                      values=affection_options)
        # This sets the default option text.
        affection_combo.set(default_option)
        # This adds the combo box to the window.
        affection_combo.grid(row=5, column=1, columnspan=1, padx=5, pady=5)
        # Frame for buttons.
        self.options_button_frame = tk.Frame(self, bg="white")
        self.options_button_frame.pack(padx=10, pady=(20, 30))
        # Search button image.
        search_button_image = tk.PhotoImage(file="SEARCH.png")
        # Search button.
        search_button = tk.Button(self.options_button_frame,
                                 image=search_button_image ,
                                 bg="white",
                                 activebackground="white",
                                 borderwidth=0,
                                 cursor="hand2",
                                 command=search_for_pets)
        search_button.grid(row=0, column=0, padx=5, pady=5)
        # Exit button image.
        exit_button_image = tk.PhotoImage(file="EXIT.png")
        # Exit button.
        exit_button = tk.Button(self.options_button_frame,
                                image = exit_button_image,
                                bg = "white",
                                borderwidth = 0,
                                cursor="hand2",
                                command=quit)
        exit_button.grid(row=0, column=1, padx=5, pady=5)

        self.mainloop()