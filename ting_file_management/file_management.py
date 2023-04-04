import sys


def txt_importer(path_file):
    if path_file.split(".")[-1] != "txt":
        return print("Formato inválido", file=sys.stderr)
    try:
        with open(path_file, "r") as txt_file:
            # return [line for line in txt_file.split("\n")]
            text = txt_file.read()
            return [line for line in text.split("\n")]
    except OSError:
        return print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
