import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog
import numpy as np
import tensorflow
from keras.applications import vgg16
from keras.preprocessing.image import img_to_array
from keras.applications.imagenet_utils import decode_predictions, preprocess_input


def load_img():
    global img, image_data
    for img_display in frame.winfo_children():
      img_display.destroy()
    image_data = filedialog.askopenfilename(initialdir="/", title="Choose an image",
                                            filetypes=(("all files", "*.*"), ("jpg files", "*.jpg"), ("png files", "*.png")))
    basewidth = 150  # Processing image for displaying
    img = Image.open(image_data)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.Resampling.LANCZOS)
    img = ImageTk.PhotoImage(img)
    file_name = image_data.split('/')
    panel = tk.Label(frame, text=str(file_name[len(file_name) - 1]).upper())
    panel.pack()
    panel_image = tk.Label(frame, image=img)
    panel_image.pack()


def classify():
    original = Image.open(image_data)
    original = original.resize((224, 224), Image.Resampling.LANCZOS)
    numpy_image = img_to_array(original)
    image_batch = np.expand_dims(numpy_image, axis=0)
    processed_image = vgg16.preprocess_input(image_batch.copy())
    predictions = vgg_model.predict(processed_image)
    label = decode_predictions(predictions)
    table = tk.Label(frame, text="Top image class predictions and confidences")
    table.pack()
    for i in range(0, len(label[0])):
      result = tk.Label(frame, text=str(label[0][i][1]).upper() + ': ' + str(round(float(label[0][i][2]) * 100, 3)) + '%')
      result.pack()


root = tk.Tk()
root.title('Portable Image Classifier')
root.iconbitmap('class.ico')
root.resizable(False, False)
tit = tk.Label(root, text="Portable Image Classifier", padx=25, pady=6, font=("", 12))
tit.pack()
canvas = tk.Canvas(root, height=500, width=500, bg='grey')
canvas.pack()
frame = tk.Frame(root, bg='white')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
chose_image = tk.Button(root, text='Choose Image',
                        padx=35, pady=10, fg="black", bg="grey",
                        relief="flat", bd=0, highlightthickness=0,
                        command=load_img)

chose_image.pack(side=tk.LEFT)
class_image = tk.Button(root, text='Classify Image',
                        padx=35, pady=10,
                        fg="black", bg="grey", command=classify)
class_image.pack(side=tk.RIGHT)
vgg_model = vgg16.VGG16(weights='imagenet')
root.mainloop()
