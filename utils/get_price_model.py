from decimal import Decimal

def get_price_token(prompt_number, output_token, days , users , model):
    price_input : float = 0.0
    price_output : float = 0.0
    
    if model == "gtp-3.5-turbo-0125" :
        price_input = 0.0005
        price_output = 0.0015
    
    if model == "gtp-3.5-turbo-instruct" :
        price_input = 0.0015
        price_output = 0.0020
    
    if model == "gtp-4" :
        price_input = 0.03
        price_output = 0.06
    
    if model == "gtp-4-32k" :
        price_input = 0.06
        price_output = 0.12
        
    total_tokens =  (prompt_number + output_token) / 1000
    price_total = (price_input + price_output)

    
    total =  ( (total_tokens * price_total) * days) * (users)
    
    number = Decimal(total)
    numero_sin_decimales = str(number.quantize(Decimal("0.00000001")))
    print(numero_sin_decimales)
    return numero_sin_decimales