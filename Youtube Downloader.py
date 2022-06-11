# SCRIPT PARA DOWNLOAD DE VÍDEOS DO YOUTUBE, COM INTERFACE GRÁFICA

from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog


# Função para criação e organização da interface do programa
def Widgets():
    link_rotulo = Label(janela, text="Link                   :", bg="#E8D579")
    link_rotulo.grid(row=1, column=0, pady=5, padx=5)

    janela.linkTexto = Entry(janela, width=54, textvariable=video_Link)
    janela.linkTexto.grid(row=1, column=1, pady=5, padx=5, columnspan=2)

    destino_rotulo = Label(janela, text="Destino             :", bg="#E8D579")
    destino_rotulo.grid(row=2, column=0, pady=5, padx=5)

    janela.destinoTexto = Entry(janela, width=40, textvariable=destino_Download)
    janela.destinoTexto.grid(row=2, column=1, pady=5, padx=5)

    botao_destino = Button(janela, text="Procurar", command=Procurar, width=10)
    botao_destino.grid(row=2, column=2, pady=1, padx=1)

    botao_Download = Button(janela, text="Download", command=Download, width=20, bg="red", fg="white")
    botao_Download.grid(row=3, column=1, pady=3, padx=3)


# Função para procurar e selecionar a pasta onde o arquivo será salvo
def Procurar():
    diretorio_Download = filedialog.askdirectory(initialdir="ESCOLHA O LOCAL PARA SALVAR")
    destino_Download.set(diretorio_Download)


# Função para realizar o download do vídeo
def Download():
    Youtube_link = video_Link.get()
    download_Pasta = destino_Download.get()
    getVideo = YouTube(Youtube_link)
    videoStream = getVideo.streams.get_highest_resolution() # Com essa opção, o script vai escolher a melhor resolução do vídeo para baixar
    videoStream.download(download_Pasta)

    # Após concluir o download, abrirá uma nova janela confirmando que o download foi finalizado e a pasta de destino do arquivo
    messagebox.showinfo(f"SUCESSO!", f"DOWNLOAD SALVO EM:\n"
                                     f"{download_Pasta}")


# Criação da janela
janela = Tk()

janela.geometry("500x120")
janela.resizable(False, False)
janela.title("YOUTUBE DOWNLOADER")
janela.config(background="black")

# Especificando o tipo das variáveis
video_Link = StringVar()
destino_Download = StringVar()

# Chamando a função que irá montar a interface do programa, dentro da janela
Widgets()

janela.mainloop()
