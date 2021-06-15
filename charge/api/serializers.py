from rest_framework import serializers
from core_model.models import Charge


class ChargeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Charge
        fields = '__all__'
        read_only_fields = (
            "id",
        )
