import streamlit as st
import pandas as pd
import numpy as np
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report  # Wrapper for Streamlit

# Import additional libraries as needed

# Title and Project Introduction
st.title("Income Prediction Project")

st.markdown("""
### 4 Key Elements of This Project
- This notebook (project code)
- Streamlit for interactive analysis
- GitHub repository with the project
- Video in GitHub readme showing Streamlit application
""")

# Business Understanding
st.markdown("""
## Step 1 - CRISP-DM: Business Understanding

In the context of income prediction, understanding the business scenario is essential, particularly how data can add value.
Income prediction is critical for financial institutions, insurance companies, and marketing firms, as it aids in customizing offerings and making credit-related decisions.

**Objective:** This project aims to predict clients' income based on demographic and economic characteristics (age, education, asset ownership, marital status, etc.). Enhancing the accuracy of income predictions supports strategic decision-making, like credit offerings and personalized marketing actions.
""")

# Data Dictionary
st.markdown("""
## Data Dictionary

The table below describes the key features of the dataset used for income prediction.

| Variable                | Description                             | Type        |
|-------------------------|-----------------------------------------|-------------|
| **data_ref**            | Reference date of data collection       | Date        |
| **id_cliente**          | Unique client identifier                | Numeric     |
| **sexo**                | Client gender (Male/Female)             | Categorical |
| **posse_de_veiculo**    | Vehicle ownership (Yes/No)              | Binary      |
| **posse_de_imovel**     | Property ownership (Yes/No)             | Binary      |
| **qtd_filhos**          | Number of children                      | Numeric     |
| **tipo_renda**          | Primary income source (e.g., Employed, Self-employed) | Categorical |
| **educacao**            | Education level (e.g., High School, College) | Categorical |
| **estado_civil**        | Marital status (e.g., Single, Married)  | Categorical |
| **tipo_residencia**     | Type of residence (e.g., Owned, Rented) | Categorical |
| **idade**               | Client age                              | Numeric     |
| **tempo_emprego**       | Years of employment                     | Numeric     |
| **qt_pessoas_residencia** | Number of people in residence        | Numeric     |
| **renda**               | Monthly income                          | Numeric     |
""")

import streamlit as st

# Title of the section
st.title("Bibliotecas Utilizadas")

# Description of libraries used
st.markdown("""
- **Pandas**: Utilizado para manipulação de dados tabulares (DataFrames), como filtragem, agregação e transformação de dados.
- **Seaborn**: Biblioteca para criação de gráficos estatísticos, que facilita a visualização de padrões e tendências.
- **Matplotlib**: Ferramenta de visualização de dados, muito útil para criar gráficos simples ou complexos.
- **Pandas Profiling**: Gera relatórios automáticos de análise exploratória de dados, ajudando a entender rapidamente as principais características do dataset.
""")




# Optional: Display a profiling report if needed
st.write("### Relatório de Análise Exploratória")

import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# Title and explanation
st.title("Carregando os dados")

# Explanation of pd.read_csv
st.markdown("""
O comando `pd.read_csv` é um comando da biblioteca **Pandas** (`pd.`) e carrega os dados do arquivo CSV indicado para um objeto *DataFrame* do Pandas.
""")

# Code example in Markdown (properly closed)
st.markdown("""
```python
from ydata_profiling import ProfileReport

renda = pd.read_csv('previsao_de_renda.csv')
renda.head(5)
""")

import streamlit as st
import pandas as pd

# Load the data
renda = pd.read_csv('previsao_de_renda.csv')

# Display a sample of the data
st.write("### Exemplo de Dados Carregados")
st.dataframe(renda.head())


import streamlit as st

# Title
st.title("Análise de Renda")

# Opening the HTML file with the full path and loading its content
file_path = "/Users/samwalford/Downloads/original (7)/output/analise.html"
with open(file_path, "r") as file:
    html_content = file.read()

# Display the HTML content in Streamlit
st.components.v1.html(html_content, height=800, scrolling=True)

import streamlit as st

# Title
st.title("Análise de Renda")

# Markdown content
st.markdown("""
A análise de renda foi realizada a partir de um dataset contendo informações de **15.000 observações** e **15 variáveis**. 
O relatório gerado utiliza técnicas exploratórias e estatísticas, permitindo a visualização detalhada das características dos dados, 
como a distribuição de variáveis **numéricas**, **categóricas** e **booleanas**.

A seguir, apresento as principais descobertas e insights obtidos com base nessa análise.
""")
import streamlit as st

# Title for the section
st.header("Etapa 2 Crisp-DM: Preparação dos dados")

# Description with bullet points
st.markdown("""
Nessa etapa realizamos tipicamente as seguintes operações com os dados:

- **seleção**: Já temos os dados selecionados adequadamente?
- **limpeza**: Precisaremos identificar e tratar dados faltantes
- **construção**: construção de novas variáveis
- **integração**: Temos apenas uma fonte de dados, não é necessário integração
- **formatação**: Os dados já se encontram em formatos úteis?
""")

import streamlit as st
import pandas as pd
import io

# Carregar os dados
df = pd.read_csv('previsao_de_renda.csv')

# Verificar a estrutura dos dados
st.write("### Estrutura dos Dados")
buffer = io.StringIO()
df.info(buf=buffer)
s = buffer.getvalue()
st.text(s)

# Verificar as primeiras linhas
st.write("### Primeiras Linhas dos Dados")
st.dataframe(df.head())

import streamlit as st

# Add descriptive text
st.markdown("""
Nesta análise, estamos trabalhando com um dataset que contém informações de **15.000 clientes**, incluindo variáveis como **sexo, posse de veículo e imóvel, número de filhos, tipo de renda, educação, estado civil, idade, tempo de emprego, número de pessoas na residência e renda**. 

Uma característica importante desta base de dados é a presença de algumas variáveis fortemente correlacionadas com a renda, como o **tempo de emprego** e a **quantidade de pessoas na residência**, que serão exploradas para entender o impacto no rendimento anual dos clientes. Vale destacar que a variável **tempo de emprego** possui alguns valores nulos, o que pode ser um fator a considerar na modelagem final.
""")

import streamlit as st
import pandas as pd

# Carregar os dados
df = pd.read_csv('previsao_de_renda.csv')

# Verificar os valores nulos em todas as colunas
st.write("### Valores Nulos em Cada Coluna")
st.write(df.isnull().sum())

# Selecionar apenas as colunas numéricas para tratar os valores nulos com a mediana
colunas_numericas = df.select_dtypes(include=['float64', 'int64']).columns

# Preencher os valores nulos com a mediana apenas nas colunas numéricas
df[colunas_numericas] = df[colunas_numericas].fillna(df[colunas_numericas].median())

# Verificar dados duplicados
st.write("### Número de Linhas Duplicadas")
st.write(f"Número de linhas duplicadas: {df.duplicated().sum()}")

# Remover linhas duplicadas, se houver
df.drop_duplicates(inplace=True)

# Verificar a limpeza dos dados
st.write("### Estrutura dos Dados Após a Limpeza")
buffer = io.StringIO()
df.info(buf=buffer)
s = buffer.getvalue()
st.text(s)
import streamlit as st

# Add descriptive text about the data analysis and cleaning process
st.markdown("""
Durante o processo de análise e limpeza dos dados, foi verificado que a base contém **15.000 entradas** e **15 variáveis**. 

Importante destacar que **não foram encontradas linhas duplicadas**, garantindo a integridade dos dados. No entanto, a variável **tempo de emprego** possui **2.573 valores ausentes**, o que poderá impactar a modelagem se não for tratada adequadamente. Todas as outras variáveis estão completas, sem valores nulos, o que proporciona uma base sólida para a análise e modelagem preditiva. 

Esta etapa de análise de qualidade de dados é fundamental para garantir que os resultados sejam confiáveis e robustos.
""")
import streamlit as st
import pandas as pd

# Carregar os dados
df = pd.read_csv('previsao_de_renda.csv')

# Preencher valores nulos de 'tempo_emprego' com a mediana
df['tempo_emprego'].fillna(df['tempo_emprego'].median(), inplace=True)

# Verificar novamente se há valores nulos
st.write("### Valores Nulos Após o Preenchimento")
st.write(df.isnull().sum())

# Explicação da etapa de preparação dos dados
st.markdown("""
Para essa etapa do processo de preparação de dados, foquei em lidar com valores ausentes, especificamente na variável **tempo de emprego**, 
que apresentava um número significativo de valores nulos. Esses valores ausentes poderiam prejudicar a qualidade das análises e da modelagem preditiva, 
então optei por preenchê-los com a **mediana** dessa variável. A escolha da mediana é estratégica, pois ela reduz o impacto de valores extremos que poderiam distorcer a análise.

Após o preenchimento, verifiquei novamente se ainda há valores nulos em todas as variáveis. Como mostra a saída, todas as colunas estão agora completas, 
sem valores ausentes, o que nos garante uma base de dados sólida e pronta para as próximas etapas da análise e modelagem.
""")


import streamlit as st
import pandas as pd

# Carregar os dados
df = pd.read_csv('previsao_de_renda.csv')

# Verificar tipos de dados
st.write("### Tipos de Dados Antes da Conversão")
st.write(df.dtypes)

# Se necessário, ajustar tipos de dados
# Exemplo: Converter coluna 'data_ref' para formato de data
df['data_ref'] = pd.to_datetime(df['data_ref'])

# Verificar se todas as colunas estão no formato correto
st.write("### Tipos de Dados Após a Conversão")
st.write(df.dtypes)
import streamlit as st
import pandas as pd

# Carregar os dados
df = pd.read_csv('previsao_de_renda.csv')

# Verificar tipos de dados antes da conversão
st.write("### Tipos de Dados Antes da Conversão")
st.write(df.dtypes)

# Ajustar tipos de dados, convertendo 'data_ref' para formato de data
df['data_ref'] = pd.to_datetime(df['data_ref'])

# Verificar tipos de dados após a conversão
st.write("### Tipos de Dados Após a Conversão")
st.write(df.dtypes)

# Explicação da conversão e importância dos tipos de dados
st.markdown("""
Durante a análise dos dados, foi necessário ajustar alguns tipos de variáveis para melhorar o tratamento da informação. 
Inicialmente, a variável **data_ref** estava no formato `object`, o que não permitia uma manipulação eficiente das datas. 
Após a conversão para o formato `datetime`, conseguimos explorar melhor o comportamento temporal dos dados.

As outras variáveis mantiveram seus tipos apropriados, como variáveis numéricas (`int64` e `float64`) e categóricas (`object`), 
além das variáveis booleanas (`bool`) para **posse_de_veiculo** e **posse_de_imovel**. 

Essas alterações foram essenciais para garantir uma análise mais robusta e precisa.
""")
import streamlit as st

# Display the Markdown text in Streamlit
st.markdown("# Construção de Novas Variáveis")
st.write(
    """
    Fiz a construção de novas variáveis, pois pode melhorar a performance de modelos preditivos 
    e fornecer insights mais profundos.
    """
)
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Criar a variável 'faixa_etaria' usando intervalos de idade
df['faixa_etaria'] = pd.cut(df['idade'], bins=[0, 18, 30, 45, 60, 100], labels=['0-18', '19-30', '31-45', '46-60', '61+'])

# Contar a quantidade de pessoas em cada faixa etária
faixa_etaria_counts = df['faixa_etaria'].value_counts().sort_index()

# Exibir um gráfico de barras da distribuição de faixa etária
st.subheader("Distribuição de Faixa Etária")
fig, ax = plt.subplots()
faixa_etaria_counts.plot(kind='bar', ax=ax)
ax.set_xlabel("Faixa Etária")
ax.set_ylabel("Quantidade")
ax.set_title("Distribuição de Faixa Etária entre os Participantes")
st.pyplot(fig)
st.write("""
### Análise da Distribuição de Faixa Etária

O gráfico acima mostra a distribuição dos participantes em diferentes faixas etárias. Observamos que a maioria dos indivíduos se concentra nas faixas de **31-45 anos** e **46-60 anos**, sugerindo que uma grande parte da população analisada está em idade produtiva. As faixas **0-18 anos** e **61+ anos** representam uma menor proporção dos dados, indicando que as extremidades etárias são menos representadas neste conjunto. Essa distribuição pode ter implicações para a análise de renda e de perfil demográfico da população.
""")

import streamlit as st
import pandas as pd

# Exemplo de dados
data = {
    'renda': [50000, 70000, 55000, 48000, 60000],
    'tempo_emprego': [5, 10, 0, 8, 12]
}
df = pd.DataFrame(data)

# Criar uma nova variável que capture a relação entre renda e tempo de emprego
df['renda_por_ano_emprego'] = df['renda'] / df['tempo_emprego'].replace(0, 1)

# Título do aplicativo
st.title("Análise de Renda por Tempo de Emprego")

# Mostrar tabela de dados com a nova variável
st.write("Tabela de Dados com Renda, Tempo de Emprego e Renda por Ano de Emprego:")
st.dataframe(df[['renda', 'tempo_emprego', 'renda_por_ano_emprego']])
import streamlit as st


st.write(
    """
    A variável **renda por ano emprego** foi criada para avaliar a eficiência salarial de cada indivíduo, ou seja, 
    quanto de renda a pessoa gera para cada ano de trabalho. Essa métrica permite uma comparação mais justa entre 
    pessoas com diferentes tempos de emprego, facilitando a análise de como o tempo de trabalho impacta a renda.

    O resultado desta variável nos mostra, por exemplo, que pessoas com menor tempo de emprego podem ter uma renda maior por ano trabalhado, 
    enquanto aqueles com mais tempo de emprego tendem a ter uma distribuição de renda mais estável ou até menos expressiva. 
    Isso pode indicar que o tempo de emprego não é o único fator determinante da renda, e outros aspectos, como o tipo de emprego ou setor, 
    também devem ser considerados.
    """
)

import streamlit as st
import pandas as pd

# Exemplo de dados para simulação
data = {
    'qt_pessoas_residencia': [4, 3, 5, 2, 6],
    'posse_de_imovel': [1, 0, 1, 1, 0]  # 1 = possui imóvel, 0 = não possui imóvel
}
df = pd.DataFrame(data)

# Criar uma nova variável 'pessoas_por_imovel'
df['pessoas_por_imovel'] = df['qt_pessoas_residencia'] / (df['posse_de_imovel'].astype(int) + 1)

import streamlit as st
import pandas as pd

# Exemplo de dados para simulação
data = {
    'qt_pessoas_residencia': [4, 3, 5, 2, 6],
    'posse_de_imovel': [1, 0, 1, 1, 0]  # 1 = possui imóvel, 0 = não possui imóvel
}
df = pd.DataFrame(data)

# Criar uma nova variável 'pessoas_por_imovel'
df['pessoas_por_imovel'] = df['qt_pessoas_residencia'] / (df['posse_de_imovel'].astype(int) + 1)

# Título e descrição
st.markdown("## Cálculo da variável 'pessoas_por_imovel'")
st.write(
    """
    A variável **pessoas_por_imovel** foi criada para calcular a média de pessoas por imóvel,
    considerando se o indivíduo possui ou não um imóvel. O cálculo divide o número de pessoas 
    na residência pelo indicador de posse de imóvel (com +1 para evitar divisão por zero).
    """
)

# Exibir o DataFrame no Streamlit
st.write(df[['qt_pessoas_residencia', 'posse_de_imovel', 'pessoas_por_imovel']].head())
import streamlit as st

# Display the text in Streamlit
st.markdown(
    """
    A variável **pessoas por imovel** foi criada para calcular a quantidade média de pessoas por imóvel, 
    dividindo o número de pessoas na residência pela posse do imóvel (quando o valor é "True"). 
    Se a pessoa não possui um imóvel, o valor permanece igual ao número de pessoas na residência.

    Essa variável ajuda a entender melhor a densidade de ocupação dos imóveis entre as pessoas que 
    possuem e não possuem um imóvel. No exemplo exibido, quando a posse do imóvel é "True", 
    a variável mostra a média exata de pessoas no imóvel, e quando é "False", o valor é ajustado. 
    Isso pode ser útil para avaliar se existe uma relação entre posse de imóvel e o número de pessoas por 
    residência, o que pode fornecer insights sobre hábitos de moradia ou condições socioeconômicas.
    """
)
import streamlit as st

# Display the title for the section
st.subheader("Criar variáveis dummies para as colunas categóricas")

import streamlit as st
import pandas as pd

# Sample data (replace with your actual data)
data = {
    'sexo': ['M', 'F', 'M', 'F', 'M'],
    'tipo_renda': ['Empregado', 'Desempregado', 'Autônomo', 'Empregado', 'Estudante'],
    'educacao': ['Ensino Médio', 'Ensino Superior', 'Ensino Médio', 'Ensino Fundamental', 'Ensino Superior'],
    'estado_civil': ['Solteiro', 'Casado', 'Divorciado', 'Solteiro', 'Viúvo']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create dummy variables
df_dummies = pd.get_dummies(df, columns=['sexo', 'tipo_renda', 'educacao', 'estado_civil'], drop_first=True)

# Display the first few rows of the dummy DataFrame in Streamlit
st.write("DataFrame with Dummy Variables:")
st.dataframe(df_dummies.head())
import streamlit as st

# Display the explanatory text
st.write("""
A criação de variáveis dummies é essencial para transformar variáveis categóricas em binárias, tornando-as utilizáveis por modelos de machine learning que requerem dados numéricos. 

Por exemplo, variáveis como "tipo de renda" e "educação" foram convertidas em novas colunas binárias (0 ou 1), capturando categorias específicas de forma compatível com os algoritmos. Isso preserva as informações categóricas, permitindo que os modelos compreendam as relações entre essas categorias e variáveis como "renda", sem erros de interpretação ordinal.
""")

import streamlit as st
import pandas as pd

# Example data (replace this with your actual data)
data = {
    'renda': [1500, 3000, 7000, 12000, 50000]
}
df = pd.DataFrame(data)

# Categorize income into groups
df['grupo_renda'] = pd.cut(df['renda'], bins=[0, 2000, 5000, 10000, 25000, 100000], labels=['Muito Baixa', 'Baixa', 'Média', 'Alta', 'Muito Alta'])

# Display the first rows in Streamlit
st.write("### Categorias de Renda")
st.write(df[['renda', 'grupo_renda']].head())
import streamlit as st

# Display the explanation text
st.write("""


A categorização da variável **renda** em grupos foi realizada para facilitar a análise e interpretação dos dados. Ao dividir a renda em faixas (Muito Baixa, Baixa, Média, Alta), conseguimos identificar padrões e comportamentos relacionados aos diferentes níveis de renda. Essa abordagem é útil, por exemplo, para analisar a distribuição de características sociodemográficas ou outros fatores com base nos diferentes grupos de renda.

No exemplo acima, vemos que indivíduos com renda em torno de 8.060 estão classificados no grupo "Média", enquanto aqueles com renda abaixo de 2.000 estão no grupo "Muito Baixa". Essa categorização simplifica a análise e permite uma visão mais clara da distribuição de renda entre os participantes.
""")
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data for demonstration
import pandas as pd
data = {
    'idade': [25, 30, 35, 40, 45, 50, 55, 60],
    'renda': [2000, 3000, 5000, 7000, 6000, 8000, 8500, 9000]
}
df = pd.DataFrame(data)
import streamlit as st

st.header("Entendimento dos dados - Bivariadas")


# Plotting the relationship between age and income
st.write("## Relação entre Idade e Renda")

plt.figure(figsize=(6, 4))
sns.scatterplot(x='idade', y='renda', data=df)
plt.title('Relação entre Idade e Renda')
plt.xlabel('Idade')
plt.ylabel('Renda')

# Display the plot in Streamlit
st.pyplot(plt)
import streamlit as st

st.write("""
A imagem acima apresenta um gráfico de dispersão que explora a relação entre **idade** e **renda**. 
Observa-se que, apesar de a maioria das rendas mais altas estarem concentradas em indivíduos entre 30 e 50 anos, a dispersão de pontos não revela uma correlação muito clara entre essas variáveis. 

À medida que a idade aumenta, há uma leve tendência de aumento de renda até cerca de 50 anos, após o qual as rendas tendem a se estabilizar ou diminuir. Isso sugere que, embora a idade possa influenciar a renda, outros fatores podem ter um impacto mais significativo no comportamento da renda dentro do conjunto de dados analisado.
""")
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Sample DataFrame creation (remove if you already have df)
import pandas as pd
df = pd.DataFrame({
    'tempo_emprego': [1, 3, 5, 7, 10],
    'renda': [3000, 5000, 7000, 8000, 12000]
})

# Plotting the relationship between employment duration and income
st.header("Relação entre Tempo de Emprego e Renda")

# Creating the plot
plt.figure(figsize=(8, 4))
sns.scatterplot(x='tempo_emprego', y='renda', data=df)
plt.title('Relação entre Tempo de Emprego e Renda')
plt.xlabel('Tempo de Emprego (Anos)')
plt.ylabel('Renda')

# Displaying the plot in Streamlit
st.pyplot(plt)
import streamlit as st

# Displaying the descriptive text about the plot
st.markdown("""
O gráfico de dispersão acima mostra a relação entre o **tempo de emprego** (em anos) e a **renda dos indivíduos**. Podemos observar que, embora haja uma leve tendência de aumento da renda conforme o tempo de emprego aumenta, não há uma correlação muito forte entre as variáveis. As rendas mais altas estão concentradas entre os indivíduos com até 20 anos de tempo de emprego. Após esse ponto, a renda tende a estabilizar, indicando que o tempo de emprego por si só pode não ser um fator determinante na obtenção de rendas mais altas, sugerindo a influência de outros fatores.
""")
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Assuming you have your DataFrame df already loaded
# Example data for demonstration purposes
data = {
    'Gênero': ['Masculino', 'Feminino', 'Masculino', 'Feminino', 'Masculino'],
    'renda': [2000, 3000, 1500, 4000, 2500]
}
df = pd.DataFrame(data)

# Plotting boxplot to see the distribution of income by Gênero
st.markdown("### Distribuição de Renda por Gênero")
fig, ax = plt.subplots(figsize=(6, 4))
sns.boxplot(x='Gênero', y='renda', data=df, ax=ax)
ax.set_title('Distribuição de Renda por Gênero')
ax.set_xlabel('Gênero')
ax.set_ylabel('Renda')

# Display the plot in Streamlit
st.pyplot(fig)
st.write("#### Análise da Distribuição de Renda por Gênero")
st.write("""
O gráfico de boxplot acima representa a distribuição da renda entre gêneros. Observa-se que a mediana da renda 
varia entre Masculino e Feminino, com o grupo Feminino apresentando uma mediana de renda ligeiramente superior. 
A dispersão dos dados também sugere uma variação nas rendas dentro de cada grupo, destacando uma amplitude maior 
de rendas para o gênero Feminino. Essa análise é útil para entender diferenças de renda entre gêneros e identificar 
possíveis desigualdades econômicas.
""")

import streamlit as st
import pandas as pd

# Load your DataFrame
df = pd.read_csv('previsao_de_renda.csv')  # Make sure this file is in the same directory or provide the full path

# Check if the 'posse_de_veiculo' column exists and display unique values
if 'posse_de_veiculo' in df.columns:
    st.write("Column 'posse_de_veiculo' exists.")
    st.write("Unique values in 'posse_de_veiculo':", df['posse_de_veiculo'].unique())
else:
    st.write("Column 'posse_de_veiculo' does not exist in the DataFrame.")

# Now, you can retry the boxplot if the column is verified
if 'posse_de_veiculo' in df.columns:
    import matplotlib.pyplot as plt
    import seaborn as sns

    # Plotting the boxplot
    st.write("### Distribuição de Renda por Posse de Veículo")
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.boxplot(x='posse_de_veiculo', y='renda', data=df, ax=ax)
    ax.set_title('Distribuição de Renda por Posse de Veículo')
    ax.set_xlabel('Posse de Veículo')
    ax.set_ylabel('Renda')

    # Display the plot
    st.pyplot(fig)
import streamlit as st

# Explanation of the boxplot in storytelling format
st.markdown("""


O gráfico acima explora a relação entre a posse de veículo e a distribuição de renda dos indivíduos. 
Observei que a posse de um veículo pode estar associada a uma faixa de renda mais alta em comparação 
àqueles que não possuem veículo. Essa análise pode nos ajudar a entender possíveis padrões de consumo, 
uma vez que pessoas com maior renda tendem a ter maior acesso a bens de alto valor, como veículos. 

Esse insight pode ser útil para estratégias de segmentação e para compreender o impacto econômico da 
posse de bens na vida dos participantes do estudo.
""")
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your data (replace with your actual CSV file path)
df = pd.read_csv('previsao_de_renda.csv')

# Calculate the mean income by marital status
media_renda_por_estado_civil = df.groupby('estado_civil')['renda'].mean()

# Display the mean income by marital status in Streamlit
st.write("### Média de Renda por Estado Civil")
st.write(media_renda_por_estado_civil)

# Plot a boxplot to visualize the distribution of income by marital status
st.write("### Distribuição de Renda por Estado Civil")
fig, ax = plt.subplots(figsize=(8, 4))
sns.boxplot(x='estado_civil', y='renda', data=df, ax=ax)
ax.set_title('Distribuição de Renda por Estado Civil')
ax.set_xlabel('Estado Civil')
ax.set_ylabel('Renda')
plt.xticks(rotation=45)
st.pyplot(fig)
st.write("### Distribuição de Renda por Estado Civil")
st.write(
    """
    Observa-se que pessoas no estado civil "Casado" apresentam uma maior variabilidade de renda,
    com valores máximos bem acima dos outros grupos. Essa dispersão sugere que dentro do grupo
    de casados, há uma distribuição de renda mais heterogênea. Em contraste, grupos como "Solteiro"
    e "Viúvo" possuem rendas mais concentradas e com menor dispersão.

    A análise desses dados pode indicar que o estado civil "Casado" abrange uma maior diversidade 
    econômica, possivelmente devido a fatores como renda familiar compartilhada ou diferentes 
    fases de vida econômica.
    """
)
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Selecionar apenas as colunas numéricas
df_numerico = df.select_dtypes(include=['float64', 'int64'])

# Displaying the heatmap for correlations between numerical variables
st.write("### Mapa de Correlação entre Variáveis Numéricas")
fig, ax = plt.subplots(figsize=(8, 4))
sns.heatmap(df_numerico.corr(), annot=True, cmap='coolwarm', linewidths=0.5, ax=ax)
st.pyplot(fig)

# Calcular e exibir a média de renda por estado civil
st.write("### Média de Renda por Estado Civil")
media_renda_estado_civil = df.groupby('estado_civil')['renda'].mean().reset_index()
st.dataframe(media_renda_estado_civil)
import streamlit as st

st.subheader("Mapa de Correlação entre Variáveis Numéricas")
st.write("O mapa de correlação entre as variáveis numéricas apresenta a relação entre diferentes características. Observamos que algumas variáveis possuem correlações mais fortes, como a quantidade de filhos com a quantidade de pessoas na residência. Esse tipo de análise ajuda a identificar quais variáveis possuem relação e pode indicar quais delas são mais relevantes para análises preditivas.")

st.subheader("Média de Renda por Estado Civil")
st.write("A tabela de média de renda por estado civil revela uma diferença interessante nos níveis de renda conforme o estado civil dos indivíduos. Pessoas casadas apresentam uma média de renda superior, enquanto pessoas viúvas têm a menor média de renda. Essas informações podem ser úteis para entender o impacto do estado civil na renda e possíveis fatores econômicos relacionados.")

st.write("""
### Conclusão
#### Rodando o Modelo

**Seleção das Variáveis:**
As variáveis selecionadas para prever a renda são o **tempo de emprego**, a **quantidade de pessoas na residência**, a **renda por ano de emprego** e o **número de pessoas por imóvel**. Essas variáveis foram escolhidas por apresentarem correlação com a renda, sugerindo que influenciam diretamente na variação do rendimento.

**Treinamento e Teste:**
Os dados foram divididos em dois conjuntos: **70% dos dados foram usados para treinar o modelo** e os **30% restantes foram reservados para testar e avaliar o desempenho do modelo**. Isso garante que o modelo seja avaliado com base em dados que ele ainda não viu, permitindo uma avaliação mais confiável.

**Modelo de Regressão Linear:**
Utilizamos a técnica de **regressão linear**, implementada pela função `LinearRegression()` da biblioteca **Scikit-learn**, para modelar a relação entre as variáveis preditoras e a variável alvo (renda). A regressão linear é adequada para esse problema, pois estamos lidando com uma variável contínua.

**Avaliação do Modelo:**
Duas métricas principais foram usadas para avaliar o desempenho do modelo:

- **MSE (Erro Médio Quadrático):** Essa métrica mede o erro médio ao quadrado entre os valores reais e os valores preditos, indicando o quão precisas foram as previsões do modelo.
- **R² (Coeficiente de Determinação):** Essa métrica avalia a proporção da variação da renda que é explicada pelo modelo, fornecendo uma ideia da qualidade geral do ajuste do modelo aos dados.

Essas métricas nos ajudam a entender o quão bem o modelo está performando e se as variáveis selecionadas estão explicando adequadamente as variações na renda.
""")

import streamlit as st
from sklearn.model_selection import train_test_split

# Display header
st.write("### Divisão do Dataset em Treino e Teste")

# Selecionar as variáveis independentes (features) e a dependente (target)
X = df[['idade', 'tempo_emprego', 'qtd_filhos']]  # Ajuste conforme as variáveis que deseja usar
y = df['renda']

# Dividir o dataset em treino e teste (80% treino e 20% teste)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Display information about the split
st.write("**Variáveis Selecionadas:**")
st.write(X.columns.tolist())

st.write("**Tamanho do Conjunto de Treinamento:**", len(X_train))
st.write("**Tamanho do Conjunto de Teste:**", len(X_test))

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Carregar o DataFrame
# df = pd.read_csv('previsao_de_renda.csv')  # Substitua pelo caminho correto

# Criar as novas variáveis 'renda_por_ano_emprego' e 'pessoas_por_imovel'
df['renda_por_ano_emprego'] = df['renda'] / df['tempo_emprego'].replace(0, 1)
df['pessoas_por_imovel'] = df['qt_pessoas_residencia'] / (df['posse_de_imovel'].astype(int) + 1)

# Remover linhas com valores ausentes nas colunas selecionadas
df = df[['tempo_emprego', 'qt_pessoas_residencia', 'renda_por_ano_emprego', 'pessoas_por_imovel', 'renda']].dropna()

# Selecionar as variáveis independentes (features) e a variável dependente (target)
X = df[['tempo_emprego', 'qt_pessoas_residencia', 'renda_por_ano_emprego', 'pessoas_por_imovel']]
y = df['renda']

# Dividir os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Criar o modelo de Regressão Linear
modelo = LinearRegression()

# Treinar o modelo com os dados de treino
modelo.fit(X_train, y_train)

# Fazer previsões com os dados de teste
y_pred = modelo.predict(X_test)

# Avaliar o modelo usando métricas de desempenho
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Exibir os resultados da avaliação
st.subheader("Avaliação do Modelo")
st.write(f"MSE (Erro Médio Quadrático): {mse:.2f}")
st.write(f"R² (Coeficiente de Determinação): {r2:.2f}")

# Exibir os coeficientes do modelo
coeficientes = pd.DataFrame(modelo.coef_, X.columns, columns=['Coeficientes'])
st.subheader("Coeficientes do Modelo")
st.write(coeficientes)
st.write("""
### Análise do Desempenho do Modelo de Regressão Linear

O modelo de regressão linear foi treinado com **70% dos dados** e testado com os **30% restantes**, resultando em uma análise de 12.000 registros para treino e 3.000 para teste. A seguir estão as métricas principais de desempenho:

- **Erro Médio Quadrático (MSE)**: O MSE de aproximadamente 47.064.739 indica o erro médio quadrático entre os valores reais e preditos. Valores menores de MSE sugerem melhor precisão, mas neste caso, um valor elevado sugere que o modelo pode ter limitações em capturar todas as variações de renda.

""")
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error, r2_score
import streamlit as st

# Criar o modelo de Lasso com um valor de alpha (o parâmetro de regularização)
lasso_model = Lasso(alpha=1.0)

# Treinar o modelo com os dados de treino
lasso_model.fit(X_train, y_train)

# Prever no conjunto de teste
y_pred_lasso = lasso_model.predict(X_test)

# Avaliar o modelo
mse_lasso = mean_squared_error(y_test, y_pred_lasso)
r2_lasso = r2_score(y_test, y_pred_lasso)

# Exibir os resultados em Streamlit
st.write("### Avaliação do Modelo Lasso")
st.write(f"Lasso - MSE (Erro Médio Quadrático): {mse_lasso:.2f}")
st.write(f"Lasso - R² (Coeficiente de Determinação): {r2_lasso:.2f}")
st.write("### Interpretação dos Resultados do Modelo Lasso")
st.write("""
O modelo Lasso foi avaliado com duas métricas principais:

- **MSE (Erro Médio Quadrático)**: Essa métrica indica a média dos erros ao quadrado entre os valores preditos e os valores reais de renda. Quanto menor o MSE, melhor o modelo. No entanto, ainda temos um erro relativamente alto, o que sugere que há variáveis importantes que talvez não foram consideradas ou que o modelo poderia ser melhorado.
  
- **R² (Coeficiente de Determinação)**: Este valor indica a proporção da variabilidade da renda que é explicada pelo modelo. Um valor de R² de 0.27 indica que o modelo explica aproximadamente 27% da variação na renda, o que é uma performance modesta. Isso sugere que, embora o modelo capture alguns padrões, ele não explica totalmente a renda dos indivíduos.

Esses resultados mostram que o modelo Lasso, com o parâmetro de regularização utilizado, tem um desempenho similar ao modelo de regressão linear, mas ainda possui espaço para aprimoramentos.
""")
st.write("## Explicação do GridSearchCV no Processo de Ajuste de Hiperparâmetros")

st.write("""
Vou utilizar o **GridSearchCV** que é uma técnica utilizada para otimizar os hiperparâmetros de um modelo de machine learning. No caso da regularização **Ridge** e **Lasso**, o hiperparâmetro a ser ajustado é o **alpha**, que controla a intensidade da regularização.

O processo funciona da seguinte forma:

- **GridSearchCV** testa vários valores de *alpha* definidos no parâmetro *param_grid*.
- Ele divide os dados em várias partes utilizando *cross-validation* (neste caso, 5 partes, ou seja, *cv=5*). O modelo é treinado em diferentes combinações de dados e avaliado nas partes restantes.
- A métrica de avaliação usada é o **MSE (Erro Médio Quadrático)**, que mede a diferença média entre os valores preditos e reais. Você também pode utilizar outras métricas, como o **R²**, dependendo do objetivo da análise.

Essa abordagem garante que o modelo seja ajustado de maneira robusta, testando diferentes valores de *alpha* e selecionando o que resulta na melhor performance, minimizando o risco de overfitting ou underfitting.
""")
import streamlit as st
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Ridge

# Definir os parâmetros a serem testados
param_grid_ridge = {'alpha': [0.001, 0.01, 0.1, 1, 10, 100]}

# Criar o modelo Ridge
ridge = Ridge()

# Configurar o GridSearchCV
grid_ridge = GridSearchCV(ridge, param_grid_ridge, cv=5, scoring='neg_mean_squared_error')

# Ajustar o modelo aos dados
grid_ridge.fit(X_train, y_train)

# Exibir o melhor valor de alpha e o melhor MSE
st.write("## Resultados do GridSearchCV para o Modelo Ridge")
st.write(f"Melhor valor de alpha para Ridge: **{grid_ridge.best_params_['alpha']}**")
st.write(f"Melhor MSE (Erro Médio Quadrático) para Ridge: **{-grid_ridge.best_score_:.2f}**")
import streamlit as st

st.subheader("Explicação dos Resultados do GridSearchCV para o Modelo Ridge")

st.write("""
O processo de ajuste de hiperparâmetros com o GridSearchCV encontrou o melhor valor para o parâmetro de regularização `alpha`, que controla a intensidade da regularização no modelo Ridge. 

Neste caso, o melhor valor de `alpha` encontrado foi **100**, o que indica um ajuste que ajuda a evitar overfitting, equilibrando a complexidade do modelo. Além disso, o menor erro médio quadrático (MSE) obtido foi **61615581.55**, refletindo a precisão do modelo na previsão dos dados.

Esses resultados são fundamentais para entender a performance do modelo Ridge após o ajuste de hiperparâmetros, proporcionando um balanço adequado entre viés e variância.
""")
import streamlit as st
from sklearn.linear_model import Lasso
from sklearn.model_selection import GridSearchCV

# Definir os parâmetros a serem testados
param_grid_lasso = {'alpha': [0.001, 0.01, 0.1, 1, 10, 100]}

# Criar o modelo Lasso
lasso = Lasso()

# Configurar o GridSearchCV
grid_lasso = GridSearchCV(lasso, param_grid_lasso, cv=5, scoring='neg_mean_squared_error')

# Ajustar o modelo aos dados
grid_lasso.fit(X_train, y_train)

# Melhor valor de alpha e MSE para o modelo Lasso
best_alpha = grid_lasso.best_params_['alpha']
best_mse = -grid_lasso.best_score_

# Exibir os resultados no Streamlit
st.subheader("Resultados do GridSearchCV para o Modelo Lasso")
st.write(f"Melhor valor de alpha para Lasso: {best_alpha}")
st.write(f"Melhor MSE (Erro Médio Quadrático) para Lasso: {best_mse:.2f}")
st.subheader("Interpretação dos Resultados do GridSearchCV para o Modelo Lasso")
st.write("""
O GridSearchCV foi utilizado para ajustar o parâmetro de regularização `alpha` do modelo Lasso. 
Após testar diferentes valores de `alpha`, o melhor valor encontrado foi 10, indicando o nível ideal de penalização para reduzir o overfitting. 
O menor erro quadrático médio (MSE) obtido foi de aproximadamente 61.612.038,76, o que reflete a precisão do modelo nas previsões de renda.

Esse ajuste é fundamental para melhorar o desempenho do modelo, balanceando a complexidade do modelo e a precisão nas previsões.
""")
st.subheader("Etapa 5 Crisp-DM: Avaliação dos Resultados")
st.write("### Comparação de Modelos: Regressão Linear Simples, Ridge e Lasso")
st.write("""
Os três modelos de regressão — Linear, Ridge e Lasso — foram utilizados para prever a variável **renda** com base em variáveis como **tempo de emprego**, **quantidade de pessoas na residência**, **renda por ano de emprego** e **pessoas por imóvel**. Abaixo estão os principais resultados de cada modelo:
""")

st.write("#### Regressão Linear Simples:")
st.write("- MSE (Erro Médio Quadrático): 45.760.941")
st.write("- R² (Coeficiente de Determinação): 0.3049")

st.write("#### Ridge (com melhor alpha ajustado):")
st.write("- MSE: 45.760.964")
st.write("- R²: 0.3049")

st.write("#### Lasso (com melhor alpha ajustado):")
st.write("- MSE: 45.762.247")
st.write("- R²: 0.3049")

st.subheader("Interpretação dos Resultados")
st.write("""
- **Erro Médio Quadrático (MSE)**: Uma métrica de erro que mede o desvio quadrático médio entre os valores reais e os valores preditos. Quanto menor o valor, melhor o modelo.
- **Coeficiente de Determinação (R²)**: Mede a proporção de variação da renda que pode ser explicada pelo modelo. Um valor de 0.3049 significa que cerca de 30,49% da variação da renda pode ser explicada pelas variáveis do modelo.
""")

st.subheader("Análise")
st.write("""
- Todos os três modelos obtiveram resultados muito semelhantes, com diferenças mínimas no MSE e no R². Isso indica que as técnicas de regularização (Ridge e Lasso) não adicionaram grandes melhorias no ajuste dos dados.
- O modelo **Ridge** foi ligeiramente melhor em termos de MSE, sugerindo que a regularização Ridge pode ter um leve benefício em comparação com o Lasso, mas a diferença é insignificante.
""")

st.subheader("Conclusão")
st.write("""
Dado que os três modelos performaram de maneira bastante similar, tanto o Ridge quanto o Lasso poderiam ser considerados boas escolhas. No entanto, a regularização Ridge mostrou um resultado marginalmente melhor em termos de MSE. Ainda assim, a **Regressão Linear Simples** continua sendo uma opção viável, uma vez que não há uma melhoria significativa nos modelos regularizados.
""")
st.subheader("Avaliação dos Resultados de Regularização com Ridge e Lasso")
st.write("""
Após a aplicação do **GridSearchCV** para ajustar o hiperparâmetro **alpha** dos modelos **Ridge** e **Lasso**, obtivemos os seguintes resultados:

- **Melhor alpha para Ridge**: 100
- **Melhor MSE para Ridge**: 49.762.513,19
- **Melhor alpha para Lasso**: 10
- **Melhor MSE para Lasso**: 49.762.370,84

Os valores de **MSE** (Erro Médio Quadrático) indicam que tanto o modelo **Ridge** quanto o **Lasso** apresentam desempenhos muito semelhantes, com uma diferença mínima entre os dois. O alpha ideal para o modelo Ridge foi 100, enquanto o Lasso encontrou o melhor desempenho com alpha = 10.
""")

st.write("""
Embora ambos os modelos tenham alcançado resultados quase idênticos em termos de erro, o **Lasso** apresentou uma leve vantagem com um MSE ligeiramente menor. No entanto, a escolha entre Ridge e Lasso pode depender da necessidade de regularização mais forte ou da simplificação do modelo, já que o Lasso tende a zerar coeficientes de variáveis menos relevantes, tornando o modelo mais interpretável.
""")

st.write("""
**Conclusão**: O Lasso teve uma performance marginalmente melhor neste caso, o que pode ser útil se o objetivo for um modelo mais simples e interpretável.
""")

import streamlit as st

# Título da Etapa 6: Implantação
st.subheader("Etapa 6 Crisp-DM: Implantação")
st.write("""
Nessa etapa, colocamos em uso o modelo desenvolvido, normalmente implementando o modelo em um motor de decisão que toma ações automaticamente com base nos resultados das previsões. Esse processo pode envolver a integração do modelo em sistemas que processam dados em tempo real ou em lotes, fornecendo previsões para apoiar decisões empresariais automatizadas.
""")

# Simulação de uma interface de predição
st.markdown("### Simulação de Predição de Renda")

# Entrada de dados do usuário para simulação
tempo_emprego = st.number_input("Tempo de Emprego (anos)", min_value=0, value=5)
qt_pessoas_residencia = st.number_input("Quantidade de Pessoas na Residência", min_value=1, value=3)
renda_por_ano_emprego = st.number_input("Renda por Ano de Emprego", min_value=0.0, value=10000.0)
pessoas_por_imovel = st.number_input("Pessoas por Imóvel", min_value=0.0, value=1.5)

# Carregar o modelo e fazer a predição (exemplo, certifique-se de ter o modelo treinado salvo)
# Aqui você carregaria o modelo e faria a predição; este é um exemplo básico.
# modelo = ... (carregar modelo treinado)
# X_novo = [[tempo_emprego, qt_pessoas_residencia, renda_por_ano_emprego, pessoas_por_imovel]]
# renda_prevista = modelo.predict(X_novo)

# Exibir o resultado da previsão
# (Substitua o valor abaixo pela variável `renda_prevista` após implementar o modelo)
renda_prevista = 25000  # Exemplo
st.write(f"### Renda Prevista: R$ {renda_prevista:,.2f}")

st.write("""
Essa interface simula como o modelo poderia ser usado em produção, permitindo que o usuário insira dados e obtenha uma previsão de renda com base no modelo treinado. Em um ambiente real, o modelo seria atualizado periodicamente com novos dados e integrado a um sistema de automação para tomar decisões em tempo real.
""")

