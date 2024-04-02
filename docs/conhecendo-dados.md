# Conhecendo os dados

Nesta seção, você deverá registrar uma detalhada análise descritiva e exploratória sobre a base de dados selecionada na Etapa 1 com o objetivo de compreender a estrutura dos dados, detectar eventuais _outliers_ e também, avaliar/detectar as relações existentes entre as variáveis analisadas.

Para isso, sugere-se que você utilize cálculos de medidas de tendência central, como média, mediana e moda, para entender a centralidade dos dados; explorem medidas de dispersão como desvio padrão e intervalos interquartil para avaliar a variabilidade dos dados; utilizem gráficos descritivos como histogramas e box plots, para representar visualmente as características essenciais dos dados, pois essas visualizações podem facilitar a identificação de padrões e anomalias; analisem a relação aparente entre as variáveis por meio de análise de correlação ou gráficos de dispersões, entre outras técnicas. 

Inclua nesta seção, gráficos, tabelas e demais artefatos que você considere relevantes para entender os dados com os quais você irá trabalhar. 

Primeiramente, trazemos as informações do tamanho do dataset e os tipos de seus atributos antes de qualquer transformação:

# Tabela de dados

| Coluna           | Contagem não nula | Tipo de dados |
|------------------|-----------------:|-----------------|
| id                |             5110 | int64            |
| gender            |             5110 | object           |
| age               |             5110 | float64          |
| hypertension      |             5110 | int64            |
| heart_disease     |             5110 | int64            |
| ever_married      |             5110 | object           |
| work_type         |             5110 | object           |
| Residence_type    |             5110 | object           |
| avg_glucose_level |             5110 | float64          |
| bmi               |             4909 | float64          |
| smoking_status    |             5110 | object           |
| stroke            |             5110 | int64            |



 Além disso, podemos observar os dados analíticos dos atributos numéricos do dataset:


| Statistic           | id              | age             | hypertension  | heart_disease | avg_glucose_level | bmi            | stroke          |
|--------------------|------------------|-----------------|----------------|----------------|-------------------|-----------------|-----------------|
| count               | 5110.000000     | 5110.000000     | 5110.000000    | 5110.000000    | 5110.000000     | 4909.000000     | 5110.000000     |
| mean                | 36517.829354     | 43.226614       | 0.097456       | 0.054012       | 106.147677     | 28.893237       | 0.048728       |
| std                 | 21161.721625     | 22.612647       | 0.296607       | 0.226063       | 45.283560     | 7.854067       | 0.215320       |
| min                 | 67.000000       | 0.080000        | 0.000000       | 0.000000       | 55.120000     | 10.300000       | 0.000000       |
| 25th percentile     | 17741.250000     | 25.000000       | 0.000000       | 0.000000       | 77.245000     | 23.500000       | 0.000000       |
| 50th percentile     | 36932.000000     | 45.000000       | 0.000000       | 0.000000       | 91.885000     | 28.100000       | 0.000000       |
| 75th percentile     | 54682.000000     | 61.000000       | 0.000000       | 0.000000       | 114.090000     | 33.100000       | 0.000000       |
| max                 | 72940.000000     | 82.000000       | 1.000000       | 1.000000       | 271.740000     | 97.600000       | 1.000000       |

A partir dessas primeiras análises, podemos notar alguns pontos interessantes. Por exemplo:

![image](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-saude/blob/main/docs/img/Grafico_imc.png)


Para começarmos a nos aprofundar nos dados, demonstramos a relação entre os atributos através do mapa de calor:

![image](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-saude/blob/main/docs/img/Mapa_calor.png)

É possível observar que um dos atributos com maior relação com o atributo binário "stroke" é a idade. Existe alguma relação entre idade e incidência de AVC?

![image](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-saude/blob/main/docs/img/Grafico_correlacao_idade.png)

Sobre os atributos não-binários, vamos observar sua distribuição e correlação com incidência de AVC:

Tagaismo: Como estão distribuídas as categorias de histórico de tabagismo no dataset? Quantas incidências de AVC tem cada categoria?

![image](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-saude/blob/main/docs/img/Grafico_correlacao_smoke.png)

Vínculo empregatício: Como estão distribuídas as categorias de vínculo empregatício no dataset? Quantas incidências de AVC tem cada categoria?

![image](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-saude/blob/main/docs/img/Grafico_correlacao_work.png)

Histórico de estado civil: Como estão distribuídas as categorias de estado civil no dataset? Quantas incidências de AVC tem cada categoria?

![image](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-saude/blob/main/docs/img/Grafico_correlacao_married.png)

Sexo: Como estão distribuídas as categorias de sexo no dataset? Quantas incidências de AVC tem cada categoria?

![image](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-saude/blob/main/docs/img/Grafico_correlacao_gender.png)

Além disso, podemos explorar a correlação entre alguns atributos contínuos. Algumas delas são exploradas em mais detalhes nos gráficos abaixo:

![image](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-saude/blob/main/docs/img/Grafico_correlacao_v2.png)

Nos aprofundando um pouco, podemos avaliar a distribuição de certos atributos. Os atributos em questão estão balanceados?

![image](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-saude/blob/main/docs/img/Grafico_distribuicao_v2.png)

Pode-se observar a partir da distribuição que o atributo binário "stroke" parece desbalanceado, o que é confirmado a partir de uma análise em cima do próprio

![image](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-saude/assets/70342051/b7426daf-8412-4328-91c1-5286f373b6f5)



## Descrição dos achados

A partir da análise descrita e exploratória realizada, descreva todos os achados considerados relevantes para o contexto em que o trabalho se insere. Por exemplo: com relação à centralidade dos dados algo chamou a sua atenção? foi possível identificar correlação entre os atributos?

### Mapa de calor:

Com os dados do mapa de calor conseguimos constatar que não existem atributos que exercem um impacto forte no indicie de AVC. Contudo, por um lado alguns atributos como hipertensão, idade, nível médio de glicose e histórico de doenças cardíacas são indicies que não podem ser ignorados. Por outro lado, o atributo de tipo de residência não aparenta ter nenhuma correlação com a o indicie de AVC. 

### Valores nulos:

Pode se observar que o atributo IMC possui 201 entradas nulas no dataset. Qual será a melhor forma de se lidar com isso para treinar o modelo?

### Valores médios possívelmente discrepantes:

Dos valores médios observados na descrição do dataset, há um destaque para o IMC médio. No dataset, o IMC médio é de aproximadamente 28.9. Segundo a OMS, o IMC de um adulto saudável é entre 19 e 25, porém é notado que existe uma variância entre diferentes culturas, gêneros e outros fatores.

### Atributos mais relacionados a incidencia de AVC:

Nota-se que, no conjunto de dados trabalhado, os atributos que demonstram uma maior correlação com o atributo binário "stroke" são os atributos relacionados a saúde da pessoa, como nível médio de glicose, hipertensão e histórico de doenças cardíacas, além de idade.

### Porcentagem de pessoas com AVC:

<b>1. Desequilíbrio de Classes:</b>

Maioria dos pacientes (95,1%) não teve AVC.
Ocorrência de AVC é minoritária (4,9%).

<b>2. Correlações:</b>

Correlação positiva entre idade e AVC (risco aumenta com a idade).
Correlações com outros atributos (hipertensão, doença cardíaca, tabagismo) devem ser exploradas.

<b>3. Centralidade dos Dados:</b>

Atributos com maior influência no risco de AVC São:
Fatores Demográficos: Idade e sexo.
Fatores de Saúde: Hipertensão, doença cardíaca, diabetes, tabagismo.

<b>4. Observações:</b>

Dataset é apenas um exemplo e pode não ser representativo da população geral.

## Ferramentas utilizadas

Existem muitas ferramentas diferentes que podem ser utilizadas para fazer a análise dos dados. Nesta seção, descreva as ferramentas/tecnologias utilizadas e sua aplicação.

A linguagem de programação escolhida para desenvolvimento do código foi o Python (https://www.python.org/doc/)
A IDE de desenvolvimento escolhida foi o IntelliJ (https://www.jetbrains.com/pt-br/idea/)
As bibliotecas escolhidas para análise do dataset e criação de gráficos foram as seguintes:

pandas 
matplotlib 
scikit-learn 
seaborn 
numpy 
