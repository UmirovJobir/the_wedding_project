
from django import views
from rest_framework.response import Response
from django.http import HttpResponseNotAllowed
from rest_framework.views import APIView

from services.models import SystemInfoModel, RestoranModel, BookedDate, EvantModel, ServiceModel, TableModel, MenuModel, Order, SystemInfoFileModel

from services.serializers.system_serializer import SystemSerializer, SystemInfoFileSerializer
from services.serializers.restoran_serializer import RestoranSerializer, EvantSerializer
from services.serializers.service_serializer import ServiceSerializer, MenuSerializer
from services.serializers.restoran_serializer import TableSerializer
from services.serializers.order_serializer import OrderGetSerializer, OrderPostSerializer


from rest_framework import permissions, generics

from rest_framework.response import Response

from accounts.models import  BlacklistUser


class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff

class SystemView(generics.ListAPIView):
    serializer_class = SystemSerializer 
    queryset = SystemInfoModel.objects.all()
    permission_classes = [IsAdminUser]

class SystemFileView(generics.ListAPIView):
    serializer_class = SystemInfoFileSerializer 
    queryset = SystemInfoFileModel.objects.all()
    permission_classes = [IsAdminUser]

class TableView(generics.ListAPIView):
    serializer_class = TableSerializer
    queryset = TableModel.objects.all()


    
class RestoranView(generics.ListAPIView):
    serializer_class = RestoranSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
            city = self.request.user.city
            date = self.request.user.event_date
            events_id = self.request.query_params.get("id")
            restorans = RestoranModel.objects.filter(event_id=events_id).all()
            booked_dates = BookedDate.objects.filter(date=date).values_list('restoran_id_id', flat=True)
            if booked_dates.exists():
                restorans = restorans.exclude(id__in=booked_dates)
                return RestoranModel.objects.filter(id__in=restorans, city=city)
            return restorans.filter(city=city)

class EvantView(generics.ListAPIView):
    serializer_class = EvantSerializer 
    queryset = EvantModel.objects.all()
    permission_classes = [IsAdminUser]

class ServiceView(generics.ListAPIView):
    serializer_class = ServiceSerializer 
    queryset = ServiceModel.objects.all()
    permission_classes = [IsAdminUser]

class MenuView(generics.ListAPIView):
    serializer_class = MenuSerializer 
    queryset = MenuModel.objects.all()

    def get_queryset(self):
        events_id = self.request.query_params.get("id")
        return MenuModel.objects.filter(event_id=events_id).all()


class OrderView(APIView):
    serializer_class = OrderGetSerializer
    queryset = Order.objects.all()
    permission_classes = [permissions.IsAuthenticated]


    def post(self, request):
        blacklist = BlacklistUser.objects.all()
        blacklist = blacklist.values("user_id_id")
        user = self.request.user 
        list = []
        for black in blacklist:
            list.append(black['user_id_id'])
        if user.id in list: 
            return HttpResponseNotAllowed("not allowed")
        else:
            serializer = OrderPostSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.validated_data['user_id'] = self.request.user
    
            total_price = 0

            services = ServiceModel.objects.filter(pk__in=request.data.get('service_id')).all()
            menus = MenuModel.objects.filter(pk__in=request.data.get('menu_id')).all()
            for service in services:
                total_price += service.price
            for menu in menus:
                total_price += menu.price

            serializer.validated_data['day'] = self.request.user.event_date
            serializer.save(total_price=total_price, )

            restoran_id = request.data.get('restoran_id')
            restoran = RestoranModel.objects.get(id=restoran_id)
            date_user = self.request.user.event_date 

            BookedDate.objects.create(date=date_user, restoran_id=restoran)
        
            return Response(data=serializer.data)

