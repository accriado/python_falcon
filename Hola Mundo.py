from wsgiref.simple_server import make_server

# things.py

# Let's get this party started!
import falcon


# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.
class HolaMundo(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = ('\nTwo things awe me most, the starry sky '
                     'above me and the moral law within me.\n'
                     '\n'
                     '    ~ Immanuel Kant\n\n'
                     '\HOLA MUNDO')
class HolaMundoJson(object):
    def on_get(self,req,resp):
        resp.media= {'response':'Hola Mundo'}


if __name__=='__main__':
    api = falcon.API()
    api.add_route('/',HolaMundo())
    api.add_route('/json',HolaMundoJson())
    
    with make_server('',8080,api) as httpd:
        httpd.serve_forever()


# falcon.API instances are callable WSGI apps
#app = falcon.API()

# Resources are represented by long-lived class instances
#things = ThingsResource()

# things will handle all requests to the '/things' URL path
#app.add_route('/things', things)