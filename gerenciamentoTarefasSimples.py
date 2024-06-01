def mostrar_opcoes():
    print('--------------------- ')
    print('')
    print('Nossas opções são: ')
    print('1 - Adicionar Tarefa')
    print('2 - Excluir Tarefa')
    print('3 - Exibir tarefa')
    print('4 - Sair')

def obter_opcao():
    while True:
        opcao = int(input('Digite aqui sua opção: '))
        if opcao >= 1 and opcao <= 4:
            return opcao
        else:
            print('Digite uma opção Válida. ')

def adicionar_tarefa(tarefas):
    tarefa = input('Digite aqui a tarefa para ser adicionada: ')
    tarefas.append(tarefa)
    print(f'Tarefa {tarefa} adicionada com sucesso. ')

def excluir_tarefa (tarefas):
    tarefa = input('Digite aqui a tarefa para ser excluída. (Pode escrever o índice da tarefa)')
    index = int(tarefa)
    if 0 <= index < len(tarefas):
        removida = tarefa.pop(index)
        print(f'Tarefa removida com sucesso. ')
    else:
        print('Índice fora do alcance. ')

def exibir_tarefas(tarefas):
    if not tarefas:
        print('Não está na lista de tarefas ')
    else:
        print('Lista de Tarefas:')
        for i, tarefa in enumerate(tarefas):
            print(f'{i} - {tarefa}')


def main():
    tarefas = []
    while True:
        mostrar_opcoes()
        opcao = obter_opcao()
        
        if opcao == 4:
            print('Saindo...')
            break
        
        if opcao == 1:
            adicionar_tarefa(tarefas)
        elif opcao == 2:
            excluir_tarefa(tarefas)
        elif opcao == 3:
            exibir_tarefas(tarefas)

if __name__ == "__main__":
    main()