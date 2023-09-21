import customtkinter
from PIL import Image, ImageTk
import os
import pandas as pd 
from cryptography.fernet import Fernet


"""
# Note => Run This Code only if The Key was lost..........
key = Fernet.generate_key()

with open("thekey.key", "wb") as w:
                w.write(key)
with open("project.py", "rb") as r:
                content = r.read()

content_enc = Fernet(key).encrypt(content)

with open("project.py", "wb") as w:
                w.write(content_enc)  
"""

customtkinter.set_appearance_mode("Dark")


class App(customtkinter.CTk):
    width = 900
    height = 600
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Library Management System")
        self.geometry(f"{self.width}x{self.height}")
        self.iconbitmap("arc.ico.ico")
        self.resizable(False, False)

        self.bg_image = customtkinter.CTkImage(Image.open("bg_gradient.jpg"),
                                               size=(self.width, self.height))
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=0, column=0)

        # create login frame........
        self.login_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.login_frame.grid(row=0, column=0, sticky="ns")
        self.login_label = customtkinter.CTkLabel(self.login_frame, text="Enter Username and Password ",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.login_label.grid(row=0, column=0, padx=30, pady=(150, 50))

        #Creating entry for username.............
        self.username_entry = customtkinter.CTkEntry(self.login_frame, width=200, placeholder_text="username")
        self.username_entry.grid(row=1, column=0, padx=40, pady=(15, 15))

        #Creating Entry for Password.........
        self.password_entry = customtkinter.CTkEntry(self.login_frame, width=200, show="*", placeholder_text="password")
        self.password_entry.grid(row=2, column=0, padx=30, pady=(0, 15))

        #Creating Login Button...........
        self.login_button = customtkinter.CTkButton(self.login_frame, text="Login", command=self.login_event, width=200)
        self.login_button.grid(row=3, column=0, padx=30, pady=(15, 15))

        # create main frame..........
        self.main_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_label = customtkinter.CTkLabel(self.main_frame, text="You Are Not Allowed Due to Incorrect UserName and Password",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.main_label.grid(row=0, column=0, padx=30, pady=(30, 15))
        
        #Creating Button Widget.....
        self.back_button = customtkinter.CTkButton(self.main_frame, text="Back", command=self.back_event, width=200)
        self.back_button.grid(row=1, column=0, padx=30, pady=(15, 15))

    def login_event(self):
        user_username = self.username_entry.get()
        user_password = self.password_entry.get()

        data = pd.read_csv("user.csv")
        
        saved_username = data["username"][0] #Getting username from csv file..
        saved_password = data["password"][0] #Getting password from csv file....

        if user_username == saved_username and user_password == saved_password:
            #Code used to Decrypt the file.........
            with open("thekey.key", "rb") as r:
                key = r.read()

            with open("project.py", "rb") as r:
                contents = r.read()
                contents_dec = Fernet(key).decrypt(contents)

            with open("project.py", "wb") as w:
                w.write(contents_dec)  


            with open("thekey.key", "wb") as e:
                e.write = ""
            
            #Executing library file programme........
            import project
            
            #Encrypting programme of project main file...........
            key = Fernet.generate_key()

            with open("thekey.key", "wb") as w:
                w.write(key)

            with open("project.py", "rb") as r:
                content = r.read()

            content_enc = Fernet(key).encrypt(content)

            with open("project.py", "wb") as w:
                w.write(content_enc)    
        
        else:
            self.login_frame.grid_forget()  # remove login frame
            self.main_frame.grid(row=0, column=0, sticky="nsew", padx=100)  # show main frame


    def back_event(self):
        self.main_frame.grid_forget()  # remove main frame
        self.login_frame.grid(row=0, column=0, sticky="ns")  # show login frame


if __name__ == "__main__":
    app = App()
    app.mainloop()
