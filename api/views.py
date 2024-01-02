
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime


class CurrenTimeView(APIView):
    def get(self, request, *args, **kwargs):
        curren_time = datetime.now().strftime("%y-%m-%d %H-%M-%S")

        return Response({"time" : curren_time},status=status.HTTP_200_OK)
    