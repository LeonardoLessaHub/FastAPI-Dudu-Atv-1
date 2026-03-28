from fastapi import FastAPI

app = FastAPI()

@app.get("/what")
def what_is_api():
    return {
        "message": "Uma API (Application Programming Interface) é um conjunto de regras que permite que diferentes softwares e sistemas se comuniquem e troquem dados entre si."
    }

class User(BaseModel):
    data: list[str]
@app.get("/user")
def get_user(user: User):
    return user

@app.get("/calculate")
def calculate(category: str, a: float, b: float):
    if category == "soma":
        resultado = a + b
    elif category == "subtracao":
        resultado = a - b
    elif category == "multiplicacao":
        resultado = a * b
    elif category == "divisao":
        if b == 0:
            return {"error": "Erro: Não é possível dividir por zero."}
        resultado = a / b
    else:
        return {"error": "Categoria inválida. Tente: soma, subtracao, multiplicacao ou divisao."}
    
    if resultado.is_integer():
        resultado = int(resultado)

    return {
        "category": category,
        "result": f"O resultado é {resultado}"
    }