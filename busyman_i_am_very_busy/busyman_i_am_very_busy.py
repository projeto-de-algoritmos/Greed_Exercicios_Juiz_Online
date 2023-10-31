def interval_scheduling(lista_inicio, lista_fim):
    conjunto_resultante = []

    index = list(range(len(lista_inicio)))
    index.sort(key=lambda i : lista_fim[i])
    momento_ultima_task = 0
    for i in index:
        if lista_inicio[i] >= momento_ultima_task:
            conjunto_resultante.append(i)
            momento_ultima_task = lista_fim[i]

    return conjunto_resultante


n_casos = int(input())
i = 0

while i <= n_casos+1:
    n_atividades = int(input())

    horario_inicio_tasks = []
    horario_fim_tasks = []

    for i in range(0, n_atividades):
        m, n = input().split()

        horario_inicio_tasks.append(int(m))
        horario_fim_tasks.append(int(n))

    result = interval_scheduling(horario_inicio_tasks, horario_fim_tasks)
    print(len(result))
    i += 1
