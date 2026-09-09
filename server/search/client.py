from elasticsearch import AsyncElasticsearch
from core.config import settings

class ElasticsearchClient:
    def __init__(self):
        self.es = AsyncElasticsearch(hosts=[settings.ELASTICSEARCH_URL])

    async def close(self):
        await self.es.close()
    
    async def connect(self):
        await self.es.ping()
