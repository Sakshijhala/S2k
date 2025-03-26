from tkinter import *
import calendar

# Function to display the calendar
def show():
    try:
        # Get the year from the entry field
        year = int(year_field.get())

        # Create a new window to display the calendar
        root = Toplevel(new)  # Use Toplevel instead of Tk() to prevent multiple main windows
        root.config(background="grey")
        root.title(f"Calendar - {year}")
        root.geometry('550x660')

        # Generate the calendar for the given year
        context = calendar.calendar(year)

        # Display the calendar inside the new window
        cal_year = Label(root, text=context, font=("Courier", 10, "bold"), justify=LEFT, bg="white")
        cal_year.pack(padx=10, pady=10)

    except ValueError:
        error_label.config(text="Please enter a valid year!", fg="red")  # Show error message

# Main application window
new = Tk()
new.config(background="grey")
new.title('Calendar')
new.geometry('300x250')

# UI Components
cal_label = Label(new, text="Calendar", bg="grey", font=("Times", 20, "bold"))
cal_label.pack(pady=10)

year_label = Label(new, text="Enter Year:", bg="dark grey")
year_label.pack(pady=5)

year_field = Entry(new)
year_field.pack(pady=5)

button = Button(new, text="Show Calendar", fg="black", bg="light grey", command=show)  # Call show() only when clicked
button.pack(pady=10)

error_label = Label(new, text="", bg="grey")  # Error label for invalid input
error_label.pack()

new.mainloop()  # Start the GUI event loop


