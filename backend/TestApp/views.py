from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


from .serializer import AccountsSerializer
from .models import AccountsTable


@api_view(['GET'])
def hello_world(request):
    return Response({"message": "Hello, world!"})


class Accounts(APIView):
    def get(self, request):
        accounts = AccountsTable.objects.all()
        serializer = AccountsSerializer(accounts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AccountsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
