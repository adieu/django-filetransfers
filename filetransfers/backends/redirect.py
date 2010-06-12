from django.conf import settings
from django.http import HttpResponseRedirect
from django.utils.encoding import smart_str

def serve_file(request, file, save_as, content_type):
    """
    Redirects downloads to a handler at settings.FILETRANSFERS_BASE_REDIRECT_URL
    """
    return HttpResponseRedirect(smart_str(
        settings.FILETRANSFERS_BASE_REDIRECT_URL + file.name))
