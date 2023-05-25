# Gerador de posts
Gerador de posts baseado em templates e dados armazenados em arquivo csv.

Essa aplicação surgiu da necessidade de gerar textos a partir de um template, cujos dados deveriam ser coletados de um arquivo .csv e .yaml. Então, é isso que esse programa faz: ler dados de um arquivo .csv, outros dados de um arquivo .yaml e preenche um ou mais templates.

## Instalação

```bash
(.venv) $ pip install gerador-posts
```

## Uso

1. Crie os dados:
    1. Crie a pasta `./dados`;
    1. Dentro dessa pasta, crie dois arquivos de dados: `links.csv` e `variaveis.yaml` (os arquivos devem ter exatamente esses títulos).
1. Crie os templates:
    1. Crie a pasta `./posts_templates`;
    1. Dentro dessa pasta você pode criar quantos templates desejar, em qualquer formato de arquivo. (para inserir dados no template use a sintaxe do Jinja2).
1. Crie a pasta aonde os posts prontos serão armazenados: `./posts_prontos`;
1. Execute o pacote:
    ```bash
    (.venv) $ gerador-posts
    ```