import tkinter as tk
from tkinter import *
from tkinter import messagebox
import json
import requests

def extract_song_lyrics():
    artist_name = str(artist.get()).lower()
    song_name = str(song.get()).lower() 
    link = "https://api.lyrics.ovh/v1/"+artist_name.replace(' ', '%20')+'/'+song_name.replace(' ', '%20')

    req = requests.get(link)
    json_data = json.loads(req.content)

    try:
        lyrics = json_data["lyrics"]
        print(lyrics)
        messagebox.showinfo("Successfully Extracted Lyrics", "The lyrics for the song {} have been extracted".format(song_name.upper()))

    except:
        messagebox.showerror("Error","Enter the correct Song name and Artist name")

# Window Initialization
window = Tk()
window.title("Lyric Extractor")
window.geometry("700x220")
window.resizable(0, 0)
window.configure(bg="lightblue")

# Creating Labels and Entries using grid method
heading_label = tk.Label(window, text="Song Lyric Extractor", font=("Bushscript", 18, "bold"), bg="lightblue", fg="black")
heading_label.grid(row=0, column=0, columnspan=5, sticky="ew")

song_name_label = tk.Label(window, text="Song Name: ", font=("Courier", 18, "bold"), bg="lightblue", fg="black")
song_name_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

song = StringVar()
song_name_Entry = tk.Entry(window, width=40, textvariable=song, font=("Comic Sans", 14, "italic"))
song_name_Entry.grid(row=1, column=1, padx=10, pady=10)

artist_name_label = tk.Label(window, text="Artist Name: ", font=("Courier", 18, "bold"), bg="lightblue", fg="black")
artist_name_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

artist = StringVar()
artist_name_entry = tk.Entry(window, width=40, textvariable=artist, font=("Comic Sans", 14, "italic"))
artist_name_entry.grid(row=2, column=1, padx=10, pady=10)

Extract_Button = tk.Button(window, text='Song Extraction', font=("Bushscript", 18, "bold"), width=15, command=extract_song_lyrics)
Extract_Button.grid(row=3, column=0, columnspan=2, pady=20)

window.mainloop()
