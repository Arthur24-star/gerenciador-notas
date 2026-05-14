import random


# Lista de dicionários contendo os estudantes e suas notas
estudantes = [
    {
        "nome": "Arthur",
        "notas": [8.5, 7.0, 9.0]
    },

    {
        "nome": "Maria",
        "notas": [6.5, 7.5, 8.0]
    },

    {
        "nome": "Carlos",
        "notas": [5.0, 6.0, 4.5]
    }
]


def calcular_media(notas):
    """
    Calcula a média das notas de um estudante.

    Args:
        notas (list): Lista contendo notas do tipo float.

    Returns:
        float: Valor médio calculado a partir das notas.
    """

    media = sum(notas) / len(notas)

    return media


def verificar_aprovacao(media, media_minima=7.0):
    """
    Verifica a situação final do estudante.

    Args:
        media (float): Média final do estudante.
        media_minima (float): Média mínima para aprovação.

    Returns:
        str: Retorna 'Aprovado' ou 'Reprovado'.
    """

    if media >= media_minima:
        return "Aprovado"

    else:
        return "Reprovado"


def gerar_relatorio(alunos):
    """
    Gera um relatório completo de desempenho dos estudantes.

    Args:
        alunos (list): Lista de dicionários contendo os dados dos estudantes.

    Returns:
        None
    """

    print("\n=== RELATÓRIO DE DESEMPENHO ===")

    for aluno in alunos:

        nome = aluno["nome"]

        notas = aluno["notas"]

        media = calcular_media(notas)

        situacao = verificar_aprovacao(media)

        print(f"\nAluno: {nome}")

        print(f"Notas: {notas}")

        print(f"Média: {media:.2f}")

        print(f"Situação: {situacao}")

        print("-" * 30)


# Execução principal do sistema
gerar_relatorio(estudantes)