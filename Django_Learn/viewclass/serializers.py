from rest_framework import serializers
from . models import TbCustomerPaper


class CpSerializer(serializers.ModelSerializer):
    """
    Serializers把querysets和model instances这些复杂的数据结构转化为native Python
    以便于以json,xml或其它内容类型的形式render出去。
    """
    class Meta:
        model = TbCustomerPaper
        fields = "__all__"
