from rest_framework import serializers

from vehicle.models import Car, Moto, Milage
from vehicle.validators import TitleValidator


class MilageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milage
        fields = '__all__'


# class CarSerializer(serializers.ModelSerializer):
#     last_milage = serializers.IntegerField(source='milage_set.all.first.milage')
#     milage = MilageSerializer(many=True)
#
#     class Meta:
#         model = Car
#         fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    last_milage = serializers.SerializerMethodField()
    milage = MilageSerializer(many=True)

    class Meta:
        model = Car
        fields = '__all__'

    def get_last_milage(self, obj):
        if obj.milage.all().first():
            return obj.milage.all().first().milage
        return 0

    def create(self, validated_data):
        milages_data = validated_data.pop('milage')
        car = Car.objects.create(**validated_data)
        for milage_data in milages_data:
            Milage.objects.create(car=car, **milage_data)
        return car


class MotoSerializer(serializers.ModelSerializer):
    last_milage = serializers.SerializerMethodField()

    class Meta:
        model = Moto
        fields = '__all__'

    def get_last_milage(self, obj):
        if obj.milage.all().first():
            return obj.milage.all().first().milage

        return 0


class MotoMilageSerializer(serializers.ModelSerializer):
    moto = MotoSerializer()

    class Meta:
        model = Milage
        fields = ('milage', 'year', 'moto',)


class MotoCreateSerializer(serializers.ModelSerializer):
    milage = MilageSerializer(many=True)

    class Meta:
        model = Moto
        fields = '__all__'
        validators = [
            TitleValidator(field='title'),
            serializers.UniqueTogetherValidator(queryset=Moto.objects.all(), fields=('title', 'description',))
        ]

    def create(self, validated_data):
        milage_extracted = validated_data.pop('milage')
        moto_item = Moto.objects.create(**validated_data)

        for milage in milage_extracted:
            Milage.objects.create(**milage, moto=moto_item)

        return moto_item
