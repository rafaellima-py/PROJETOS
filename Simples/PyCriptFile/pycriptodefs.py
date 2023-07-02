from tkinter.filedialog import askdirectory
import pyAesCrypt
from pathlib import Path


diretorio = ''

def select_file():
    global diretorio
    file = askdirectory(parent=tabview.tab('Criptografar'))
    diretorio = file
    c_text_dir.set(diretorio)

   