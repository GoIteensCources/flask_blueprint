from flask import redirect, url_for, flash
from flask_mail import Message

from . import email
from flask_login import login_required, current_user
from app import mail


@email.route("/subscription")
@login_required
def subscription():
    msg = Message('Event reminder',
                  recipients=[current_user.email, ])
    # msg.body = 'Your daily weather '
    msg.html = (f"<p> Hello from FlaskApp <b>{current_user.nickname}</b> </p>"
                f"<p> Weather in the London: </p>")

    mail.send(msg)
    flash('Email sent')
    return redirect(url_for("index"))
