from flask import Flask, render_template, request

app = Flask(__name__)
mi_cliente = None

class Cliente:
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        self.nombre = nombre
        self.apellido = apellido
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def depositar(self, monto):
        self.balance += monto

    def retirar(self, monto):
        if monto <= self.balance:
            self.balance -= monto
            return True  # Return True for successful withdrawal
        else:
            return False  # Return False for insufficient funds

def crear_cliente():
    # You can customize this function based on your needs
    return Cliente(nombre="ikar", apellido="jesus", numero_cuenta="123456", balance=1000)

@app.route('/', methods=['GET', 'POST'])
def vista_cliente():
    global mi_cliente

    if mi_cliente is None:
        mi_cliente = crear_cliente()

    if request.method == 'POST':
        action = request.form['action']
        monto = int(request.form['monto'])

        # Validate inputs
        if not action or not monto:
            return render_template('index.html', cliente=mi_cliente, error="Please fill out all fields")

        if action == 'depositar':
            mi_cliente.depositar(monto)
        elif action == 'retirar':
            success = mi_cliente.retirar(monto)
            if not success:
                return render_template('index.html', cliente=mi_cliente, error="Insufficient funds for withdrawal")

    return render_template('index.html', cliente=mi_cliente)

if __name__ == '__main__':
    app.run(debug=True)

