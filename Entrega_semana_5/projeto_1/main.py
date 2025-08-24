# Importa o arquivo que contém os cálculos
import mean_var_std
from unittest import main

# Define o parâmetro usado e imprime o resultado da função
print(mean_var_std.calculate([0,1,2,3,4,5,6,7,8]))

# Roda os testes unitários automaticamente
main(module='test_module', exit=False)