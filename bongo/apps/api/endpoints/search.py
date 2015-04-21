from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(('POST',))
def search(request, format=None):
    if 'query' not in request.data:
        return Response({"error": "'query' missing from request body."}, status=422)
    else:
        query = request.data['query']

    results = {}

    return Response(results, status=200)