import requests
from rest_framework import serializers


def validate_isin(isin):
    url = f"https://www.cdcp.cz/isbpublicjson/api/VydaneISINy?isin={isin}"
    response = requests.get(url)
    if response.status_code != 200 or not response.json().get('vydaneisiny'):
        raise serializers.ValidationError("Invalid ISIN")