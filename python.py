# Recebe a entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber um conceito e retornar sua respectiva descrição.
def descrever_conceito(conceito):
    if conceito == "Prompt Simples":
        return "Instrução direta e breve"
    elif conceito == "Prompt Contextual":
        return "Inclui informações adicionais para contexto"
    elif conceito == "Prompt Interativo":
        return "Inclui perguntas para envolver o usuário"
    elif conceito == "Prompt de Refinamento":
        return "Solicitação para melhorar uma resposta anterior"

# Imprime a descrição do conceito recebido na "entrada" através da função "descrever_conceito". 
print(descrever_conceito(entrada))
