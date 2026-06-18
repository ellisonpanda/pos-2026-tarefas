import zeep

wsdl_url = "https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"

client = zeep.Client(wsdl=wsdl_url)

try:
    numero = int(input("Digite um número inteiro: "))
    
    resultado = client.service.NumberToWords(ubiNum=numero)
    
    print(f"Número digitado: {numero}")
    print(f"Por extenso em inglês: {resultado}")

except ValueError:
    print("Digite apenas números inteiros.")