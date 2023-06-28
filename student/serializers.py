from rest_framework import serializers


from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = '__all__'



###Можно и без сигнала обойтись

    # def create(self, validated_data):
    #     student = Student.objects.create(**validated_data)
    #     send_register_mail(student.email, student.full_name)
    #     return student