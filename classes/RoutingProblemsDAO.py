from classes.RoutingProblemsDatabase import RoutingProblemsDatabase
from uuid import uuid4
import re


class RoutingProblemsDAO:
    def __init__(self):
        self.database = RoutingProblemsDatabase()

    def get_routing_problems(self, owner: str, page: int = 0, name: str = ''):
        page_size = 10

        return self.database.routing_problems_collection.find({
            'owner': owner,
            'name': {
                '$regex': re.compile(name, re.IGNORECASE)
            }
        },
        {
            '_id': 0,
            'owner': 0,
            'clients': 0,
            'settings': 0
        }
        ).skip(page_size * page).limit(page_size)
    
    def get_routing_problem(self, id: str, requester: str):
        return self.database.routing_problems_collection.find_one({
            'id': id,
            'owner': requester
        },
        {
            '_id': 0,
            'owner': 0
        }
        )
    
    def post_routing_problem(self, routing_info):
        clients = routing_info['clients']
        settings = routing_info['settings']
        owner = routing_info['owner']
        name = routing_info['name']
        routing_problem_id = str(uuid4())
        
        self.database.routing_problems_collection.insert_one({
            'id': routing_problem_id,
            'name': name,
            'clients': clients,
            'settings': settings,
            'owner': owner
        })

        return routing_problem_id
    
    def delete_routing_problem(self, id, requester):

        return self.database.routing_problems_collection.delete_one({
            'id': id,
            'owner': requester
        })

    def close_connection(self):
        self.database.client.close()

    
        
    
