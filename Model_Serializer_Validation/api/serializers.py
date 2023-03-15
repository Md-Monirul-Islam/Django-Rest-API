from dataclasses import field, fields
from xml.dom import ValidationErr
from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    # Validator
    def start_with_r(value):
        if value[0].lower() != 'r':
            raise ValidationErr("Name should be start with R")
    name = serializers.CharField(validators=[start_with_r])

    #name = serializers.CharField(read_only=True)
    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']
        #read_only_fields = ['name', 'roll']
        #extra_kwargs = {'name': {'read_only': True}}

    #################### Validation ########################
    # Field level validation
    def validate_roll(self, value):
        if value >= 200:
            raise ValidationErr("Seat Full!!")
        return value

    # Object level validation
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'lal' and ct.lower() != 'pabna':
            raise serializers.ValidationError('City must be Pabna!!')
        return data
