import threading
import time
import random

# Função que será executada por cada thread
def tarefa_thread(id_thread):
    """
    Simula uma tarefa com tempo de execução variável.
    Cada thread imprime seu início, dorme por um tempo aleatório e depois finaliza.
    """
    print(f"[THREAD-{id_thread}] Iniciando...")
    tempo_execucao = random.uniform(1, 5)  # Tempo entre 1 e 5 segundos
    time.sleep(tempo_execucao)
    print(f"[THREAD-{id_thread}] Finalizada após {tempo_execucao:.2f} segundos.")

def main():
    """
    Função principal que cria, inicia e sincroniza as threads.
    """

    num_threads = 5  # Número de threads a serem criadas
    threads = []

    print("Iniciando execução com múltiplas threads...\n")

    # Criação e inicialização das threads
    for i in range(num_threads):
        thread = threading.Thread(target=tarefa_thread, args=(i,))
        threads.append(thread)
        thread.start()

    # Aguarda a conclusão de todas as threads (sincronização)
    for i, thread in enumerate(threads):
        thread.join()
        print(f"[MAIN] Thread-{i} finalizada (join concluído).")

    # Todas as threads foram finalizadas neste ponto
    print("\n[MAIN] Todas as threads foram concluídas com sucesso.")
    print("[MAIN] Código de saída: 0 (sucesso)")

# Execução do programa
if __name__ == "__main__":
    main()
