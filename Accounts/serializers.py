# from xml.dom import ValidationErr
from rest_framework.exceptions import ValidationError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import DjangoUnicodeDecodeError, force_bytes, smart_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from rest_framework import serializers

from Accounts.utils import Util
from django.core.mail import send_mail
from django.conf import settings
from .models import User
from .profile import Profile




class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"})

    class Meta:
        model = User
        fields = ["name", "email", 'contact',"password", "password2"]
        extra_kwargs = {"password2": {"write_only": True}}

    def validate(self, attrs):
        password = attrs.get("password")
        password2 = attrs.get("password2")
        if password != password2:
            raise serializers.ValidationError(
                "password and confirm passworrd doesnt match"
            )
        return attrs

    def create(self, validate_data):
        validate_data['role']=User.Roles.STUDENT
        return User.objects.create_user(**validate_data)



class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = User
        fields = ["email", "password"]


# ## making user profile serializer for accessing instance user
class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source = 'user.email',read_only = True)
    
    class Meta:
        model = Profile
        fields = ["id", "email", "name","contact","image"]
        # fields = ['id','email']

# serializeer for User Profile
class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude=('password','is_active','is_admin','role','created_at','updated_at',)


class UserPasswordChangeSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=255, style={"input_type": "password"}, write_only=True
    )
    password2 = serializers.CharField(
        max_length=255, style={"input_type": "password"}, write_only=True
    )

    class Meta:
        model = User
        fields = ["password", "password2"]

    def validate(self, attrs):
        password = attrs.get("password")
        password2 = attrs.get("password2")
        user = self.context.get("user")
        if password != password2:
            raise serializers.ValidationError(
                "password and conformation password does not match"
            )

        user.set_password(password)
        user.save()
        return attrs


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = User
        fields = ["email"]

    def validate(self, attrs):
        email = attrs.get("email")
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            print("encoded UID:", uid)
            token = PasswordResetTokenGenerator().make_token(user)
            print("password reset token:", token)
            link = "http://localhost:3000/api/user/reset/" + uid + "/" + token
            print("password reset link:", link)
             # Construct the reset link
                # sending the mail to the user to change the password
            body = "Click the following link to change the password" +"/"+ link
            data = {
                "subject": "Rest Your Password",
                "body": body,
                "to_email": user.email,
            }
            Util.send_email(data)
            return attrs
        else:
            raise serializers.ValidationError("Your Email not found")

    def get_reset_link(elf,uid,token):
        # Construct the password reset link
            return f"http://localhost:3000/api/user/reset/{uid}/{token}"





class UserPasswordResetSerializer(serializers.Serializer):
    password = serializers.CharField(
        max_length=255, style={"input_type": "password"}, write_only=True
    )
    password2 = serializers.CharField(
        max_length=255, style={"input_type": "password"}, write_only=True
    )

    class Meta:
        model = User
        fields = ["password", "password2"]

    def validate(self, attrs):
        try:
            password = attrs.get("password")
            password2 = attrs.get("password2")
            id = self.context.get("uid")
            token = self.context.get("token")
            print(id)
            if password != password2:
                raise serializers.ValidationError(
                    "password and conformation password does not match"
                )
            id = urlsafe_base64_decode(id)   ##
            user = User.objects.get(id=id)
            if not user:
                raise serializers.ValidationError("User with specified ID does not exist")
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise serializers.ValidationError("Token is not valid or expaired")
            
            user.set_password(password)
            user.save()
            return attrs
        except DjangoUnicodeDecodeError as identifier:
            PasswordResetTokenGenerator().check_token(user, token)
            raise serializers.ValidationError("token is not valid or expaired")