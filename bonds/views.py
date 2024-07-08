from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Avg, Min, Sum
from .models import Bond
from .serializers import BondSerializer
from datetime import date


class BondViewSet(viewsets.ModelViewSet):
    serializer_class = BondSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Bond.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'])
    def analyze(self, request):
        bonds = self.get_queryset()
        avg_interest_rate = bonds.aggregate(Avg('interest_rate'))['interest_rate__avg']
        closest_maturity = bonds.aggregate(Min('maturity_date'))['maturity_date__min']
        total_value = bonds.aggregate(Sum('value'))['value__sum']

        future_value = sum([
            float(bond.value) * (1 + float(bond.interest_rate) / 100) ** ((bond.maturity_date - date.today()).days / 365)
            for bond in bonds
        ])

        return Response({
            'average_interest_rate': avg_interest_rate,
            'closest_maturity_date': closest_maturity,
            'total_value': total_value,
            'future_value': future_value
        })