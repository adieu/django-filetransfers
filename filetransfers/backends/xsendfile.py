from django.http import HttpResponse
from django.utils.encoding import smart_str

def serve_xsendfile(request, file, save_as, content_type):
    response = HttpResponse(ChunkedFile(file), content_type=content_type)
    response['X-Sendfile'] = file.path
    if save_as:
        response['Content-Disposition'] = smart_str(u'attachment; filename=%s' % save_as)
    if file.size is not None:
        response['Content-Length'] = file.size
    return response
