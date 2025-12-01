"""Flask web application for warehouse management."""
from flask import Flask, render_template, request, redirect, url_for, flash
from varasto import Varasto

app = Flask(__name__)
app.secret_key = 'dev-secret-key-change-in-production'

# In-memory storage for warehouses
warehouses = {}
warehouse_counter = 0


@app.route('/')
def index():
    """Display list of all warehouses."""
    return render_template('index.html', warehouses=warehouses)


@app.route('/warehouse/create', methods=['GET', 'POST'])
def create_warehouse():
    """Create a new warehouse."""
    # pylint: disable=global-statement
    global warehouse_counter
    if request.method == 'POST':
        name = request.form.get('name')
        tilavuus = float(request.form.get('tilavuus', 0))
        saldo = float(request.form.get('saldo', 0))

        warehouse_counter += 1
        warehouse_id = warehouse_counter
        warehouses[warehouse_id] = {
            'id': warehouse_id,
            'name': name,
            'varasto': Varasto(tilavuus, saldo)
        }
        flash(f'Varasto "{name}" luotu onnistuneesti!', 'success')
        return redirect(url_for('index'))

    return render_template('create_warehouse.html')


@app.route('/warehouse/<int:warehouse_id>/edit', methods=['GET', 'POST'])
def edit_warehouse(warehouse_id):
    """Edit an existing warehouse."""
    if warehouse_id not in warehouses:
        flash('Varastoa ei löytynyt!', 'error')
        return redirect(url_for('index'))

    warehouse = warehouses[warehouse_id]

    if request.method == 'POST':
        warehouse['name'] = request.form.get('name')
        flash(f'Varasto "{warehouse["name"]}" päivitetty!', 'success')
        return redirect(url_for('index'))

    return render_template('edit_warehouse.html', warehouse=warehouse)


@app.route('/warehouse/<int:warehouse_id>/delete', methods=['POST'])
def delete_warehouse(warehouse_id):
    """Delete a warehouse."""
    if warehouse_id in warehouses:
        name = warehouses[warehouse_id]['name']
        del warehouses[warehouse_id]
        flash(f'Varasto "{name}" poistettu!', 'success')
    else:
        flash('Varastoa ei löytynyt!', 'error')

    return redirect(url_for('index'))


@app.route('/warehouse/<int:warehouse_id>/add', methods=['GET', 'POST'])
def add_content(warehouse_id):
    """Add content to a warehouse."""
    if warehouse_id not in warehouses:
        flash('Varastoa ei löytynyt!', 'error')
        return redirect(url_for('index'))

    warehouse = warehouses[warehouse_id]

    if request.method == 'POST':
        maara = float(request.form.get('maara', 0))
        warehouse['varasto'].lisaa_varastoon(maara)
        flash(f'{maara} lisätty varastoon "{warehouse["name"]}"!', 'success')
        return redirect(url_for('index'))

    return render_template('add_content.html', warehouse=warehouse)


@app.route('/warehouse/<int:warehouse_id>/remove', methods=['GET', 'POST'])
def remove_content(warehouse_id):
    """Remove content from a warehouse."""
    if warehouse_id not in warehouses:
        flash('Varastoa ei löytynyt!', 'error')
        return redirect(url_for('index'))

    warehouse = warehouses[warehouse_id]

    if request.method == 'POST':
        maara = float(request.form.get('maara', 0))
        otettu = warehouse['varasto'].ota_varastosta(maara)
        flash(f'{otettu} otettu varastosta "{warehouse["name"]}"!', 'success')
        return redirect(url_for('index'))

    return render_template('remove_content.html', warehouse=warehouse)


if __name__ == '__main__':
    app.run(debug=True)
