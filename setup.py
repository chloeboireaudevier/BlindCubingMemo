import cx_Freeze

# base = "Win32GUI" allows your application to open without a console window
executables = [cx_Freeze.Executable('main.py', base = "Win32GUI")]

cx_Freeze.setup(
    name = "Blind Trainer",
    options = {"build_exe" : 
        {"packages" : ["pygame",'sys','random','pygame.freetype'], "include_files" : ['const.py','rubiks_icon.webp']}},
    executables = executables
)