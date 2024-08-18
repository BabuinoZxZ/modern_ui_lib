from setuptools import setup, find_packages

setup(
    name='modern_ui_lib',
    version='0.1',
    packages=find_packages(),  # Inclui todos os pacotes em modern_ui_lib
    install_requires=[
        'tkinter',  # Inclua qualquer outra dependência necessária
    ],
    description='Uma biblioteca para criar interfaces modernas com Tkinter',
    author='Seu Nome',
    author_email='seuemail@example.com',
    url='https://github.com/BabuinoZxZ/modern_ui_lib.git',  # URL do repositório
)
