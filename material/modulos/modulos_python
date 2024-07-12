## S09 - Lidando com arquivos, pacotes e módulos

**OBS: Sempre acompanhar as partes do código com prática síncrona**
**OBS: Lembrar de: oferecer um dicionário para alunas com eventuais traduções importantes no contexto da aula. Elas já devem usar e conhecer o google translate, mas enfatizar que o seu uso pode ajudar no entendimento da lógica da aula.**

---
---

#### Criando um ambiente virtual
&nbsp;
Em Python, um ambiente virtual é um diretório que contém um interpretador Python específico e as bibliotecas a ele associadas. Ambientes virtuais permitem que um usuário possua múltiplo ambientes Python na mesma máquina (computador), cada uma com seus diferentes módulos e dependências.Isso significa que esse ambientes permitem a criação e uso de ambientes Python distintos e isolados de modo que se possa gerenciar o uso de pacotes durante o desenvolvimento de projetos, melhor atendendo aos requisitos de cada sistema.
&nbsp;

Vantagens do uso de ambientes virtuais:
    - estabilidade
    - reproducibilidade
    - gestão de dependências
&nbsp;

Existem diversas formas de se criar um ambiente virtual, porém usaremos o módulo venv, que está disponível na biblioteca padrão do Python.
&nbsp;

Criar um ambiente virtual com o módulo venv:   
``` bash
python3 -m venv <myvenv>
``` 
Ativar ambiente virtual criado:
``` bash
source myenv/bin/activate
```
Desativar ambiente virtual criado:
``` bash
deactivate
```    

--- 

#### Dependências

Dependências acontecem quando o software principal depende de outras bibliotecas de software para o seu funcionamento. 
Essa é uma prática comum - e necessária - no desenvolvimento, porém requer manutenção e cuidado para não acarretar maiores problemas, que podem ocorrer de diferentes formas, como: a necessidade de bibliotecas complementares, longas cadeiras de instalação, programas conflitantes, dependências circulares, dependências desatualizadas, etc.
&nbsp;

[https://www.alura.com.br/artigos/o-que-e-inferno-de-dependencias-como-utilizar-dependabot](https://www.alura.com.br/artigos/o-que-e-inferno-de-dependencias-como-utilizar-dependabot)
[https://www.treinaweb.com.br/blog/o-que-e-gerenciador-de-dependencias](https://www.treinaweb.com.br/blog/o-que-e-gerenciador-de-dependencias)

---

#### Pacotes e módulos (`dir`)

O que são módulos em Python?
A linguagem Python tem uma maneira de colocar as definições em um arquivo e então usá-las em um script ou em uma execução interativa do interpretador. Tal arquivo é chamado de módulo; definições de um módulo podem ser importadas para outros módulos, ou para o módulo principal.
Um módulo permite que o código seja organizado de forma lógica, realizando agrupamentos de códigos relacionados e facilitando a compreensão do código.
&nbsp;

Pacotes x Módulos:
Um pacote (biblioteca) é basicamente um tipo de módulo que contém um conjunto de módulos. Enquanto um módulo é armazenado em um arquivo simples (com a extensão de nome de arquivo `.py`), um pacote é um diretório contendo vários módulos e um arquivo `__init__`.
&nbsp;

![Módulos](/S09/conteudo_e_codigo/images/modulos.png)

[Pip Documentation](https://pip.pypa.io/en/stable/)
[Python docs: Módulos](https://docs.python.org/pt-br/3/tutorial/modules.html)
[Python - Modules](https://www.tutorialspoint.com/python/python_modules.htm#:~:text=A%20module%20is%20a%20Python,can%20also%20include%20runnable%20code.)
 
---

#### Pacotes públicos PyPi
    
O Python Package Index - PyPI - é o repositório de software oficial de terceiros para a linguagem Python. 
Isso significa que é uma plataforma onde desenvolvedores podem publicar e distribuir seus pacotes Python, tornando-os de fácil acesso para a comunidade Python.
[Pypi](https://pypi.org/)
&nbsp;

---

#### Instalando pacotes com o Pip

Criar um novo arquivo .py na raiz do repositório da semana e colar o código abaixo e tentar rodar 
***(NOTA: a professora e alunas não podem ter o pacote Pandas instalado -> o objetivo aqui é criar um erro de importação para começar a elucidar os assuntos da semana).***
    
Input:
```Python
series_object = pandas.Series([1, 3, 5, 12, 6, 8])
```

Output:
```bash
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
NameError: name 'pandas' is not defined
```
 
Gerenciadores de pacotes são coleções de ferramentas de software que auxiliam na automação no processo de instalação, configuração e remoção de programas/pacotes/libs/frameworks de forma consistente.

[Fonte: o-que-e-gerenciador-de-dependencias](https://www.treinaweb.com.br/blog/o-que-e-gerenciador-de-dependencias)
[Fonte: O que é um gerenciador de pacotes](https://horadecodar.com.br/o-que-e-um-gerenciador-de-pacote/)

Pip é um sistema de gestão de pacotes escrito em Python que é utilizado para instalação e manejo de software. É a ferramenta recomendada pela Python Software Foundation para instalação de aplicações Python e suas dependências e um dos gerenciadores mais utilizados no dia a dia por desenvolvedores Python.

[Pip](https://pypi.org/project/pip/)
[Pip Documentation](https://pip.pypa.io/en/stable/)

No terminal, checar versão com alunas para demonstrar que elas já possuem instalado
    
``` bash
pip --version
```

Instalar o pacote Pandas

```bash
pip install pandas
```
    
Repetir o processo anterior, agora com o pacote instalado. Gancho para o próximo tópico: o que são pacotes e módulos em Python
        
Input
```Python
    import pandas             
    
    series_object = pandas.Series([1, 3, 5, 12, 6, 8])  
```

Output:
```bash
series_object
0     1
1     3
2     5
3    12
4     6
5     8
dtype: int64
```

---

#### Desinstalando pacotes

Pacotes podem ser desinstalados de um ambiente virtual usando pip:

```bash
pip uninstall <packagename>
```
&nbsp;

---

#### Importando pacotes e importando funções específicas

Destacar as vantagens deimportar funções específicas e não o pacote inteiro?
https://stackoverflow.com/a/710603

Demonstrar com o pacote math, importando função sqrt:
    
```Python
from math import sqrt

num = 4
print(sqrt(num))
```

---

#### Gerenciando pacotes no ambiente virtual (requirements.txt) 
- install
- uninstall
- freeze

Existem diferentes maneiras de se efetuar o gerenciamento de dependências em um projeto. Existem ferramentas completamente destinadas a isso, mas o arquivo de dependências é uma das formas mais simples de abordar o assunto. O arquivo requirements.txt é um arquivo de texto que lista todas as dependências necessárias ao funcionamento de um projeto.
&nbsp;

Exemplo:
```txt
numpy
pandas
datetime
```
&nbsp;

É possível instalar todas as dependências listadas nesse arquivo utilizando :
```bash
pip install -r requirements.txt
```
&nbsp;


Após instaladas, as dependências podem ser conferidas usando o comando freeze via pip:
```bash
pip freeze
````
&nbsp;

Output:
```bash
DateTime==5.1
numpy==1.24.3
pandas==2.0.1
python-dateutil==2.8.2
pytz==2023.3
six==1.16.0
tzdata==2023.3
zope.interface==6.0
```
&nbsp;

---

