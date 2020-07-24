from cx_Freeze import setup, Executable

base = None

executables = [Executable("quiz.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {
        'packages':packages,
    },
}

setup(
    name = "ddong pihagi",
    options = options,
    version = "1.0",
    description = "inflearn pygame",
    executables = executables
)