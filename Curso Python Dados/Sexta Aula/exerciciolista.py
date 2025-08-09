#exercicio

import pandas as pd

#lista de aparelhos

aparelhos = [ 'TV 55 pl', 'Caixa Bluetooth', 'Monitor Curvo', 'Samsung Galaxy S22',
             'Huawei P50 Pro', 'MacBook Air M2', 'JBL Tune 510BT', 'Sony WH-1000XM5',
              'Apple AirPods Pro', 'PlayStation 5'
]

#lista de precos correspondentes

precos = [2.800, 250.00, 1400.00, 3.500, 4.200, 8.500, 250.00, 2.200, 1800.00, 4.500]

#lista de estoque correspondente

estoque = [20, 35, 15, 12, 50, 60, 25, 10, 8, 18]


df = pd.DataFrame({
    'Aparelhos' : aparelhos,
    'Preços' : precos,
    'Estoque' : estoque
})

df['Total'] = df['Preços'] * df['Estoque']

print(df)
