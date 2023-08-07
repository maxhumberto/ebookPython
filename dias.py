from datetime import datetime

def diferenca_em_dias(data1, data2):
    formato_data = "%Y-%m-%d"
    data1_obj = datetime.strptime(data1, formato_data)
    data2_obj = datetime.strptime(data2, formato_data)

    diferenca = abs((data2_obj - data1_obj).days)
    return diferenca

# Teste da função
data1 = "2023-08-01"
data2 = "2023-08-10"
print(diferenca_em_dias(data1, data2))  # Resultado: 9