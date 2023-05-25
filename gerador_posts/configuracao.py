from jinja2 import Environment, FileSystemLoader
import yaml
import os

class Configuracao:
    def __init__(self):
        self.yaml_path = './dados/variaveis.yaml'
        self.templates_pasta = './posts_templates'

    def lerYaml(self):
        ''' 
        Carrega variáveis do yaml
        ''' 
        with open(self.yaml_path, 'r') as arquivo:
            dados = yaml.safe_load(arquivo)
        return dados

    def configurarAmbiente(self):
        '''
        Identifica pasta com templates e estabelece configurações para identação e quebra de linha dos trechos que usa Jinja
        '''
        ambiente = Environment(loader=FileSystemLoader(self.templates_pasta), trim_blocks=True, lstrip_blocks=True)
        return ambiente

    def renderizarTemplate(self, dados, ambiente):
        '''
        Aplica configurações do ambiente em cada template
        '''
        for arquivo in os.listdir(self.templates_pasta):
            template = ambiente.get_template(arquivo)
            with open(f'./posts_prontos/{arquivo}', 'w') as post:
                post.write(template.render(dados, enumerate=enumerate)) # Aplica variáveis do yaml no template e salva o arquivo
