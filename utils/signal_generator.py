def generate_signal(last_price, prediction):
    if prediction > last_price:
        return 'BUY'
    elif prediction < last_price:
        return 'SELL'
    else:
        return 'HOLD'
