import tkinter as tk
from PIL import ImageTk, Image

# Create a list of photo paths
photos = ["Electro Giant.jpg", "Executioner.jpg", "Golem.jpg", "Firecracker.jpg"]


num_columns = 4
# Create the Tkinter window
window = tk.Tk()
window.title("Photo Table")

# Create a function to display the photos
def display_photos():
    num_photos = len(photos)
    num_rows = (num_photos + num_columns - 1) // num_columns
    
    for i in range(num_rows):
        for j in range(num_columns):
            index = i * num_columns + j
            
            # Check if there are remaining photos
            if index >= num_photos:
                break
            
            # Load the image
            image = Image.open(photos[index])
            # Resize the image if needed
            image = image.resize((200, 200), Image.ANTIALIAS)
            # Convert the image to Tkinter-compatible format
            photo = ImageTk.PhotoImage(image)
            
            # Create a label to display the photo
            label = tk.Label(window, image=photo)
            label.image = photo  # Store a reference to the photo
            label.grid(row=i, column=j, padx=10, pady=10)

# Call the function to display the photos
display_photos()

# Start the Tkinter event loop
window.mainloop()