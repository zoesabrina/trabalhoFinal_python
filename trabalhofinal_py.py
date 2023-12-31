# -*- coding: utf-8 -*-
"""trabalhoFinal_py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xlb65x7v-eVCgsgN6Lgk8mmrptb60agJ?usp=sharing
"""

import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

df = pd.read_csv('CADASTRO_IES_2020.CSV', encoding='latin1', delimiter=';', error_bad_lines=False)
print(df.head())

print(df.info())

print("Analise exploratoria:")
print("Total de linhas: ", len(df))
print("Resumo estatistico:\n", df.describe())
print("\n")

print("Análise exploratória:")
print("Total de linhas: ", len(df))
print("\nResumo estatístico por região:")
regiao_stats = df.groupby('NO_REGIAO_IES').describe()
print(regiao_stats)

# Gráfico instituições p/ região
contagem_regioes = df['NO_REGIAO_IES'].value_counts()
plt.figure(figsize=(10, 6))
plt.bar(contagem_regioes.index, contagem_regioes.values, color=['skyblue', 'orange', 'purple', 'fireBrick', 'green'])
plt.xlabel('Região')
plt.ylabel('Quantidade de Instituições')
plt.title('Distribuição de Instituições por Região')
plt.savefig('distribuicao_regiao.png')
plt.show()

print("Análise exploratória por raça/cor:")
print("Total de linhas: ", len(df))
print("\nResumo estatístico das colunas de raça/cor:")
raca_stats = df[['DOC_EX_BRANCA', 'DOC_EX_PRETA', 'DOC_EX_PARDA', 'DOC_EX_AMARELA', 'DOC_EX_INDÍGENA']].describe()
print(raca_stats)

# Gráfico raça/cor
racas = ['DOC_EX_BRANCA', 'DOC_EX_PRETA', 'DOC_EX_PARDA', 'DOC_EX_AMARELA', 'DOC_EX_INDÍGENA']
raca_labels = ['Branca', 'Preta', 'Parda', 'Amarela', 'Indígena']
quantidade_racas = df[racas].sum()
plt.figure(figsize=(10, 6))
plt.bar(raca_labels, quantidade_racas, color='salmon')
plt.xlabel('Raça/Cor')
plt.ylabel('Quantidade de Docentes')
plt.title('Distribuição de Raça/Cor dos Docentes')
plt.savefig('distribuicao_raca_cor.png')
plt.show()

print("Análise exploratória por gênero:")
print("Total de linhas: ", len(df))
print("\nResumo estatístico das colunas de gênero:")
genero_stats = df[['DOC_EX_FEMI', 'DOC_EX_MASC']].describe()
print(genero_stats)

# Gráfico docentes p/ gênero
generos = ['DOC_EX_FEMI', 'DOC_EX_MASC']
genero_labels = ['Feminino', 'Masculino']
quantidade_docentes = df[generos].sum()
plt.figure(figsize=(10, 6))
plt.pie(quantidade_docentes, labels=genero_labels, colors=['cyan', 'gold'], autopct='%1.1f%%',  labeldistance=0.7)
plt.axis('equal')
plt.title('Quantidade de Docentes por Gênero')
plt.savefig('quantidade_docentes_genero.png')
plt.show()

### Começa PDF Aqui ####
class PDF(FPDF):
    def chapter_title(self, title):
        self.set_left_margin(20)
        self.set_right_margin(20)
        self.set_font('Arial', 'B', 15)
        self.ln(15)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(5)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 6, body)
        self.ln()

    def add_image(self, image_path):
        self.image(image_path, x=10, y=None, w=180)

pdf = PDF()
pdf.add_page()

# pdf- Gráfico instituições p/ região
pdf.chapter_title('Distribuição de Instituições por Região')
pdf.chapter_body('A análise da distribuição das instituições de ensino superior por região nos traz uma perspectiva interessante. Ao observar o gráfico, é notável que a maioria das faculdades e universidades se concentra na região Sudeste do Brasil. Isso se deve, em grande parte, ao fato de que as primeiras universidades e instituições de ensino superior do país surgiram nessa área. Essas instituições pioneiras desempenharam um papel fundamental no desenvolvimento educacional nas regiões Sul e Sudeste, contribuindo para a construção de uma sólida base educacional nessas localidades.')
pdf.add_image('distribuicao_regiao.png')

pdf.add_page()

# pdf- Gráfico raça/cor 
pdf.chapter_title('Distribuição de Raça/Cor dos Docentes')
pdf.chapter_body('O gráfico exibe a distribuição de docentes com diferentes origens étnicas, abrangendo as categorias de Branca, Preta, Parda, Amarela e Indígena. Ao longo de grande parte da história do país, as oportunidades educacionais foram historicamente limitadas para grupos étnicos minoritários, como indígenas e afrodescendentes. Isso resultou em um número significativamente menor de indivíduos dessas origens buscando carreiras no ensino superior e, consequentemente, contribuindo como professores. É notável e, ao mesmo tempo, um lembrete da necessidade contínua de promover a diversidade e inclusão no ensino superior, com a esperança de que, com o tempo, possamos reverter essas disparidades.')
pdf.add_image('distribuicao_raca_cor.png')

pdf.add_page()

# pdf- Gráfico docentes p/ gênero
pdf.chapter_title('Quantidade de Docentes por Gênero')
pdf.chapter_body('Olhando para a quantidade de professores nas universidades e faculdades, percebe-se algo interessante sobre a igualdade de gênero na educação. No passado, as oportunidades de educação para as mulheres eram limitadas, o que levava a menos mulheres escolhendo carreiras acadêmicas e de ensino. No entanto, hoje em dia, estamos vendo uma mudança gradual. As mulheres estão cada vez mais ocupando posições nas instituições de ensino superior, o que é um sinal positivo de progresso em direção à igualdade de gênero. Isso mostra que as mulheres estão conquistando seu espaço na educação superior e contribuindo de forma significativa.')
pdf.add_image('quantidade_docentes_genero.png')

pdf.output('relatorio_analise.pdf')