
lista = {
    0: {
        "id": 7112000,
        "description": "Audiometria(s)",
        "cst": 1,
        "aliq": 0.00,
        "vu": 30.00,
        "amount": 1
    },
    1: {
        "id": 7112000,
        "description": "Mensalidade Funcionário(s)",
        "cst": 1,
        "aliq": 0.00,
        "vu": 32.00,
        "amount": 8
    },
    2: {
        "id": 7112000,
        "description": "Audiometria(s)",
        "cst": 1,
        "aliq": 0.00,
        "vu": 30.00,
        "amount": 3
    }
}

for total in lista:
    amount = lista[total]["vu"] * lista[total]["amount"]
    lista[total]["vt"] = amount