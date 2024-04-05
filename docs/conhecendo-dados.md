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

É evidente que a idade é um dos atributos mais significantemente associados ao risco de AVC, conforme indicado pela análise do atributo binário "stroke". Existe uma correlação substancial entre idade e incidência de AVC.

Observa-se que o AVC é menos comum em pessoas com menos de 55 anos, porém, após essa faixa etária, o risco aumenta consideravelmente. Estudos mostram que após os 55 anos, as chances de AVC duplicam (MARIANELLI Mariana, MARIANELLI Camila, NETO Tobias. Principais fatores de risco do AVC isquêmico: Uma abordagem descritiva).

Além disso, abaixo dos 85 anos, os homens têm maior propensão a serem afetados pelo AVC. No entanto, acima dos 85 anos, as mulheres têm uma incidência maior, o que pode ser atribuído à maior expectativa de vida feminina (JAMES et al., 2014).

Fatores de risco como diabetes, tabagismo, hipertensão, alto colesterol e obesidade, bem como a falta de atividade física, desempenham um papel crucial no desenvolvimento do AVC.

Entre os fatores de risco modificáveis, destaca-se a hipertensão arterial sistêmica como o mais comum, seguido pela fibrilação atrial, diabetes mellitus, dislipidemia, obesidade e tabagismo, que pode até dobrar o risco de AVC (apud MARIANELLI, 2020).

![image](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-saude/blob/main/docs/img/Grafico_correlacao_idade.png)

Sobre os atributos não-binários, vamos observar sua distribuição e correlação com incidência de AVC:

Tabagismo: Como estão distribuídas as categorias de histórico de tabagismo no dataset? Quantas incidências de AVC tem cada categoria?
atraves da analise do dataset em questao, podemos avaliar que o tabagismo não tem grande influencia no avc, porém nosso dataset encontra um grande numero de pessoas que estao categorizadas como "desconhecidas, ou seja não responderam se fuma ou nao, talves por se tratr de crianças. entao pode ter havido influencia no resultado ja que estudos dizem que o tabagismo influencia  no avc.
No entanto "Segundo Rodrigues (2021) em seu estudo 'Previsão de traçado por meio de algoritmos de Ciência de Dados e Machine Learning', os valores desconhecidos relacionados ao tabagismo em indivíduos com menos de 18 anos foram ajustados para 'nunca', resultando na redução de incógnitas de 1.544 para 909, que posteriormente foram removidas do conjunto de dados."

![image](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-saude/blob/main/docs/img/Grafico_correlacao_smoke.png)

Vínculo empregatício: Como estão distribuídas as categorias de vínculo empregatício no dataset? Quantas incidências de AVC tem cada categoria?

Percebe-se, a partir da análise do conjunto de dados selecionado, que as categorias mais prevalentes são aquelas relacionadas a pessoas empregadas em empresas privadas. Em contraste, as categorias de crianças e trabalhadores por conta própria estão significativamente abaixo da média, representando menos de 50% do total. Essa disparidade nos dados é evidente. Por exemplo, há um grande número de entrevistados que são empregados em empresas privadas em comparação com aqueles que trabalham por conta própria, sendo que menos da metade pertence a essa última categoria. No entanto, é difícil determinar se o tipo de emprego tem influência no risco de AVC, uma vez que não temos dados suficientes para avaliar isso com precisão. Seria necessário entrevistar um número significativamente maior de pessoas em cada categoria para estabelecer uma correlação confiável entre o tipo de vínculo empregatício e a incidência de AVC.


Mas Segundo Rodrigues (2021) em seu estudo 'Previsão de traçado por meio de algoritmos de Ciência de Dados e Machine Learning', outra reclassificação foi feita ao alterar todos os valores de 'filho' para 'nunca trabalhou', visto que crianças não deveriam ser consideradas como um tipo de trabalho, o que pode implicar em valores de 'nunca trabalharam'.

![image](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-saude/blob/main/docs/img/Grafico_correlacao_work.png)

Histórico de estado civil: Como estão distribuídas as categorias de estado civil no dataset? Quantas incidências de AVC tem cada categoria?

![image](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-saude/blob/main/docs/img/Grafico_correlacao_married.png)

Sexo: Como estão distribuídas as categorias de sexo no dataset? Quantas incidências de AVC tem cada categoria?
Abaixo de 85 anos de idade o sexo masculino é o mais acometido. Já em idades acima de 85 anos, o sexo feminino é o mais acometido já que as mulheres apresentam maior expectativa de vida. Em idades abaixo de 85 anos o sexo masculino é o mais acometido. (JAMES et al., 2014). 

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

Segundo a Organização mundial de saúde, a entrofia, o indivíduo considerado saudável deve ter o IMC entre 18,5 a 24,99.
Dos valores médios observados na descrição do dataset, há um destaque para o IMC médio. No dataset, o IMC médio é de aproximadamente 28.9. Segundo a OMS, o IMC de um adulto saudável é entre 18,5 e 24,99, porém é notado que existe uma variância entre diferentes culturas, gêneros e outros fatores. Acima deste valor pode ser considerado um individuo, com sobrepeso, gordo ou obeso (NIEMAN, 1990)

![image](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-saude/assets/81451748/d26183ee-5002-402d-8f75-65f83a295952)

### Atributos mais relacionados a incidencia de AVC:

Nota-se que, no conjunto de dados trabalhado, os atributos que demonstram uma maior correlação com o atributo binário "stroke" são os atributos relacionados a saúde da pessoa, como nível médio de glicose, hipertensão e histórico de doenças cardíacas, além de idade.

### Porcentagem de pessoas com AVC:

<b>1. Desequilíbrio de Classes:</b>

Maioria dos pacientes (95,1%) não teve AVC.
Ocorrência de AVC é minoritária (4,9%).

<b>2. Correlações:</b>

Correlação positiva entre idade e AVC (risco aumenta com a idade).
Correlações com outros atributos (hipertensão, doença cardíaca, tabagismo) devem ser exploradas sendo assim, temos:

<b>2.1. Idade:</b>

Correlação positiva forte: risco de AVC aumenta com a idade.
Explicação:
Envelhecimento causa rigidez arterial, aterosclerose e declínio da função cardiovascular.
Maior probabilidade de acúmulo de fatores de risco (hipertensão, diabetes).

<b>2.2. Hipertensão:</b>

Correlação positiva forte: hipertensão aumenta significativamente o risco de AVC.
Explicação:
Pressão alta danifica os vasos sanguíneos, tornando-os mais propensos a rupturas e coágulos.
A hipertensão não controlada é um dos principais fatores de risco para AVC.

<b>2.3. Doença cardíaca:</b>

Correlação positiva forte: doenças cardíacas aumentam o risco de AVC.
Explicação:
Doenças cardíacas como arritmia, infarto e insuficiência cardíaca podem levar à formação de coágulos sanguíneos que podem causar AVC.
A doença cardíaca também pode danificar os vasos sanguíneos, tornando-os mais propensos a rupturas.

<b>2.4. Tabagismo: </b>

Correlação positiva forte: tabagismo aumenta significativamente o risco de AVC.
Explicação:
O cigarro danifica os vasos sanguíneos e aumenta a coagulação do sangue.
Tabagismo aumenta o risco de aterosclerose e outras doenças cardiovasculares.


<b>2.5.0 Outros Fatores de Risco: </b>
<b></b>
2.5.1. Diabetes:

Aumento do risco de AVC, especialmente em diabéticos tipo 2.
<b></b>
2.5.2. Colesterol alto:

Aumento do risco de aterosclerose e coágulos sanguíneos.
<b></b>
2.5.3. Obesidade:

Aumento do risco de hipertensão, diabetes e outras doenças cardiovasculares.
<b></b>
2.5.4. Sedentarismo:

Aumento do risco de doenças cardiovasculares e diabetes.
<b></b>
2.5.5. Dieta:

Dieta rica em gorduras saturadas e trans, colesterol e sódio aumenta o risco de AVC.
<b></b>
2.5.6. Consumo excessivo de álcool:

Aumento do risco de hipertensão e doenças cardíacas.


<b>2.6. Considerações Adicionais: </b>

A força da correlação não indica causalidade.
O risco individual de AVC depende de uma combinação de fatores.
Modificar os fatores de risco pode reduzir significativamente o risco de AVC.

<b>3. Centralidade dos Dados:</b>

Os dados do changeset fornecem informações valiosas sobre os fatores de risco para AVC. A análise desses dados pode ajudar a:

<b>3.0.1. Identificar os principais fatores de risco:</b>

Idade, sexo, hipertensão, doença cardíaca, diabetes e tabagismo são os principais fatores de risco para AVC.
Compreender a relação entre esses fatores e o risco de AVC.

<b>3.0.2. Desenvolver estratégias de prevenção:</b>

Modificar os fatores de risco pode reduzir significativamente o risco de AVC.
Criar programas de prevenção direcionados a grupos de alto risco.

<b>3.0.3. Melhorar o tratamento e o prognóstico:</b>

A análise de dados pode ajudar a identificar pacientes com maior risco de complicações.
Otimizar o tratamento e melhorar o prognóstico dos pacientes com AVC.

<b>3.1.0. Fatores Demográficos:</b>


<b>3.1.1. Idade:</b>

A idade é o principal fator de risco para AVC.
O risco de AVC aumenta significativamente com a idade.

<b>3.1.2. Sexo:</b>

Homens têm um risco ligeiramente maior de AVC do que mulheres.
As mulheres têm um risco maior de AVC após a menopausa.

<b>3.2.0. Fatores de Saúde:</b>


<b>3.2.1. Hipertensão:</b>

A hipertensão é um dos principais fatores de risco para AVC.
A pressão alta danifica os vasos sanguíneos, aumentando o risco de rupturas e coágulos.

<b>3.2.2. Doença cardíaca:</b>

Doenças cardíacas aumentam o risco de AVC.
A doença cardíaca pode levar à formação de coágulos sanguíneos que podem causar AVC.

<b>3.2.3. Diabetes:</b>

O diabetes aumenta o risco de AVC, especialmente em diabéticos tipo 2.
O diabetes danifica os vasos sanguíneos e aumenta o risco de coágulos sanguíneos.

<b>3.2.4. Tabagismo:</b>

O tabagismo é um importante fator de risco para AVC.
O cigarro danifica os vasos sanguíneos e aumenta a coagulação do sangue.

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


ORGANIZAÇÃO MUNDIAL DA SAÚDE. Obesity: preventing and managing the global epidemic. Geneva, 1998. p. 276.

SILVA, M. V. B. M. PARÂMETROS ANTROPOMÉTRICOS E DE SAÚDE DOS OFICIAIS DO CENTRO DE INSTRUÇÃO E ADAPTAÇÃO DA AERONÁUTICA - CIAAR (BASE AÉREA DE BELO HORIZONTE). Revista Brasileira de Atividade Física & Saúde. Universidade Federal de Minas Gerais, V8, 2003, p 41-48. 

MARIANELLI Mariana, MARIANELLI Camila, NETO Tobias. Principais fatores de risco do avc isquêmico: Uma abordagem descritiva. Vol.3, 2020. https://ojs.brazilianjournals.com.br/ojs/index.php/BJHR/article/view/22269


JAMES, Paul A. et al. 2014 evidence-based guideline for the management of high blood pressure in adults: report from the panel members appointed to the Eighth Joint National Committee (JNC 8). JAMA, v. 311, n. 5, p. 507-520, 5 fev. 2014. doi: 10.1001/jama.2013.284427.
