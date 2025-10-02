def add_task(task):
    tasks.append(task)
    print(f'Tarefa "{task}" adicionada com sucesso!')

def list_tasks():
    print('Tarefas:')
    for idx, task in enumerate(tasks, 1):
        print(f'{idx}. {task}')

def remove_task(index):
    try:
        task = tasks.pop(index - 1)
        print(f'Tarefa "{task}" removida com sucesso!')
    except IndexError:
        print('Índice inválido!')


tasks = []

while True:
    print ('O que deseja fazer?')
    print ('1 - Adicionar tarefa')
    print ('2 - Listar tarefas')
    print ('3 - Remover tarefa')
    print ('4 - Sair')

    choice = input('Escolha uma opção: ')

    if choice == '1':
        task = input('Digite a tarefa: ')
        add_task(task)
    elif choice == '2':
        list_tasks()
    elif choice == '3':
        index = int(input('Digite o índice da tarefa a ser removida: '))
        remove_task(index)
    elif choice == '4':
        print('Saindo...')
        break
    

