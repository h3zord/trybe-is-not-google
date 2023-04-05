from ting_file_management.queue import Queue


def create_word_list(word, instance, content: bool):
    word_searches = []

    for file in instance.queue:
        word_search = {
                    "palavra": word,
                    "arquivo": file["nome_do_arquivo"],
                    "ocorrencias": []
                }

        for index, line in enumerate(file["linhas_do_arquivo"]):
            if word.lower() in line.lower():

                word_search["ocorrencias"].append(
                    {"linha": index + 1, "conteudo": line}
                ) if content else word_search["ocorrencias"].append(
                    {"linha": index + 1}
                )

        if len(word_search["ocorrencias"]):
            word_searches.append(word_search)

    return word_searches


def exists_word(word, instance: Queue):
    return create_word_list(word, instance, False)


def search_by_word(word, instance: Queue):
    return create_word_list(word, instance, True)
