from rest_framework import serializers
from myapp.models import Users,Activity_periods

class ActivitySerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Activity_periods
		fields = ['start_time','end_time']

class UserSerializer(serializers.ModelSerializer):

	activity_periods = ActivitySerializer(read_only=True,many=True)
	class Meta:
		model = Users
		fields = ['id','real_name','tz','activity_periods']