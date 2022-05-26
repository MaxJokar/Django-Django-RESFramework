from rest_framework import serializers
    #Fields from our Model should be made the same for serializers
    # name=models.CharField(max_length=20)
    # family=models.CharField(max_length=30)
    # email=models.EmailField(max_length=30)
    # age=models.PositiveIntegerField()
    # username=models.CharField(max_length=30)
    # password=models.CharField(max_length=60)




class PersonSerializers(serializers.Serializer):
    name=serializers.CharField(max_length=20)
    family=serializers.CharField(max_length=30)
    email=serializers.EmailField(max_length=30)
    age=serializers.IntegerField()
    username=serializers.CharField(max_length=30)
    password=serializers.CharField(max_length=60)






