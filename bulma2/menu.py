from flask import Blueprint, render_template
from flask_login import login_required, current_user

menu = Blueprint('menu', __name__)


@menu.route('/dishes')
@login_required
def dishes():
    return render_template('dishes.html', name=current_user.name)