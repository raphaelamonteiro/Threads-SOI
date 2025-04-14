# :bulb: Implementação de Threads com Controle de Execução em Linguagem Livre

O objetivo desta atividade é criar um programa que demonstre o uso de threads com controle de execução em uma linguagem de programação livre (por exemplo, C, C++, Java, Python, etc.).

### :snake: **Implementação em Python**
- criação de múltiplas threads
- controle de execução com `join`
-  uso de tempos aleatórios para simular cargas diferentes


---

### 🧠 **Explicações e Comentários**

1. **Execução Paralela:**
   - Cada thread executa a função `tarefa_thread`, simulando uma tarefa com tempo de duração aleatório. Isso simula diferentes cargas de trabalho.
   - As threads são iniciadas quase ao mesmo tempo e rodam em paralelo (concorrência real pode depender do sistema operacional e número de núcleos da CPU).

2. **Escalonamento pelo Sistema Operacional:**
   - O sistema operacional é responsável por escalonar a execução das threads.
   - Mesmo com múltiplas threads, nem todas rodam *simultaneamente* (a não ser que haja múltiplos núcleos). O SO alterna entre elas com base em prioridades, tempo de execução e uso de recursos.

3. **Sincronização com `join`:**
   - A função `join()` bloqueia a thread principal até que a thread filha correspondente termine.
   - Isso garante que o programa só exiba a mensagem final depois que **todas** as threads tiverem finalizado.
