from django.shortcuts import render
from myapp.models import Activity_periods,Users
from myapp.serializers import UserSerializer
from rest_framework.views import APIView
from django.http import JsonResponse

class getMembersView(APIView):

	def get(self,request):
		users = Users.objects.all()
		serializer =UserSerializer(users, many=True)
		return JsonResponse(data={"ok":"true", "members": serializer.data})



