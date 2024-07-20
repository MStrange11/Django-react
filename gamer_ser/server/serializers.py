from django.contrib.auth.models import User

from rest_framework import serializers

from .models import UserProfile,uidg

class UserProfileSerializer(serializers.ModelSerializer):
    friends = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all(), many=True, required=False)
    class Meta:
        model = UserProfile
        # fields = ['user','current_state', 'img', 'XP', 'lvl']
        fields = '__all__'

    def validate_friends(self, value):
        if any(f not in UserProfile.objects.all() for f in value):
            raise serializers.ValidationError("One or more friends do not exist.")
        return value
    
    # def validate_XP(self, value):
    #     if value.xp < 0:  
    #         raise serializers.ValidationError("xp connot be negitive.")
    #     return value
    
    # def get_user(self, obj):
    #     # Assuming `user` is a ForeignKey to the User model
    #     return obj.user.id  # or use obj.user.username or obj.user.email as needed

class UserSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['username', 'email', 'profile']

    def get_profile(self, obj):
        profile = UserProfile.objects.filter(user=obj).first()
        return UserProfileSerializer(profile).data if profile else None

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

class RegisterSerializer(serializers.ModelSerializer):
    # userID = serializers.CharField(default=str(uidg()), read_only=True)
    # current_state = serializers.CharField(default='ideal')
    # img = serializers.CharField(default='https://cdn-icons-png.flaticon.com/512/5281/5281619.png')
    # password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        # fields = ['username', 'email', 'password', 'userID', 'current_state', 'img']
        fields = ['username', 'email', 'password']

    def validate(self, data):
        if User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError("Username is already taken!")
        
        if data.get("email") is None:
            err = {"email": "This field is required."}
            raise serializers.ValidationError(err)
        
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError("Email address is already registered")
            
        return data

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'], email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        UserProfile.objects.create(user=user)
        return user
