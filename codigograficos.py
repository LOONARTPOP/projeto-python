# Importando as bibliotecas matplotlib para construção e visualização de grafico
# e pandas para leitura e manipulação de arquivos.

import matplotlib.pyplot as plt
import pandas as pd

# Estilo do grafico.
plt.style.use('Solarize_Light2')

# Lendo o arquivo CSV.
am = pd.read_csv('tabela.csv',delimiter=';')

# Criando uma figura com 2 subplots.
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14,4))

# Dados do primeiro gráfico,taxa de fecundidade.
ax1.plot(am['ano'],am['fertilidademb'],label='brasil',marker='o')
ax1.plot(am['ano'],am['fertilidademlb'],label='luxemburgo',marker='o')
ax1.plot(am['ano'],am['fertilidademfp'],label='filipinas',marker='o')
ax1.plot(am['ano'],am['fertilidademus'],label='estados unidos',marker='o')
ax1.plot(am['ano'],am['fertilidademm'],label='global',marker='o')

# Definindo limites para os eixos x e y, apenas o eixo x nesse caso.
ax1.set_xlim(1999,2025)

# Detalhes do grafico 1 como titulo, rotulos dos eixos x e y, legendas e grade. 
ax1.set_title('Taxa de fecundidade 2000-2025')
ax1.set_xlabel('ano')
ax1.set_ylabel('Taxa de fecundidade')
ax1.legend(title='Taxa de fecundidade')
ax1.grid(True)

# dados do segundo gráfico, idh.
ax2.plot(am['ano'],am['idhbr'],label='brasil',marker='o')
ax2.plot(am['ano'],am['idhlux'],label='luxemburgo',marker='o')
ax2.plot(am['ano'],am['idhphl'],label='filipinas',marker='o')
ax2.plot(am['ano'],am['usa'],label='estados unidos',marker='o')
ax2.plot(am['ano'],am['idhw'],label='global',marker='o')

# Definindo limites para os eixos x e y.
ax2.set_xlim(1999,2025)
ax2.set_ylim(0,1)

# Detalhes do grafico 1 como titulo, rotulos dos eixos x e y, legendas e grade.
ax2.set_title('IDH ao decorrer dos anos')
ax2.set_xlabel('ano')
ax2.set_ylabel('IDH')
ax2.legend(title='IDH')
ax2.grid(True)

# Exibindo os gráficos
plt.show()