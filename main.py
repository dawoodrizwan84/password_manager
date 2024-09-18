from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip




# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project

def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # nr_letters = random.randint(8, 10)
    # nr_symbols = random.randint(2, 4)
    # nr_numbers = random.randint(2, 4)

    # password_list = []

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))


    letter_list = [choice(letters) for _ in range(randint(8, 10))]


    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    symbols_list = [choice(symbols) for _ in range(randint(2, 4))]


    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    numbers_list = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letter_list + symbols_list + numbers_list

    shuffle(password_list)

    password = "".join(password_list)
    input_password.insert(0, password)
    pyperclip.copy(password)

    # password = ""
    # for char in password_list:
    #   password += char

    # print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = input_website.get()
    email = input_email.get()
    password = input_password.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning", message="Fields cannot be empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the delails enteres: \nEmail: "
                                                     f"{email}\nPassword: {password}\nis it ok to save?")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                clear_text()



def clear_text():
    input_website.delete(0, END)
    input_password.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #

window  = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image = logo_img)
canvas.grid(column=1, row=0)

#Labels
website_text = Label(text="Website:", font=("Arial", 8, "bold"))
website_text.grid(column=0, row=1)

email_text = Label(text="Email/Username:", font=("Arial", 8, "bold"))
email_text.grid(column=0, row=2)

password = Label(text="Password:", font=("Arial", 8, "bold"))
password.grid(column=0, row=3)

#Entries
input_website = Entry(width=35)
input_website.grid(column=1, row=1, columnspan=2)
input_website.focus()

input_email = Entry(width=35)
input_email.grid(column=1, row=2, columnspan=2)
input_email.insert(0, "dawood@dummy.com")

input_password = Entry(width=21)
input_password.grid(column=1, row=3)

#Buttons
generate_button = Button(text="Generate Button", command=generate_password)
generate_button.grid(column=2, row=3)


add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan = 2)

window.mainloop()