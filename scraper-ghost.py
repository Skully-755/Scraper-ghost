#requests
#beautifulsoup4
#lxml
#json
#time
#random
#selenium

"""Web Scraper direcionado a páginas estáticas e dinamicas! Use-o conforme o possível! Como está em beta, irão surgir ERROS...! No campo da URL, 
não é recomendável utilizar 
endpoints para a enumeração de DNS."""

from selenium.common.exceptions import WebDriverException
from pyfiglet import Figlet
from rich.console import Console
from rich.panel import Panel
import xml.etree.ElementTree as ET
import json
import requests
import time
import random
from bs4 import BeautifulSoup
import subprocess
from selenium import webdriver

class main:
    def __init__(self):

        subprocess.run(['clear'])

        console = Console()
        fig = Figlet(font="slant")
        logo = fig.renderText("Scraper Ghost")
        console.print(
            Panel(logo,border_style="red",expand=False))

        print("[INICIANDO]...")
        time.sleep(1)
        
        self.driver = input("Qual Web driver você utiliza? (Disponiveis: Firefox && Chrome && Edge): ")

        self.navegadores = { 
            "Chrome": webdriver.Chrome,
            "Firefox": webdriver.Firefox,
            "Edge": webdriver.Edge
                            }
        self.nav = ''
        try:
            for key, _ in self.navegadores.items():
                if key == self.driver:
                    self.nav = self.navegadores[self.driver]()
                    print("Web driver suportado!")
                    print("Testando...")
                    self.nav.quit()
                    break
                elif not self.driver or len(self.driver) < 2:
                    print("Sem Web Driver?")
                    return
                else:
                    print("Web driver não suportado!")
                    continue
        except WebDriverException as e:
            print(f"Erro no Web Driver: {e}")

        self.url = input("Digite a url ( Ex: https://www.youtube.com ): ")
        self.headers = {
            "Host": "httpbin.org",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
            "Connection": "keep-alive",
        }

    def verificar(self):

        if not self.url or len(self.url) < 2:
            print("É preciso selecionar uma URL...")
            print()
            print("--"*5, "DOC", "--"*5)
            print(__doc__)
            print()
            return False

        print("Consultando URL..")
        return True

class WebScrapper(main):
    def __init__(self):
        super().__init__()
        if not self.verificar():
            return

        print()
        print("--"*5, "RESOLUÇÃO DNS", "--"*5)
        print()

        self.r = requests

        if "//" in self.url:
            self.url_extensão = self.url.split("//")[1].split("/")[0]
        else:
            self.url_extensão = self.url.split("/")[0]

        sub = subprocess.run(
            ["nslookup", self.url_extensão],
            capture_output=True,
            text=True
        )

        print(f"Resolução de DNS: {sub.stdout}")

        self.coleção = {}

        try:

            print()
            print("--"*5, "HEADLES", "--"*5)
            print()

            self.nav = self.navegadores[self.driver]()
            self.nav.get(self.url)

            site = BeautifulSoup(self.nav.page_source, 'html.parser')
            organizado = site.prettify()

            self.coleção["HTML"] = organizado

            print(organizado)

            self.desc = [
                requests.get(
                    url=self.url,
                    headers=self.headers,
                    timeout=10,
                    allow_redirects=True,
                    verify=True
                ),
                requests.head(
                    url=self.url,
                    headers=self.headers,
                    timeout=10,
                    allow_redirects=False,
                    verify=True
                )
            ]

            count = 0

            for self.r in self.desc:
                count += 1

                print()
                print("--"*5, f"REQUESIÇÕES #{count}", "--"*5)
                print()

                time.sleep(random.randint(1, 7))

                if self.r.status_code == 200:
                    site = BeautifulSoup(self.r.text, 'html.parser')
                    organizado = site.prettify()
                    self.coleção["HTML"] = organizado
                    site.find('title')
                    print(site)

                    try:
                        print(
                            f"Certo, mais informações: {self.r.json()}, {self.r.status_code}, {self.r.text}, {self.r.encoding}."
                        )
                    except ValueError:
                        print(
                            f"Certo, mais informações: {self.r.status_code}, {self.r.text}, {self.r.encoding}."
                        )

                    print(f"Dados brutos: {self.r.history}")
                    print(f"Corpo da requisição: {self.r._content}, Tamanho: {self.r.headers}")

                elif self.r.status_code == 401:
                    site = BeautifulSoup(self.r.text, 'html.parser').prettify()
                    print(site)

                    try:
                        print(
                            f"Status_code: {self.r.status_code}, JSON: {self.r.json()}. Falta de autenticação."
                        )
                    except ValueError:
                        print(
                            f"Status_code: {self.r.status_code}. Falta de autenticação."
                        )

                    print(f"Dados brutos: {self.r.history}")
                    print(f"Corpo da requisição: {self.r._content}, Tamanho: {self.r.headers}")

                elif self.r.status_code == 403:
                    site = BeautifulSoup(self.r.text, 'html.parser').prettify()
                    print(site)

                    try:
                        print(
                            f"Status_code: {self.r.status_code}, JSON: {self.r.json()}. Sem permissão."
                        )
                    except ValueError:
                        print(
                            f"Status_code: {self.r.status_code}. Sem permissão."
                        )

                    print(f"Dados brutos: {self.r.history}")

                else:
                    print(f"Erro, Status_code: {self.r.status_code}")
                    print(f"Corpo da requisição: {self.r._content}, Tamanho: {self.r.headers}")
                    site = BeautifulSoup(self.r.text, 'html.parser').prettify()
                    site.find('title')
                    print(site)

                if count >= 19:
                    print(f"Limite de REQUESIÇÕES atingido! {count}..")
                    break

        except ConnectionError as e:
            print(f"Possivel erro (DNS ou Solicitação recusada): {e}")
        except ValueError as e:
            print(f"Erro: {e}")
        except AttributeError as e:
            print(f"Erro: {e}")
        else:
            print("Requisições enviadas...")
        finally:
            self.arquivamento()

    def arquivamento(self):
        if not self.coleção:
            print("Nenhum dado para salvar.")
            return

        print()
        print("--"*5, "ARQUIVAMENTO...", "--"*5)
        print()

        for item in self.coleção.values():
            try:
                if json.loads(item):  
                    return "JSON"

                with open("Coleção.json", "w", encoding="utf-8") as arquivo:
                    json.dump(self.coleção.get("HTML"), arquivo, indent=4, ensure_ascii=False)

            except TypeError as e:
                print(f"Erro: {e}")
            except json.decoder.JSONDecodeError as e:
                print(f"Erro JSON: {e}")

        for item in self.coleção.values():
            try:
                if ET.fromstring(item):
                    return "XML"

                with open("Coleção.json", "a", encoding="utf-8") as arquivo:
                    arquivo.write(ET.tostring(self.coleção.get("HTML"), encoding='unicode'))

            except ET.ParseError as e:
                print(f"Erro XML: {e}")

    def coletores(self):
        _ = self.verificar()


if __name__ == "__main__":
    scraper = WebScrapper()