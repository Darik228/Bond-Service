from rest_framework import serializers
from .models import Bond
from .validators import validate_isin


class BondSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bond
        fields = '__all__'

    def validate_isin(self, value):
        validate_isin(value)
        return value