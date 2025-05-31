# CadastroPessoas 📝
Aplicação em Python com interface de linha de comando que permite cadastrar nomes e idades de pessoas em um arquivo de texto. O sistema utiliza modularização para separar as responsabilidades entre entrada de dados, manipulação de arquivos e interface com o usuário. 

## 🚀 Funcionalidades

- 📄 Visualizar pessoas cadastradas  
- 🧍 Cadastrar uma nova pessoa (nome e idade)  
- 📂 Armazenamento automático em arquivo de texto (`dados.txt`)  
- ❌ Tratamento de erros (entrada inválida, arquivo não encontrado, etc.)  
- 🧱 Código modular (dividido em múltiplos arquivos Python)

---

## 📁 Estrutura do projeto

CadastroPessoas/
│
├── main.py # Arquivo principal que executa o sistema
├── interface.py # Interface do usuário (menu e navegação)
├── dados.py # Validação e entrada de dados
├── arquivo.py # Leitura e escrita no arquivo
└── dados.txt # Arquivo onde os cadastros são armazenados

💡 Exemplos de uso

----------------------------------------
MENU PRINCIPAL
----------------------------------------
1 - Ver pessoas cadastradas
2 - Cadastrar nova pessoa
3 - Sair do sistema
----------------------------------------
Sua opção: 2
Nome: João
Idade: 25

🛠️ Futuras melhorias

- Suporte para mais campos (telefone, email, etc.)
- Exportação para CSV
- Interface gráfica
- Busca por nome

📄 Licença
Este projeto é livre para uso educacional e pessoal. Sem restrições comerciais.

✍️ Autor
Feito com 💻 por Stefany Nicole — sinta-se à vontade para sugerir melhorias!
