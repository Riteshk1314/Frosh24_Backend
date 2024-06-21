from .models import Eventlist
class eventSerializer(serializers.ModelSerializer):
    class meta:
        model=Eventlist
        fields="__all__"
        
