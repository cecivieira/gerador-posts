from .tratar_dados import TratarDados
from .configuracao import Configuracao

def GeradorPosts():
    dados = TratarDados()
    dicionario = dados.converteCsvEmDicionario()
    atualiza_yaml = dados.insereDicionarioNoYaml(dicionario)

    configuracao = Configuracao()
    dados = configuracao.lerYaml()
    ambiente = configuracao.configurarAmbiente()
    renderizacao = configuracao.renderizarTemplate(dados, ambiente)