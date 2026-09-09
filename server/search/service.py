from elasticsearch import AsyncElasticsearch
from .schema import Event, SearchResponse, SearchRequest, SearchFilter

async def search_event(
    es: AsyncElasticsearch,
    request: SearchRequest,
    filter: SearchFilter | None = None,
) -> SearchResponse:
    try:
        must = [{"match": request.query}]
        filter_clauses = []
        if filter:
            if filter.location:
                filter_clauses.append({"term": {"location": filter.location}})
            if filter.date:
                filter_clauses.append({"term": {"date": filter.date}})
            if filter.availability:
                filter_clauses.append({"term": {"availability": filter.availability}})

        response = await es.search(index="events", body={"query": {"bool": {"must": must, "filter": filter_clauses}}})
        return SearchResponse(**response)

    except Exception as e:
        return SearchResponse(error=str(e))
