from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .queries import get_api, post_api, put_api

class DummyApi(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('id', openapi.IN_QUERY, description="ID", type=openapi.TYPE_INTEGER),
            openapi.Parameter('addtype', openapi.IN_QUERY, description="Address type", type=openapi.TYPE_STRING),
            openapi.Parameter('address', openapi.IN_QUERY, description="Address", type=openapi.TYPE_STRING),
            openapi.Parameter('city', openapi.IN_QUERY, description="City", type=openapi.TYPE_STRING),
        ],
        responses={200: 'OK'},
    )
    def get(self, request):
        data = {
            'id': request.GET.get('id'),
            'addtype': request.GET.get('addtype'),
            'address': request.GET.get('address'),
            'city': request.GET.get('city')
        }
        result = get_api(data)
        return Response(result, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['addtype', 'address', 'city'],
            properties={
                'addtype': openapi.Schema(type=openapi.TYPE_STRING),
                'address': openapi.Schema(type=openapi.TYPE_STRING),
                'city': openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        responses={201: 'Data inserted successfully', 400: 'Bad Request'},
    )
    def post(self, request):
        data = request.data
        response = post_api(data)
        if response == 'ok':
            return Response({'message': 'Data inserted successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Failed to insert data'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['id', 'addtype', 'address', 'city'],
            properties={
                'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                'addtype': openapi.Schema(type=openapi.TYPE_STRING),
                'address': openapi.Schema(type=openapi.TYPE_STRING),
                'city': openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        responses={200: 'Data updated successfully', 400: 'Bad Request', 500: 'Failed to update data'},
    )
    def put(self, request):
        data = request.data
        response = put_api(data)
        if response == 'ok':
            return Response({'message': 'Data updated successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Failed to update data'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


























# # views.py
# from django.shortcuts import render
# from django.http import Http404

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from drf_yasg import openapi
# from drf_yasg.utils import swagger_auto_schema

# # Assuming sqlquery.py is in the same directory as views.py
# from .sqlquery import get_api, post_api, put_api

# class dummy_api(APIView):

#     def get(self, request):
#         data = {
#             "addtype": request.GET.get('1'),
#             "address": request.GET.get('2'),
#             "city": request.GET.get('3')
#         }
#         print(data)
#         result = get_api(data)
#         return Response(result, status=200)

#     @swagger_auto_schema(
#         request_body=openapi.Schema(
#             type=openapi.TYPE_OBJECT,
#             required=['id', 'addtype', 'address', 'city'],
#             properties={
#                 'id': openapi.Schema(type=openapi.TYPE_INTEGER),
#                 'addtype': openapi.Schema(type=openapi.TYPE_STRING),
#                 'address': openapi.Schema(type=openapi.TYPE_STRING),
#                 'city': openapi.Schema(type=openapi.TYPE_STRING),
#             },
#         ),
#         responses={
#             201: 'Data inserted successfully',
#             400: 'Bad Request - Missing required field',
#         },
#     )
#     def post(self, request):
#         """
#         Insert data via POST request.
#         """
#         data = request.data
#         required_fields = ['id', 'addtype', 'address', 'city']
#         for field in required_fields:
#             if field not in data:
#                 return Response({'error': f'Missing required field: {field}'}, status=status.HTTP_400_BAD_REQUEST)
#         post_api(data)
#         return Response({'message': 'Data inserted successfully'}, status=status.HTTP_201_CREATED)

#     @swagger_auto_schema(
#         request_body=openapi.Schema(
#             type=openapi.TYPE_OBJECT,
#             required=['id', 'addtype', 'address', 'city'],
#             properties={
#                 'id': openapi.Schema(type=openapi.TYPE_INTEGER),
#                 'addtype': openapi.Schema(type=openapi.TYPE_STRING),
#                 'address': openapi.Schema(type=openapi.TYPE_STRING),
#                 'city': openapi.Schema(type=openapi.TYPE_STRING),
#             },
#         ),
#         responses={
#             200: 'Data updated successfully',
#             400: 'Bad Request - Missing required field',
#             500: 'Failed to update data',
#         },
#     )
#     def put(self, request):
#         data = request.data

#         # Ensure required fields are present in the request data
#         required_fields = ['id', 'addtype', 'address', 'city']

#         for field in required_fields:
#             if field not in data:
#                 return Response({'error': f'Missing required field: {field}'}, status=status.HTTP_400_BAD_REQUEST)

#         # Call the update_depreciation_master function to update the record
#         result = put_api(data)

#         if result == "ok":
#             return Response({'message': 'Data updated successfully'}, status=status.HTTP_200_OK)
#         else:
#             return Response({'error': 'Failed to update data'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
