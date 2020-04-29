from typing import Dict, Optional, Any
from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.routing import Route, Mount
from tartiflette import Resolver
from tartiflette_asgi import TartifletteApp
import httpx


async def home(request):
    return PlainTextResponse("Hello, world!")


@Resolver("Query.containers")
async def containers(parent, args, context, info):
    async with httpx.AsyncClient() as client:
        response = await client.get("http://localhost:3000/api/wms/containers")
        return response.json()


@Resolver("Container.type")
async def container_type(parent, args, context, info):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"http://localhost:3000/api/wms/container/type/{parent['type_id']}"
        )
        return response.json()


@Resolver("Mutation.CreateContainer")
async def resolve_mutation_create_container(
    parent: Optional[Any],
    args: Dict[str, Any],
    ctx: Dict[str, Any],
    info: "ResolveInfo",
) -> Dict[str, Any]:
    """
    Resolver in charge of the mutation of a recipe.
    :param parent: initial value filled in to the engine `execute` method
    :param args: computed arguments related to the mutation
    :param ctx: context filled in at engine initialization
    :param info: information related to the execution and field resolution
    :type parent: Optional[Any]
    :type args: Dict[str, Any]
    :type ctx: Dict[str, Any]
    :type info: ResolveInfo
    :return: the mutated recipe
    :rtype: Dict[str, Any]
    :raises Exception: if the recipe id doesn't exist
    """
    return "{}"


sdl = """
type Query { 
    containers(offset: Int, limit: Int, query:String): [Container!]
}

type Container {
    id: Int!
    code: String!
    type: ContainerType
    type_id: Int!
}

type ContainerType {
    id: Int!
    code: String!
    label: String
}

input ContainerInput {
    code: String!
}
type Mutation {
    CreateContainer(container: ContainerInput!): Container!
}
"""


def create_app():
    graphql = TartifletteApp(sdl=sdl,)
    routes = [Route("/", endpoint=home), Mount("/graphql", graphql)]
    return Starlette(routes=routes, on_startup=[graphql.startup])
