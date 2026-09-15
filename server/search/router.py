from fastapi import APIRouter, Depends, HTTPException, status

from elasticsearch import AsyncElasticsearch
from .client import ElasticsearchClient

from .schema import Event, SearchResponse, SearchRequest, SearchFilter
from .service import search_event

router = APIRouter(tags=["search"])

def get_es() -> AsyncElasticsearch:
    return ElasticsearchClient.es

@router.get("/events/search")
async def search_events(request: SearchRequest, es: AsyncElasticsearch = Depends(get_es)) -> SearchResponse:
    try:
        filter = SearchFilter()
        response = await es.search(index="events", body={"query": {"match_all": {}}})
        return await search_event(es, SearchRequest(**response), filter)
    except Exception as e:
        raise 