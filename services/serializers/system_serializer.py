from dataclasses import field
from pyexpat import model
from statistics import mode
from rest_framework import serializers
from services.models import SystemInfoModel, SystemInfoFileModel
from rest_framework.exceptions import ValidationError


class SystemInfoFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemInfoFileModel
        fields = ('id', 'file',)
    
    def validate_source(self, value):
        if not value.endswith(".mp4"):
            raise ValidationError(detail='Mp4 file is required')
        return value


class SystemSerializer(serializers.HyperlinkedModelSerializer):
    files = SystemInfoFileSerializer(source='systeminfofilemodel_set', many=True, read_only=True)

    class Meta:
        model = SystemInfoModel
        fields = ('id', 'title', 'description', 'files')

    def create(self, validated_data):
        files_data = self.context.get('view').request.FILES
        print(files_data)
        systeminfo = SystemInfoModel.objects.create(title=validated_data.get('title', 'no-title'), 
                                         type=validated_data.get('type', 'no-type'), description=validated_data.get('description', 'no-description'))
        for files_data in files_data.values():
            SystemInfoFileModel.objects.create(systeminfo=systeminfo, file=files_data)
        return systeminfo

