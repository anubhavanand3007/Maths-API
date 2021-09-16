from fastapi import APIRouter, Response, Request
from fastapi.params import Cookie
import mysql.connector
from pydantic import BaseModel
from typing import Optional

from starlette.routing import Host

router = APIRouter(prefix='/database', tags=['Database'])

class DBconnector(BaseModel):
    host: str
    user: str
    passwd: str
    database: str
    

@router.post('/mysql')
async def main(DBconnector: DBconnector, Query: str):
    conn = mysql.connector.connect(
        host = DBconnector.host,
        user = DBconnector.user,
        password = DBconnector.passwd,
        database = DBconnector.database
    )
    c = conn.cursor()

    c.execute(Query)
    conn.commit()
    data = c.fetchall()
    if data != [()]:
        return data




