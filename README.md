# Web Scraper Mercado Livre 📊🕸️

Um scraper robusto para extração de dados de produtos do Mercado Livre com tratamento de erros, paginação automática e exportação para Excel.

## Funcionalidades Principais ✨
- Extração de dados completos de produtos (nome, preço, link)
- Paginação automática (até 5 páginas por padrão)
- Tratamento avançado de erros e reconexão
- Limpeza e formatação de dados
- Exportação para Excel
- Delay aleatório entre requisições para evitar bloqueio

## Pré-requisitos 📋
- Python 3.8+
- Pipenv (opcional mas recomendado)

## Instalação 🛠️

### Método 1: Usando Pipenv (recomendado)
```bash
git clone https://github.com/IsraelSiebre/Scrap-Mercado-Livre
cd mercado-livre-scraper
pipenv install
pipenv shell
```

### Método 2: Instalação tradicional
```bash
git clone https://github.com/IsraelSiebre/Scrap-Mercado-Livre
cd mercado-livre-scraper
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

## Uso 🚀
```bash
python main.py
```
Siga o prompt para inserir o produto desejado. O arquivo Excel será gerado automaticamente na área de trabalho.



## Estrutura do Projeto 📂
```
mercado-livre-scraper/
├── main.py            # Ponto de entrada principal
└── README.md          # Documentação
```

## Dependências 📦
- requests >=2.26.0
- beautifulsoup4 >=4.10.0
- pandas >=1.3.0
- python-dotenv >=0.19.0
- lxml >=4.6.3
