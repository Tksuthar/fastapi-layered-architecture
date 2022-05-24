import json
from core.services.database_service import SqlLiteService

with open("local.settings.json") as f:
    env = json.load(f)

_sql_session_maker = SqlLiteService(env["SqlLiteConnectionString"]).get_session_maker()