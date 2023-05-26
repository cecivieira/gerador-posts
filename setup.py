from setuptools import setup, find_packages

REPO_URL = 'https://github.com/cecivieira/gerador-posts'

with open('README.md') as descricao:
    long_description = descricao.read()

setup(
    author='Ana Cecília Vieira',
    author_email='cecivieira@gmail.com',
    description='Gerador de posts baseado em templates e arquivos de dados (csv e yaml).',
    zip_safe=False,
    install_requires=[
        'Jinja2==3.1.2',
        'MarkupSafe==2.1.2',
        'PyYAML==6.0'
    ],
    keywords=['jinja2', 'yaml', 'templates'],
    license='MIT',
    long_description_content_type='text/markdown',
    long_description=long_description,
    name='gerador_posts',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'gerar-posts = gerador_posts.gerador_posts:GeradorPosts',
        ],
    },
    url=REPO_URL,
    python_requires='>=3.10.6',
    version='0.1.3',
)