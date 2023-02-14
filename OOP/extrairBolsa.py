# Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd
import os


class ExtrairBolsa:
    def __init__(self, ativos):
        self.driver = webdriver.Chrome()
        self.ativos = ativos
        self.preco_ativo = []
        self.var_preco_ativo =[]
        self.var_perc_ativo = []
    
    def extrair_dados(self, ativos):
        for ativo in self.ativos:
            self.driver.get(f"https://br.tradingview.com/symbols/BMFBOVESPA-BGI{ativo}2023/")
            sleep(2)
            cotacao = self.driver.find_element(By.XPATH,'//*[@id="anchor-page-1"]/div/div[3]/div[1]/div/div/div/div[1]/div[1]').text
            var_preco = self.driver.find_element(By.XPATH,'//*[@id="anchor-page-1"]/div/div[3]/div[1]/div/div/div/div[1]/div[3]/span[1]').text
            var_perc = self.driver.find_element(By.XPATH,'//*[@id="anchor-page-1"]/div/div[3]/div[1]/div/div/div/div[1]/div[3]/span[2]').text
            ativos_values = [cotacao, var_preco, var_perc]
            self.preco_ativo.append(ativos_values)
    
    def criar_planilha(self):
        df = pd.DataFrame(columns=['MÊS','PREÇO', 'VAR.R$', 'VAR.%'])
        meses = ['FEV.','MAR.', 'ABR.', 'MAI.', 'JUN.' ]
        i = 0
        for precos in self.preco_ativo:
            data = {'MÊS': [meses[i]],
                    'PREÇO': [precos[0]], 
                    'VAR.R$': [precos[1]],
                    'VAR.%': [precos[2]]}
        i= i + 1
        df = pd.concat([df, pd.DataFrame(data)], ignore_index=True)

        planilha = df.to_excel('Arroba_Boi_Futuro.xlsx', index=False)

letras = []
ativos = []        
while True:
    ativos = input('DIGITE A LETRA DOS ATIVOS:')
    letras.append(ativos)
    if ativos[0] == '0':
        break
print(letras)
extrair_bolsa = ExtrairBolsa(letras)
extrair_bolsa.extrair_dados(letras)