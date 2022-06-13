# SCRIPT PARA DOWNLOAD DE VÍDEOS DO YOUTUBE, COM INTERFACE GRÁFICA
# Versão finalizada em 12/06/2022

from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog


# Função para criação e organização da interface do programa
def Widgets():
    link_rotulo = Label(janela, text="LINK        :", bg="#E8D579")
    link_rotulo.grid(row=1, column=0, pady=10, padx=10)

    janela.linkTexto = Entry(janela, width=54, textvariable=video_Link)
    janela.linkTexto.grid(row=1, column=1, pady=10, padx=5, columnspan=2)

    destino_rotulo = Label(janela, text="DESTINO :", bg="#E8D579")
    destino_rotulo.grid(row=2, column=0, pady=10, padx=10)

    janela.destinoTexto = Entry(janela, width=40, textvariable=destino_Download)
    janela.destinoTexto.grid(row=2, column=1, pady=10, padx=5)

    botao_destino = Button(janela, text="PROCURAR", command=Procurar, width=10)
    botao_destino.grid(row=2, column=2, pady=1, padx=1)

    botao_Download = Button(janela, text="DOWNLOAD", command=Download, width=20, bg="red", fg="white")
    botao_Download.grid(row=3, column=1, pady=5, padx=15)


# Função para procurar e selecionar a pasta onde o arquivo será salvo
def Procurar():
    diretorio_Download = filedialog.askdirectory()
    destino_Download.set(diretorio_Download)


# Função para realizar o download do vídeo
def Download():
    Youtube_link = video_Link.get()
    download_Pasta = destino_Download.get()
    getVideo = YouTube(Youtube_link)
    videoStream = getVideo.streams.get_highest_resolution()
    videoStream.download(download_Pasta)
    messagebox.showinfo("DOWNLOAD FINALIZADO", f"SEU VÍDEO FOI SALVO EM:\n"
                                                f"{download_Pasta}")


# Função para criar uma janela com informações sobre o programa
def Janela_Sobre():
    def WidgetSobre():
        separacao1 = Label(janelaSobre,
                           text="___________________________________________",
                           font="san-serif 10", background="#666666", fg="white")
        separacao1.place(x=42, y=30)

        info1 = Label(janelaSobre, text="YouTube Downloader", font="san-serif 20 bold", background="#666666", fg="white")
        info1.place(x=50, y=10)

        info2 = Label(janelaSobre, text=" Projeto criado utilizando Python e as seguintes bibliotecas:\n"
                                        "  * Pytube           [Para realizar o download dos vídeos]\n"
                                        "  * Tkinter           [Para a interface gráfica do programa]\n"
                                        "* Pyinstaller      [Para gerar este arquivo executável]", font="san-serif 10", background="#666666", fg="white")
        info2.place(x=20, y=60)

        separacao2 = Label(janelaSobre, text="------------------------------------------------------------------------------------------", font="san-serif 10", background="#666666", fg="white")
        separacao2.place(x=15, y=130)

        info3 = Label(janelaSobre, text="Scrip base: acervolima.com // Aprimoramento: Leo Rodrigues\n"
                                        "GitHub: https://github.com/leorodrigues91", font="san-serif 9", background="#666666", fg="white")
        info3.place(x=25, y=155)

        info4 = Label(janelaSobre, text="Versão: 1.0 (64bits), 12 de Junho de 2022", font="san-serif 9", background="#666666", fg="white")
        info4.place(x=75, y=190)

    janelaSobre = Tk()

    janelaSobre.geometry("400x220")
    janelaSobre.resizable(False, False)
    janelaSobre.title("Sobre YouTube Downloader")
    janelaSobre.config(background="#666666")

    WidgetSobre()

    janelaSobre.mainloop()

# Criação da janela
janela = Tk()

janela.geometry("430x150")
janela.resizable(False, False)
janela.title("YOUTUBE DOWNLOADER")

# Criando um Menu
menu = Menu(janela)
sobre_menu = Menu(menu)
sobre_menu.add_command(label="Sobre...", command=Janela_Sobre)
menu.add_cascade(label="Sobre", menu=sobre_menu, command=Janela_Sobre)

janela.config(background="black", menu=menu)

# Especificando o tipo das variáveis
video_Link = StringVar()
destino_Download = StringVar()

# Chamando a função para montar a interface do programa, com os botões e entradas
Widgets()

janela.mainloop()

# the base script found in: https://acervolima.com
# with improvements by Leo Rodrigues: https://github.com/leorodrigues91
