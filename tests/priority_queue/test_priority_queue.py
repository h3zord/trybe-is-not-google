from ting_file_management.priority_queue import PriorityQueue
import pytest


file_test1 = {
    "nome_do_arquivo": "arquivo_teste1.txt",
    "qtd_linhas": 3,
    "linhas_do_arquivo": ["a", "b", "c"]
}

file_test2 = {
    "nome_do_arquivo": "arquivo_teste2.txt",
    "qtd_linhas": 5,
    "linhas_do_arquivo": ["d", "e", "f", "g", "h"]
}


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()

    priority_queue.enqueue(file_test1)
    priority_queue.enqueue(file_test2)

    assert len(priority_queue) == 2

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        priority_queue.search(99)

    assert priority_queue.is_priority(file_test2) is False

    assert priority_queue.search(0) == file_test1
    assert priority_queue.search(1) == file_test2
    assert priority_queue.dequeue() == file_test1
    assert priority_queue.dequeue() == file_test2
