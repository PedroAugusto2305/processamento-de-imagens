# Computação Gráfica e Processamento de Imagens

## Processamento Digital de Imagens - Unidade 4, seção 4.1  


## Descrição

Este projeto tem como objetivo, realizar o carregamento de uma imagem e aplicar diferentes filtros gráficos para então observar e analisar as alterações resultantes. Os filtros aplicados foram: **Média**, **Mediana** e **Sobel**. Além disso, também foi proposto experimentar diferentes tamanhos de Kernel para os filtros de média e mediana, avaliando como isso afeta a suavização da imagem. Todos os códigos podem ser conferidos neste mesmo repositório.

### 1. Carregamento de Imagem:

**Imagem Original**

<img src="./image/alan.jpg" alt="descrição da imagem" width="300"/>

### 2. Aplicação dos Filtros:

- **Filtro de Média:** Suaviza a imagem aplicando uma média ponderada, quanto maior a intensidade do filtro, maior é a suavização.
- **Filtro de Mediana:** Suaviza a imagem substituindo cada pixel pela mediana dos pixels vizinhos.
- **Filtro Sobel:** Destaca as bordas na imagem.

### 3. Análise dos Resultados:
- **Filtro de Média:**
  - Suavizou a imagem, reduzindo o ruído.
  - As bordas ficaram menos definidas.
  <img src="./image/filtro-media.png" alt="descrição da imagem" width="1000"/>
- **Filtro de Mediana:**
  - Suavizou a imagem de maneira mais eficaz que o filtro de média.
  - Preservou melhor as bordas em comparação com o filtro de média.
  <img src="./image/filtro-mediana.png" alt="descrição da imagem" width="1000"/>
  
- **Filtro Sobel:**
  - Destacou claramente as bordas na imagem.
  - Utilizado para detecção de contornos e realce de detalhes estruturais.
  <img src="./image/filtro-sobel.png" alt="descrição da imagem" width="1000"/>
  <img src="./image/filtro-sobel-combinado.png" alt="descrição da imagem" width="1000"/>

---

### Tecnologias Utilizadas

- **Linguagem de Programação:** Python 🐍
- **Bibliotecas:**
  - **OpenCV** para processamento de imagens.
  - **NumPy** para manipulação de arrays.
  - **Matplotlib** para vizualização de imagens.

### Instalação

**1. Clone o repositório:**
```bash
git clone https://github.com/PedroAugusto2305/processamento-de-imagens.git
```
**2. Acesse o diretório do projeto:**
```bash
cd processamento-de-imagens
```

**3. Crie um ambiente virtual (opcional, mas recomendado):**
```bash
python -m venv filtros
```

**4. Instale as dependências:**
```bash
pip install -r requirements.txt
```

### Uso

**1. Prepare uma imagem:** escolha uma imagem para testar o uso dos filtros. 

**2. Execute o script:**
```bash
python nome-do-arquivo.py
```
**3. Visualize os resultados:** os resultados poderão ser vistos e comparados com a imagem original.