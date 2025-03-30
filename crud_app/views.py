from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import PersonModel
from .serializers import PersonSerializer



@api_view(['GET'])
def test(request):
    return Response({'message':'Hello, World!'})

# ---------------------- Get Post -------------------

@api_view(['GET','POST'])
def person_details(request):

    if request.method == 'GET':
       
        person_obj = PersonModel.objects.all()

        serializer = PersonSerializer(person_obj,many=True)

        return Response (serializer.data, status=status.HTTP_200_OK)

    
    if request.method == "POST":

        data = request.data

        serializer = PersonSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
# ---------------------- use pk-----------------------------
@api_view(['GET','PUT','DELETE'])
def person_details_update(request,pk):
    
    try:
        person_obj = PersonModel.objects.get(id=pk)
    except PersonModel.DoesNotExist:
        return Response([])
    
    if request.method == 'GET':
       # person_obj = PersonModel.objects.get(id=pk)

        serializer = PersonSerializer(person_obj)

        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        data = request.data
        
        #person_obj = PersonModel.objects.get(id=pk)

        serializer = PersonSerializer(person_obj, data = data,partial = False)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        data = request.data
        serializer = PersonSerializer(person_obj,data=data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)


    if request.method == 'DELETE':
      #  person_obj = PersonModel.objects.get(id=pk)
        person_obj.delete()
        return Response(
            {'message':'Person deleted sucessfully'},
            status = status.HTTP_204_NO_CONTENT
            )

