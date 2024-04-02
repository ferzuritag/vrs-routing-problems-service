from pymongo import MongoClient

class RoutingProblemsDatabase:
    def __init__(self):

        self.client = MongoClient()

        self.database = self.client.get_database('routing_problems')

        self.routing_problems_collection = self.database.get_collection('routing_problems')
    
