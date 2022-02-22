from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import Tk


class Gui:
    def __init__(self) -> None:
        self.root = Tk()

    def splash_screen(self, main_function):
        self.root.title("Poster Maker")
        self.root.geometry("300x150")
        self.search_button = Button(
            self.root,
            text="Select Folder",
            command=lambda: self.on_clicked(main_function),
        ).pack()
        self.root.mainloop()

    def on_clicked(self, main_function):
        self.search_bar = filedialog.askdirectory(
            initialdir=None, title="Select Folder"
        )
        self.input_field = Entry(
            self.root,
        )
        self.input_field.pack()
        self.input_field.insert(0, "Movie Name")
        self.submit_button = Button(
            self.root,
            text="Start",
            command=lambda: self.on_clicked_start(
                main_function, MAIN_FOLDER=self.search_bar
            ),
        ).pack()

    def on_clicked_start(self, main_function, MAIN_FOLDER):

        self.gui_movie_name = self.input_field.get()
        self.start_scraper(main_function, MAIN_FOLDER=MAIN_FOLDER)

    def start_scraper(self, main_function, MAIN_FOLDER, *args, **kwargs):
        main_function(self.gui_movie_name, MAIN_FOLDER=MAIN_FOLDER, **kwargs)
        self.root.quit()

    def when_finished(self):
        messagebox.showinfo("Info", "Done")
