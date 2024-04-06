# Conhecendo os dados

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
No dataset aparece 3353 pessoas casadas e 1757 não casadas. Pessoas que fumam 42 sendo que as que nunca fumaram 90, podendo causar desbalanceamento. Da categoria tipo de trabalho, temos 2925 que trabalham em emrpesa privada, 819 autonomos, 687 filhos, 657 de empresa pública e apensa 22 que nunca trabalharam. Pessoas do sexo masculino 2007 para 2853 feminino.


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

É evidente que a idade é um dos atributos mais significantemente associados ao risco de AVC, conforme indicado pela análise do atributo binário "stroke". Existe uma correlação substancial entre idade e incidência de AVC e essas informaçoes condizem com a realidade de acordo com estudos citados no item "achados".


![image](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-saude/blob/main/docs/img/Grafico_correlacao_idade.png)

Sobre os atributos não-binários, vamos observar sua distribuição e correlação com incidência de AVC:

Tabagismo: 
Como estão distribuídas as categorias de histórico de tabagismo no dataset? Quantas incidências de AVC tem cada categoria?
As cataegorias foram divididas em: nunca fumou (1892), desconhecida (1544), fumou anteriormente (885), fuma (789)
Daqueles que nunca fumaram 90 (4,75%)  tiveram AVC, dos desconhecidos 47 (3%), do que fumaram anteriormente 70 (7,9%), e daqueles que fumam 42 (5,8%) tiveram AVC.

![image](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-saude/blob/main/docs/img/Grafico_correlacao_smoke.png)

Vínculo empregatício: Como estão distribuídas as categorias de vínculo empregatício no dataset? Quantas incidências de AVC tem cada categoria?

As categorias são: filho (687) , trabalho público (657), nunca trabalhou (22), empresa privada (2925), autônomo (819)
2925 pessoas. 
Da categoria filhos, 2 tiveram AVC, o trabalhadores públicos 33, dos que trabalharam em empresa privada 149 e entre os autônomos 65 tiveream AVC.
Se olharmos o percentual dos trabalhadores em empresa pública (5%), privada (5%) e autônomo (8%), Os que mais foram acometidos por AVC foram os autônomos abaixo os de empresa pública e privada, deste dois, ambos se equipararam. O dataset apresenta um número bem maior de trabalhadores de empresa privada, porém o percentual quanto a quantidade de pessoas que tiveram AVC foi dos trabalahdores autônomos.

Percebe-se, a partir da análise do conjunto de dados selecionado, que as categorias mais prevalentes são aquelas relacionadas aos autônomos. Em contraste, as categorias de crianças e que nunca trabalhou, além de uma quantidade pequena de amostra, demonstrando que é em baixo a chance de ter um AVC. Essa disparidade nos dados é evidente. Por exemplo, há um grande número de indivíduo que são empregados em empresas privadas em comparação com aqueles que trabalham por conta própria, sendo que menos da metade pertence a essa última categoria. No entanto, é difícil determinar se o tipo de emprego tem influência no risco de AVC, sendo assim, as correlaçoes observadas nos nossos dados não apontam para uma conclusão precisa, exceto se compararamos apenas cas categorias, privado, publico e autônomo. Seria necessário nova coleta e um número significativamente maior de pessoas em cada categoria para estabelecer uma correlação confiável entre o tipo de vínculo empregatício e a incidência de AVC.




![image](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-saude/blob/main/docs/img/Grafico_correlacao_work.png)

Histórico de estado civil: Como estão distribuídas as categorias de estado civil no dataset? Quantas incidências de AVC tem cada categoria?

No dataset podemos destacar que há influência nas categorias de estado civil pois os casados tiveram mais AVC dos que os solteiros. Isto pode ser devido a idade, se analisarmos o contexto gera,  mas neste gráfico foi analisado apenas as categorias casado e não casado.
As categorias foram divididas em casado (3353) e não casados (1757).
Dos casados  220 (6,5%) tiveram a AVC e entre os solteiros 29 (1,6%). 


![image](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-saude/blob/main/docs/img/Grafico_correlacao_married.png)

Sexo: Como estão distribuídas as categorias de sexo no dataset? Quantas incidências de AVC tem cada categoria?
As categorias são feminino (2994), masculino (2115) e outros (1)
141 (4,7) pessoas do sexo feminino tiveram AVC e 108 (5,1%) dos homens.


![image](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-saude/blob/main/docs/img/Grafico_correlacao_gender.png)

Além disso, podemos explorar a correlação entre alguns atributos contínuos. Algumas delas são exploradas em mais detalhes nos gráficos abaixo: 


![image](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-saude/blob/main/docs/img/Grafico_correlacao_v2.png)

Nos aprofundando um pouco, podemos avaliar a distribuição de certos atributos. Os atributos em questão estão balanceados?
Está bem balanceado os dados do dataset que analisa a idade e visualizamos que a maior concentração está em 70 anos de idade. A maior frequancia de AVC aparce entre 

![image](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-saude/blob/main/docs/img/Grafico_distribuicao_v2.png)

Pode-se observar a partir da distribuição que o atributo binário "stroke" parece desbalanceado, o que é confirmado a partir de uma análise em cima do próprio gráfico.

![image](https://github.com/ICEI-PUC-Minas-PMV-SI/pmv-si-2024-1-pe7-t1-saude/assets/70342051/b7426daf-8412-4328-91c1-5286f373b6f5)



## Descrição dos achados

A partir da análise descrita e exploratória realizada, descreva todos os achados considerados relevantes para o contexto em que o trabalho se insere. Por exemplo: com relação à centralidade dos dados algo chamou a sua atenção? foi possível identificar correlação entre os atributos?
Observa-se que o AVC é menos comum em pessoas com menos de 55 anos, porém, após essa faixa etária, o risco aumenta consideravelmente. Estudos mostram que após os 55 anos, as chances de AVC duplicam (MARIANELLI Mariana, MARIANELLI Camila, NETO Tobias. Principais fatores de risco do AVC isquêmico: Uma abordagem descritiva).

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

Correlação positiva fraca: risco de AVC aumenta com a idade.
Explicação:
Envelhecimento causa rigidez arterial, aterosclerose e declínio da função cardiovascular.
Maior probabilidade de acúmulo de fatores de risco (hipertensão, diabetes). A faixa de idade com maior número de AVC é acima dos 75 anos.

<b>2.2. Hipertensão:</b>

Correlação positiva fraca: hipertensão aumenta significativamente o risco de AVC.
Explicação:
Pressão alta danifica os vasos sanguíneos, tornando-os mais propensos a rupturas e coágulos.
A hipertensão não controlada é um dos principais fatores de risco para AVC.

<b>2.3. Doença cardíaca:</b>

Correlação positiva fraca: doenças cardíacas aumentam o risco de AVC.
Explicação:
Doenças cardíacas como arritmia, infarto e insuficiência cardíaca podem levar à formação de coágulos sanguíneos que podem causar AVC.
A doença cardíaca também pode danificar os vasos sanguíneos, tornando-os mais propensos a rupturas.

<b>2.4. Tabagismo: </b>

Correlação positiva fraca: tabagismo aumenta significativamente o risco de AVC.
Explicação:
O cigarro danifica os vasos sanguíneos e aumenta a coagulação do sangue.
Tabagismo aumenta o risco de aterosclerose e outras doenças cardiovasculares.
Atraves da análise do dataset da saúde, em questao , podemos avaliar que o tabagismo tem muita influência na incidência de AVC; No dataset encontramos um grande número de pessoas que estao categorizadas como "desconhecidas", ou seja não temos informação se fuma ou nao, talves por se tratar de crianças. Então pode ter havido influência no resultado já que estudos afirmam que o tabagismo influencia ao acometimento de AVC. Mas claramente pessoas que fumam ou que fumavam anteriormente tiveram AVC em número superior ao daqueles que nao fumam ou estão na categoria, desconhem.



<b>2.5. Sexo: </b>
As categorias são feminino (2994), masculino (2115) e outros (1)
141 (4,7) pessoas do sexo feminino tiveram AVC e 108 (5,1%) dos homens.
Perecebe-se que a categoria "sexo", neste dataset não mostra diferença suficiente para alergarmos se um ou o outro tem mairo chance de ter AVC visto que a diferença é de apenas 0,4% entre eles.

Abaixo de 85 anos de idade o sexo masculino é o mais acometido. Já em idades acima de 85 anos, o sexo feminino é o mais acometido já que as mulheres apresentam maior expectativa de vida. Em idades abaixo de 85 anos o sexo masculino é o mais acometido. (JAMES et al., 2014). 


<b>2.6. Considerações Adicionais: </b>

A força da correlação não indica causalidade.
O risco individual de AVC depende de uma combinação de fatores.
Modificar os fatores de risco pode reduzir significativamente o risco de AVC.

<b>3. Centralidade dos Dados:</b>

Os dados do dataset fornecem informações valiosas sobre os fatores de risco para AVC. A análise desses dados pode ajudar a:

<b>3.0.1. Identificar os principais fatores de risco:</b>

Idade, hipertensão, doença cardíaca e tabagismo são os principais fatores de risco para AVC.
Compreender a relação entre esses fatores e o risco de AVC.

<b>3.0.2. Desenvolver estratégias de prevenção:</b>

Modificar os fatores de risco pode reduzir significativamente o risco de AVC.
Criar programas de prevenção direcionados a grupos de alto risco.

<b>3.0.3. Melhorar o tratamento e o prognóstico:</b>

A análise de dados pode ajudar a identificar pacientes com maior risco de complicações.
Otimizar o tratamento e melhorar o prognóstico dos pacientes com AVC.

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
