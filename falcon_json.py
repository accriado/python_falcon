import json, falcon

class ObjRequestClass:

    def on_get(self,req,resp):
        data=json.loads(req.stream.read())

        content={
            'nombre':'Anthony',
            'apellido':'Campodonico',
            'país':'Perú'
        }

        output={}
        if(data['method'] =='get-nombre'):
            output['value']=content['nombre']

        else:
            output['value']== None

        resp.body=json.dumps(content)

api=falcon.API()
api.add_route('/test',ObjRequestClass())