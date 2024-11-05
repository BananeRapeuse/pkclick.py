import sys
import keyboard
import ctypes
import time

# Fonction pour lire la version du fichier version.txt
def print_version():
    try:
        with open('version.txt', 'r') as version_file:
            version = version_file.read().strip()
            print(f"Software version: {version}")
    except FileNotFoundError:
        print("Version file not found. Make sure 'version.txt' exists in the same directory.")

# Fonction pour appuyer sur une touche spécifique en utilisant ctypes
def press_key(hexKeyCode):
    ctypes.windll.user32.keybd_event(hexKeyCode, 0, 0, 0)

def release_key(hexKeyCode):
    ctypes.windll.user32.keybd_event(hexKeyCode, 0, 2, 0)

# Fonction pour convertir la touche en son code hexadécimal
def get_key_code(key_char):
    return ord(key_char.upper())

# Fonction pour gérer l'attente en frames
def wait_for_frames(frames, fps):
    frame_duration = 1.0 / fps  # Durée d'une frame (1/fps secondes)
    for _ in range(frames):
        time.sleep(frame_duration)  # Attendre le temps d'une frame

# Fonction principale
def main():
    if len(sys.argv) > 1 and sys.argv[1] == '-V':
        print_version()
        return
    
    print("Hello! Welcome to pkclick!")
    
    # Demander le nombre de FPS
    fps = int(input("Please tell us the number of FPS (frames per second): "))

    # Demander le nombre d'advances (frames) à attendre
    frames_to_wait = int(input("Please tell us the number of 'advances' (frames) you have to wait: "))

    # Demander à l'utilisateur de définir la touche sur laquelle il veut que le programme appuie
    key_char = input("What is your 'A' touch? (Enter a single letter): ").strip()

    if len(key_char) != 1 or not key_char.isalpha():
        print("Please enter a valid single letter.")
        return

    key_code = get_key_code(key_char)
    print(f"Waiting for {frames_to_wait} advances (frames) at {fps} FPS before pressing '{key_char.upper()}'.")

    # Fonction pour gérer l'appui sur Ctrl+R
    def on_ctrl_r():
        print("Ctrl+R detected. Starting the frame countdown...")
        wait_for_frames(frames_to_wait, fps)  # Attendre le nombre de frames spécifié
        print(f"Pressing the '{key_char.upper()}' key...")
        press_key(key_code)  # Appuyer sur la touche choisie
        time.sleep(0.05)  # Pause pour simuler un vrai appui
        release_key(key_code)  # Relâcher la touche
        print(f"The '{key_char.upper()}' key has been pressed.")

    # Assigner l'appui de Ctrl+R à l'exécution de la fonction on_ctrl_r
    print("Press Ctrl+R to start the countdown.")
    keyboard.add_hotkey('ctrl+r', on_ctrl_r)

    # Garder le script actif en attente
    keyboard.wait()

# Lancer le programme principal
if __name__ == "__main__":
    main()
