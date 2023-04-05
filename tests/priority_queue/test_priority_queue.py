from ting_file_management.priority_queue import PriorityQueue
from ting_file_management.file_process import process
# import pytest


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()

    process("statics/arquivo_teste.txt", priority_queue)
    process("statics/nome_pedro.txt", priority_queue)
    process("statics/novo_paradigma_globalizado-min.txt", priority_queue)
    process("statics/novo_paradigma_globalizado.txt", priority_queue)

    print(priority_queue.search[0])
