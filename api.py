#les bibliotheques
import api as api
from flask import Flask, request
from flask_restx import Api, Resource, fields
import client_db

app = Flask(__name__)
api = Api(app, version='0.1',title='Mon API',description='Cette API permet de créer, modifier et supprimer des entités.')
#création d'un espace de nom
namespace_entity = api.namespace('entite',description="Contient une liste d'opérations sur les entités.")

#création d'un modele
entity_model = api.model('Entité',{
    'id':fields.Integer(readonly=True,description ="Identification unique de l'entité",example=1),
    'libellé_entité':fields.String(required=True,description='Le libellé de l entité",example="Mon libellé')
    })

#création de ma méthode POST
@namespace_entity.route('/<int:id>')
class EntityIdQueries(Resource):
    @namespace_entity.doc('Ajouter une nouvelle entité')
    @namespace_entity.expect(entity_model)
    @namespace_entity.response(201,'Success')
    @namespace_entity.response(400,'Fail')
    def post(self, id):
        '''Ajouter une nouvelle entité'''
        if 'libellé_entité' not in api.payload or api.payload['libellé_entité'] =="":
            return "Libellé non trouvé ou vide",400
        label = api.payload['libellé_entité']

        success = client_db.ajouter_entite_bd(id,label)
        if success:
            print(f"Entité {id} {label} ajoutée ")
            return id, 201
        else:
            print(f"L'entité n'a pas été {id} {label} ajoutée")
            return id, 401

    @namespace_entity.doc('Obtenir une entité avec son ID')
    @namespace_entity.marshal_with(entity_model)
    def get(self,id):
        '''Obtenir une entité avec son ID'''
        entite = {
            'id': 1,
            'libellé_entité':'mon_entite'
        }
        entite = client_db.obtenir_entite_bd(id)
        return entite

    @namespace_entity.doc('Supprimer une entité avec son ID')
    @namespace_entity.response(204,'entité supprimée')
    def delete(self, id):
        '''Supprimer une entité avec son ID'''
        success = client_db.supprimer_entite_bd(id)
        if success :
            return f"L'entité {id} a été supprimer",204
        else:
            return f"L'entité {id} n'a pas été supprimée",401

    @namespace_entity.expect(entity_model)
    @namespace_entity.doc("Mettre à jour une entité avec son ID")
    def put(self, id):
        '''Mettre à jour une entité avec son ID'''
        if 'libellé_entité' not in api.payload or api.payload['libellé_entité'] == "":
            return "Libellé non trouvé ou vide",400
        label = api.payload['libellé_entité']

        success = client_db.mettre_a_jour_db(id,label)
        if success :
            return f"L'entité{id} a été mise à jour",204
        else:
            return f"L'entité{id} n'a pas été mise à jour",401


@namespace_entity.route('/')
class EntityBaseQueries(Resource):
    @namespace_entity.doc('Retourner toutes les intités')
    @namespace_entity.marshal_with(entity_model,as_list=True,code=200)
    @namespace_entity.response(400,'Fail')
    def get(self):
        '''Retourner toutes les entites'''
        liste_entities = [{
            'id':1,
            'libellé_entité':'mon_entite'
        },{
            'id': 2,
            'libellé_entité': 'mon_entite'
        }]

        liste_entities = client_db.obtenir_toutes_entite_bd()
        if liste_entities is not None:
            return liste_entities,200
        else:
            return [],400

if __name__ == '__main__':
    app.run(debug=True)

