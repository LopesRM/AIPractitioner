"""
Projeto: [Nome do Seu Projeto]

Estrutura de Pastas:

git/
└── content/
    └── Python Pratica/          # Códigos das aulas
        ├── aula1/               # Conteúdo da aula 1
        │   ├── codigos.py
        │   └── exemplos/
        ├── aula2/               # Conteúdo da aula 2
        │   ├── scripts.py
        │   └── exercicios/
        └── ...                  # Demais aulas

Como usar:
- Os códigos das aulas estão organizados por pastas numeradas
- Cada pasta contém os arquivos .py e subpastas quando necessário
- Execute os arquivos individuais para testar os exemplos
"""

def mostrar_estrutura():
    print("""
    Estrutura do Projeto:
    
    git/
    └── content/
        └── Python Pratica/      # Códigos das aulas
            ├── aula1/            # Conteúdo da aula 1
            │   ├── codigos.py
            │   └── exemplos/
            ├── aula2/            # Conteúdo da aula 2
            │   ├── scripts.py
            │   └── exercicios/
            └── ...               # Demais aulas
    """)

if __name__ == "__main__":
    print("Bem-vindo ao projeto de Python Prática!")
    print("Esta é a página inicial que explica a estrutura do projeto.\n")
    mostrar_estrutura()
    print("\nAcesse as pastas específicas para encontrar os códigos de cada aula.")