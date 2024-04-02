from fastapi import Request, HTTPException

from classes.RoutingProblemsDAO import RoutingProblemsDAO

async def post_routing_problem(request: Request, owner: str):

    data = await request.json()

    clients = data.get('clients')
    settings = data.get('settings')
    name = data.get('name')

    if clients is None:
        raise HTTPException(400, detail="You should provide the clients")
    if settings is None:
        raise HTTPException(400, detail="You should provide the settings")
    if name is None:
        raise HTTPException(400, detail="You should provide a name")

    routing_problems_dao = RoutingProblemsDAO()

    routing_problem_id = routing_problems_dao.post_routing_problem({
        'clients': clients,
        'settings': settings,
        'owner': owner,
        'name': name
    })

    routing_problems_dao.close_connection()

    return {
        'id': routing_problem_id
    }