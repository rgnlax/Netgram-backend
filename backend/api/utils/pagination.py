from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination

class CustomPagination(LimitOffsetPagination):
    def get_paginated_response(self, data):
        if len(data) > 1:
            return Response(data)
        else:
            return Response(data[0])