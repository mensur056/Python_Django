from rest_framework import serializers


class MakaleSerializer(serializers.Serializer):
    yazar = serializers.CharField()
    baslik = serializers.CharField()
    aciklama = serializers.CharField()
    metin = serializers.TextField()
    sehir = serializers.CharField()
    yayimlanma_tarihi = serializers.DateField()
    aktif = serializers.BooleanField()
    yaratilma_tarihi = serializers.DateTimeField()
    guncelleme_tarihi = serializers.DateTimeField()
