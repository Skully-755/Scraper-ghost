<palign="center">
  <img src="assets/.png" alt="Scraper Ghost" width="800">
</p>

# Scraper-ghost

Web scraper desenvolvido em Python para extração de dados de páginas estáticas e dinâmicas. Para páginas estáticas, utiliza as bibliotecas Requests e BeautifulSoup. Para páginas dinâmicas, emprega Selenium WebDriver com suporte a Chrome, Firefox e Edge. Os dados extraídos são armazenados em formato JSON.

O projeto encontra-se em fase beta.

---

## Dependências

- Python 3.8+
- requests
- beautifulsoup4
- lxml
- selenium
- pyfiglet
- rich

É necessário ter o WebDriver correspondente ao navegador escolhido (chromedriver, geckodriver ou edgedriver) instalado e disponível no PATH do sistema.

---

## Instalação

```bash
git clone https://github.com/Skully-755/Scraper-ghost.git
cd Scraper-ghost
pip install -r requirements.txt
```
---

### Ambiente Virtual (venv)

Recomenda-se o uso de um ambiente virtual para isolar as dependências do projeto.

**Criação e ativação:**

```bash
# Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```
---

## Utilização

```bash
python3 scraper-ghost.py 
```
---

## Licença

Este projeto está licenciado sob os termos da licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.