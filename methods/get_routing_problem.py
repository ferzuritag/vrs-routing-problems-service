from fastapi import HTTPException

from classes.RoutingProblemsDAO import RoutingProblemsDAO

def get_routing_problem(id, requester):
    routing_problems_dao = RoutingProblemsDAO()

    routing_problem = routing_problems_dao.get_routing_problem(id, requester)

    routing_problems_dao.close_connection()

    if routing_problem is None:
        raise HTTPException(404, detail='Problem not found')
    
    return routing_problem