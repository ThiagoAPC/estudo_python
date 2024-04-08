#Faça um programa que reproduza um audio de MP3
import pygame

#inicializa o mixer do pygame
pygame.mixer.init()

#carrega o arquivo mp3
pygame.mixer.music.load('C:/Users/tcorrea/OneDrive - Confidence Corretora de Câmbio S A/Área de Trabalho/Estudo Python\material/Rick Roll (Different link + no ads).mp3')

# Reproduzindo o arquivo MP3
pygame.mixer.music.play()

# Mantendo o programa em execução para permitir a reprodução
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)  # Ajuste para evitar consumo excessivo de CPU

