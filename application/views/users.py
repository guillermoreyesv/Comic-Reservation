from flask.views import MethodView
from flask import request


class LayawayList(MethodView):
    def get(self):
        from application.utils.user import User
        return User.getProfile()
