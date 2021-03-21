from rest_framework import serializers
from leads.models import Lead

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        Model = Lead