from rest_framework.response import Response
from submissions.models import Submission
from submissions.serializers import SubmissionSerializer
from rest_framework.views import APIView
from rest_framework import status


# Create your views here.
class SubmissionsList(APIView):
    def get(self, request, format=None):
        tasks = Submission.objects.all()
        serializer = SubmissionSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SubmissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)