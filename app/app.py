from flask import Flask, redirect, render_template, request, url_for
from models import ItemModel

app = Flask(__name__)
model = ItemModel()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        if name:
            model.add_item(name)
        return redirect(url_for('index'))

    items = model.get_all_items()
    return render_template('index.html', items=items)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
