import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd
import joblib
# Define a function to load a CSV file and make predictions using the saved model
def predict_data():
    # Open a file dialog to select a CSV file
    file_path = filedialog.askopenfilename(title="Select prediction data file", filetypes=(("CSV files", "*.csv"),))

    # Load the data from the CSV file into a Pandas dataframe
    data = pd.read_csv(file_path, header=None)

    # Load the saved KNN model from a file
    knn_model = joblib.load('C:/Users/kushw/OneDrive/Desktop/Rock vs Mine project/rock_mine_prediction_model')

    # Make predictions on the data using the model
    predictions = knn_model.predict(data)

    # Show a message box with the predicted labels
    print(predictions)
    if predictions == 'M':
        s = "Mine"
    else:
        s = "Rock"
    messagebox.showinfo(title="Predictions", message=str(s))


# Create a Tkinter window
window = tk.Tk()

# Set the size of the window
window.geometry("300x100")

# Set the background color of the window
window.configure(bg="light gray")

# Get the width and height of the screen
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate the position of the window to center it on the screen
x = (screen_width - window.winfo_reqwidth()) / 2
y = (screen_height - window.winfo_reqheight()) / 2

# Set the position of the window
window.geometry("+%d+%d" % (x, y))

# Add a button to the window to select a CSV file and make predictions
button = tk.Button(window, text="Select prediction data", command=predict_data)
button.pack()

button_width = 150
button_height = 30
button_x = (300 - button_width) / 2
button_y = (100 - button_height) / 2

# Set the position of the button
button.place(relx=button_x / 300, rely=button_y / 100, relwidth=button_width / 300, relheight=button_height / 100)

# Run the Tkinter event loop

# Run the Tkinter event loop
window.mainloop()