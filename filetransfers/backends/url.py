from django.http import HttpResponseRedirect
from django.utils.encoding import smart_str

def serve_file(request, file, save_as, content_type):
    return HttpResponseRedirect(smart_str(file.url))
