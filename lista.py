
lista = {
    0: {
        "id": 7112000,
        "Description": "Audiometria(s)",
        "CST": 1,
        "Aliq": 0.00,
        "VU": 30.00,
        "Amount": 1
    },
    1: {
        "id": 7112000,
        "Description": "Mensalidade Funcionário(s)",
        "CST": 1,
        "Aliq": 0.00,
        "VU": 32.00,
        "Amount": 8
    },
    2: {
        "id": 7112000,
        "Description": "Audiometria(s)",
        "CST": 1,
        "Aliq": 0.00,
        "VU": 30.00,
        "Amount": 3
    }
}

for total in lista:
    amount = lista[total]["VU"] * lista[total]["Amount"]
    lista[total]["VT"] = amount