from account.models import User


def user_type(request):
    user = request.user
    if user.is_authenticated:
        the_user = User.objects.get(username=user.username)
        if the_user.type_of_user == '1':
            job_seeker = True
        else:
            job_seeker = False
        return {
            'job_seeker': job_seeker,
        }
    else:
        return {}
