from django.http import HttpResponse
from django.utils.encoding import smart_str

def prepare_upload(request, url):
    return url

def serve_file(request, file, save_as, content_type):
    response = HttpResponse(ChunkedFile(file), content_type=content_type)
    if save_as:
        response['Content-Disposition'] = smart_str(u'attachment; filename=%s' % save_as)
    if file.size is not None:
        response['Content-Length'] = file.size
    return response

class ChunkedFile(object):
    def __init__(self, file):
        self.file = file

    def __iter__(self):
        return self.file.chunks()
