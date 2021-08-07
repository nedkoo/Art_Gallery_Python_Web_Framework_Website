from django.core.exceptions import PermissionDenied

from art_gallery_web.gallery_app.models import Arts


def user_is_entry_author(function):
    def wrapper(request, *args, **kwargs):
        art = Arts.objects.get(pk=kwargs['pk'])
        if art.created_by == request.user:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrapper
