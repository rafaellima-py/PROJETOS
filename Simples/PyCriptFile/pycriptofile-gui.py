import customtkinter as ctk
from pathlib import Path
from tkinter.filedialog import askdirectory
from PIL import Image
import pyAesCrypt


diretorio = ''
def select_file():
    global diretorio
    file = askdirectory(parent=tabview.tab('Criptografar'))
    text_dir.set(f'Diretório selecionado: {file}')
    diretorio = file
    
def d_select_file():
    global diretorio
    file = askdirectory(parent=tabview.tab('Descriptografar'))
    text_dir.set(f'Diretório selecionado: {file}')
    diretorio = file
    

def criptografar():
    senha = c_form_senha.get()
    if senha == '':
        mensagem_erro.set('Você precisa preencher uma senha')
    if diretorio == '':
        mensagem_erro.set('Você precisa  selecionar um diretório ')
        

    else:
        progress.pack()
        progress.start()         
        dir = Path(diretorio)
        pasta = dir.glob('**/*')
        for arquivo in pasta:
            if arquivo.is_file():
                try:
                    pyAesCrypt.encryptFile(infile=f'{arquivo}', outfile=f'{arquivo.absolute()}.pct', passw=senha, bufferSize=1024*1024)
                    
                except:
                    mensagem_erro.set('Algo deu errado, tente novamente')
                arquivo.unlink()
                print(arquivo.absolute())
        
        progress.stop()
        progress.pack_forget()
        print(senha)
        

def descriptografar():
    senha = d_form_senha.get()    
    if senha == '' and diretorio == '':
        mensagem_erro.set('Você precisa preencher uma senha e selecionar um diretório ')
    
    else:
  
        dir = Path(diretorio)
        pasta = dir.glob('**/*.pct')
       
        
        for arquivo in  pasta:
            if arquivo.is_file():
                original = arquivo.with_suffix('')
                
                try:
                    pyAesCrypt.decryptFile(str(arquivo), str(original), passw=senha, bufferSize=16*1024)
                    if '.pct' in arquivo.name:
                        arquivo.unlink()
                except ValueError:
                    mensagem_erro.set('A senha está incorreta')
     
        confirm.set('CONCLUIDO')
        print(senha)
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')
app = ctk.CTk()
app.geometry('620x480')
app.resizable(False,False)
app.title('PyCryptoFile')
app.iconbitmap('icone.ico')

tabview = ctk.CTkTabview(app, width=800)
tabview.pack()
tabview.add('Criptografar')
tabview.add('Descriptografar')
tabview.tab('Criptografar').grid_columnconfigure(0, weight=1)
tabview.tab('Descriptografar').grid_columnconfigure(0, weight=1)

c_image = ctk.CTkImage(Image.open('logo.png'), size=(200,200))
c_image_label = ctk.CTkLabel(master=tabview.tab('Criptografar'), image=c_image, text=' ').pack()
c_texto_file = ctk.CTkLabel(master=tabview.tab('Criptografar'), text='Selecione Um diretório:',
font=('',13)).pack(padx=10)

c_botao_file = ctk.CTkButton(master=tabview.tab('Criptografar'), text='Selecionar Pasta',
width=300,height=40, font=('',12),command=select_file )
c_botao_file.pack()



c_form_senha = ctk.CTkEntry(master=tabview.tab('Criptografar'),
placeholder_text='Escolha uma senha segura', width=300, show='*')
c_form_senha.pack(pady=20)

c_botao_criptografar = ctk.CTkButton(master=tabview.tab('Criptografar'),text='Criptografar Pasta',
command=criptografar, width=300)
c_botao_criptografar.pack()


d_image = ctk.CTkImage(Image.open('logo.png'), size=(200,200))
d_image_label = ctk.CTkLabel(master=tabview.tab('Descriptografar'), image=c_image, text=' ').pack()
d_texto_file = ctk.CTkLabel(master=tabview.tab('Descriptografar'), text='Selecione Um diretório:',
font=('',13)).pack(padx=10)


d_botao_file = ctk.CTkButton(master=tabview.tab('Descriptografar'), text='Selecionar Pasta',
width=300,height=40, font=('',12),command=select_file)
d_botao_file.pack()

d_form_senha = ctk.CTkEntry(master=tabview.tab('Descriptografar'),
placeholder_text='Informe a senha que você escolheu', width=300, show='*')
d_form_senha.pack(pady=20)

d_botao_criptografar = ctk.CTkButton(master=tabview.tab('Descriptografar'),text='Descriptografar Pasta',
command=descriptografar, width=300)
d_botao_criptografar.pack()


progress = ctk.CTkProgressBar(app, mode='indeterminate')
mensagem_erro = ctk.StringVar()
mensagem_erro_text = ctk.CTkLabel(app, textvariable=mensagem_erro, text_color='red', font=('', 15))
mensagem_erro_text.pack()


confirm = ctk.StringVar()
confirm_text = ctk.CTkLabel(app, textvariable=confirm, text_color='green',font=('', 15))
confirm_text.pack_forget()


text_dir = ctk.StringVar()
text_dir_text = ctk.CTkLabel(app, textvariable=text_dir)
text_dir_text.pack()


app.mainloop()