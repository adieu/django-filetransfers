from django.conf import settings
from django.utils.importlib import import_module
import mimetypes

UPLOAD_BACKEND = getattr(settings, 'FILETRANSFERS_UPLOAD_BACKEND',
                         'filetransfers.backends.default.prepare_upload')
DOWNLOAD_BACKEND = getattr(settings, 'FILETRANSFERS_DOWNLOAD_BACKEND',
                           'filetransfers.backends.default.serve_file')

_backends_cache = {}

# Public API
def prepare_upload(request, url, backend=None):
    # TODO: Support specifying maxmium file upload size and other constraints?
    # Probably can't be done for all backends, so maybe the developer should
    # always check these constraints after the upload?
    handler = _load_backend(backend, UPLOAD_BACKEND)
    result = handler(request, url)
    if isinstance(result, (tuple, list)):
        return result
    return result, {}

def serve_file(request, file, backend=None, save_as=False, content_type=None):
    # Backends are responsible for handling range requests.
    handler = _load_backend(backend, DOWNLOAD_BACKEND)
    filename = file.name.rsplit('/')[-1]
    if save_as is True:
        save_as = filename
    if not content_type:
        content_type = mimetypes.guess_type(filename)[0]
    return handler(request, file, save_as=save_as, content_type=content_type)

# Internal utilities
def _load_backend(backend, default_backend):
    if backend is None:
        backend = default_backend
    if backend not in _backends_cache:
        module_name, func_name = backend.rsplit('.', 1)
        _backends_cache[backend] = getattr(import_module(module_name), func_name)
    return _backends_cache[backend]
