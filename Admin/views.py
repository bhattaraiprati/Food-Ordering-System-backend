from django.shortcuts import render
# from rest_framework.viewsets import ModelViewSet
from Restaurant.models import Restaurant
from Restaurant.serializer import RestaurantSerializer
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework import  viewsets ,status


# Create your views here.
@api_view(['get'])
def debugging(request):

    return Response({"sucess":"sucess"})

class RestaurantDetailsViewSets(viewsets.ModelViewSet):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()

    @action(detail=False, methods=['get'])
    def pending(self, request):
        pending_users = Restaurant.objects.filter(status='pending')
        serializer = self.get_serializer(pending_users, many=True)
        return Response(serializer.data)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial',False)
        instance = self.get_object()
        data = request.data

        if 'status' in data:
            instance.status = data['status']
            instance.save(update_fields=['status'])

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data, status=status.HTTP_200_OK)


    
