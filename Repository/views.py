from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import QuestionDb
from Repository.serializers import QuestionSerializers

# Create your views here.
class QuestionListCreateView(APIView):
    def get(self,request):

        qs=QuestionDb.objects.all()
        serializer_instance=QuestionSerializers(qs,many=True)
        return Response(data=serializer_instance.data)

    def post(self,request):
        form_data=request.data
        serializer_instance=QuestionSerializers(data=form_data)

        if serializer_instance.is_valid():
            actual_data=serializer_instance._validated_data
    
            QuestionDb.objects.create(**actual_data)

            return Response(data={"message":"Question added successfully."})
        else:
            return Response(data={"message":"Invalid data", "errors": serializer_instance.errors})
        
class QuestionRetriveUpadateDeleteView(APIView):
    def get(self,request,pk):
        qs=QuestionDb.objects.get(id=pk)
        serializer_instance=QuestionSerializers(qs)
        return Response(data=serializer_instance.data)
    def put(self,request,pk):
        form_data=request.data
        serializer_instance=QuestionSerializers(data=form_data)
        if serializer_instance.is_valid():
            actual_data=serializer_instance.validated_data
            QuestionDb.objects.filter(id=pk).update(**actual_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)   
    def delete(self,request,pk):
        QuestionDb.objects.filter(id=pk).delete()
        return Response(
            {
                "message":"question deleted successfully."
            }
        )