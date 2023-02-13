from flask.views import MethodView
from flask import request


class LayawayList(MethodView):
    def get(self):
        from application.utils.user import User
        from application import app
        response = {'code': 500, 'message': 'server failed'}
        list_filters = ['onsaledate', 'title', 'id']

        # Get Bearer Token
        authorization = request.headers.get('Authorization')

        # Validate Token
        try:
            info_user = User.validate_token(authorization)
        except Exception as e:
            response = {
                'code': 400,
                'message': 'Invalid token'
            }
            app.logger.error(f'Invalid token {e}')
            return response, response['code']

        # Get params
        filter = request.args.get(key='orderBy', default='')

        # Evaluate params
        if filter.lower().strip() not in list_filters and filter:
            response = {
                'code': 400,
                'message': 'Invalid Filter'
            }
            app.logger.error(f'Invalid Filter {filter}')
            return response, response['code']

        # Search comics
        comic_list = info_user.get('comics_layaway')
        if not comic_list:
            response = {'code': 404, 'message': 'Not found comics layawayed'}
            return response, response['code']

        # Order comics
        if filter:
            comic_list = sorted(comic_list, key=lambda x: x[filter])

        response = {'code': 200, 'message': 'Found comics layawayed'}
        response['comics'] = comic_list
        return response, response['code']
