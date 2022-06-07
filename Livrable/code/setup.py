# commande à taper en ligne de commande après la sauvegarde de ce fichier:
# python setup.py build

from cx_Freeze import setup, Executable
  
executables = [
        Executable(script = "code\main.py",icon = "images\icon.png", base = "Win32GUI" )
]
# ne pas mettre "base = ..." si le programme n'est pas en mode graphique, comme c'est le cas pour chiffrement.py.
  
buildOptions = dict( 
        includes = ["pygame","math","webbrowser"],
        include_files = ["code\menu.py"]
        # include_files = ["menu.py","pacman.py","space_invader.py","snake.py","p4.py","morpion.py","aliens.py","laser.py","obstacle.py","player.py"]
)
  
setup(
    name = "Mutigame",
    version = "1.0",
    description = "Plateforme de jeux",
    author = "Tristan Lailler",
    options = dict(build_exe = buildOptions),
    executables = executables
)