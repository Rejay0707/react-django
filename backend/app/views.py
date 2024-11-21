from rest_framework.views import APIView
from rest_framework.response import Response
from .models import React
from .serializer import ReactSerializer

class ReactView(APIView):
    def get(self, request):
        # Serialize data directly
        queryset = React.objects.all()
        serializer = ReactSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
