def get_user_extra_fields(user, user_profile):
    response_data = {
        "username": user.username,
        "email": user.email,
        "userID": user_profile.userID,
        "current_state": user_profile.current_state,
        "img": user_profile.img,
        "XP": user_profile.XP,
        "lvl": user_profile.lvl
    }
    return response_data

def get_myfriends_detail(UserProfile,UserProfileSerializer,friend_id):
    try:
        # Retrieve the UserProfile for the friend
        friend_profile = UserProfile.objects.get(user=friend_id)
        
        # Serialize the friend's profile
        friend_serializer = UserProfileSerializer(friend_profile)
        
        # Return the serialized friend's profile data
        return friend_serializer.data

    except UserProfile.DoesNotExist:
        # Return a default or error response if the friend's profile is not found
        return {"error": f"Friend profile with ID {friend_id} not found"}

