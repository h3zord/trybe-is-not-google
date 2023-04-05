from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue
import sys


def process(path_file, instance: Queue):
    line_list = txt_importer(path_file)

    new_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(line_list),
        "linhas_do_arquivo": line_list
    }

    for dict in instance.queue:
        if dict["nome_do_arquivo"] == path_file:
            return None

    instance.enqueue(new_dict)
    return print(new_dict, file=sys.stdout)


def remove(instance: Queue):
    if not len(instance):
        return print("Não há elementos", file=sys.stdout)

    deleted_dict = instance.dequeue()
    file_name = deleted_dict['nome_do_arquivo']

    return print(f"Arquivo {file_name} removido com sucesso", file=sys.stdout)


def file_metadata(instance: Queue, position):
    try:
        dict = instance.search(position)
        return print(dict, file=sys.stdout)
    except IndexError:
        return print("Posição inválida", file=sys.stderr)
