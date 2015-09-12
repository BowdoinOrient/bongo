from rest_framework.decorators import api_view
from rest_framework.response import Response
from haystack.query import SearchQuerySet
from bongo.apps.bongo.helpers import arbitrary_serialize


@api_view(('POST',))
def search(request, format=None):
    if 'query' not in request.data:
        return Response({"error": "'query' missing from request body."}, status=422)
    else:
        query = request.data['query']

    sqs = SearchQuerySet().all()
    res = sqs.auto_query(query)

    results = [arbitrary_serialize(res_item.object) for res_item in res]

    return Response(results, status=200)
