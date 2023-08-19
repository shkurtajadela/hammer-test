from .models import Phone
from rest_framework import serializers
import random
import string


class PhoneSerializers(serializers.ModelSerializer):
    generated_code = serializers.ReadOnlyField(source='')
    class Meta:
        model = Phone

        fields = ['phone_number', 'generated_code']
        
        def add_code(self, validated_data):
            invitation_code = validated_data.get('invitation_code', None)

            if invitation_code:
                phone = Phone.objects.filter(generated_code=invitation_code).first()

                if phone:
                    phone.invitation_code = validated_data.get('invitation_code', phone.invitation_code)
                    phone.save()
                    return phone
                else:
                    raise serializers.ValidationError("Invalid invitation code.")
            else:
                raise serializers.ValidationError("Invitation code is required.")
            
        

def generate_invite_code(length):
    characters = string.ascii_letters + string.digits  # Все буквы и цифры
    while True:
        code = ''.join(random.choice(characters) for _ in range(length))
        if not Phone.objects.filter(generated_code=code).exists():
            return code