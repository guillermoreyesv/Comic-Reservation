class Request():
    def get_json(request):
        from application import app
        try:
            params_received = request.get_json()
            return True, params_received
        except Exception as e:
            app.logger.error(f'request body is not JSON {e}')
            response = {
                'code': 400,
                'status': 'failed',
                'message': 'The request body must be a JSON'
            }
            return False, response
