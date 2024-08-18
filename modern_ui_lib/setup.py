from setuptools import setup, find_packages

setup(
    name='modern_ui_lib',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'tkinter',  # Inclua tkinter apenas se necessário
    ],
    description='Uma biblioteca para criar interfaces modernas com Tkinter',
    author='Seu Nome',
    author_email='seuemail@example.com',
    url='https://github.com/BabuinoZxZ/modern_ui_lib.git',  # Altere para o URL do seu repositório, se aplicável
)
