from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from app.models import Job
from app.permissions import IsAdmin
from app.serializer import JobsSerializer

# Create your views here.


def index(request):
    return render(request, 'index.html')


class JobsList(APIView):
    def get(self, request):
        jobs = Job.objects.all()
        serializers = JobsSerializer(jobs, many=True)

        return Response(serializers.data)

    def post(self, request):
        serializers = JobsSerializer(data=request.data)
        if serializers.is_valid():
            job = serializers.save(commit=False)
            job.save_post()
            return Response(serializers.data, status=HTTP_201_CREATED)
        return Response(serializers.errors, status=HTTP_400_BAD_REQUEST)


class JobsDescription(APIView):
    def get_job(self, id):
        try:
            return Job.objects.get(id=id)
        except Job.DoesNotExist:
            return Http404

    def get(self, request, id):
        job = self.get_job(id)
        serializers = JobsSerializer(job)
        return Response(serializers.data)
