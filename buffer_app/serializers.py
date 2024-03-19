from rest_framework import serializers
from. models import *

class AdminPublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'
        