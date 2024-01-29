import os
import subprocess
import tkinter as tk
from tkinter import filedialog

def select_webm_files():
    root = tk.Tk()
    root.withdraw()  # Para não abrir a janela completa do Tk
    file_paths = filedialog.askopenfilenames(filetypes=[("WebM files", "*.webm")])
    return list(file_paths)

def convert_webm_to_mp3(webm_files):
    if not webm_files:
        print("Nenhum arquivo selecionado.")
        return

    # Criar um diretório de saída no mesmo diretório do primeiro arquivo WEBM
    first_file_dir = os.path.dirname(webm_files[0])
    output_folder = os.path.join(first_file_dir, 'Converted_MP3')
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for webm_file in webm_files:
        base_name = os.path.basename(webm_file)
        mp3_file = os.path.join(output_folder, os.path.splitext(base_name)[0] + '.mp3')

        cmd = ['ffmpeg', '-i', webm_file, '-vn', '-ab', '128k', '-ar', '44100', '-y', mp3_file]
        subprocess.run(cmd)

    print("Conversão concluída!")

# Selecionando arquivos WEBM através da interface gráfica
webm_files = select_webm_files()

convert_webm_to_mp3(webm_files)
