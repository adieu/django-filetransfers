from django.conf import settings

from filetransfers.api import prepare_upload as delegate

def prepare_upload(*args, **kwargs):
    """Delegates uploads to other backends based on private=False or True"""
    if kwargs['private']:
        kwargs['backend'] = settings.DELEGATE_PRIVATE_UPLOADS
    else:
        kwargs['backend'] = settings.DELEGATE_PUBLIC_UPLOADS
    return delegate(*args, **kwargs)
