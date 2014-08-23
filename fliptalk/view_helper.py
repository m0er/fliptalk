import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse

class JsonResponse(HttpResponse):
    """
    An HTTP response class that consumes data to be serialized to JSON.

    :param data: Data to be dumped into json. By default only ``dict`` objects
      are allowed to be passed due to a security flaw before EcmaScript 5. See
      the ``safe`` parameter for more information.
    :param encoder: Should be an json encoder class. Defaults to
      ``django.core.serializers.json.DjangoJSONEncoder``.
    :param safe: Controls if only ``dict`` objects may be serialized. Defaults
      to ``True``.
    """

    def __init__(self, data={}, encoder=DjangoJSONEncoder, safe=True, **kwargs):
        if safe and not isinstance(data, dict):
            raise TypeError('In order to allow non-dict objects to be '
                'serialized set the safe parameter to False')
        kwargs.setdefault('content_type', 'application/json; charset=UTF-8')

        data = json.dumps(data, cls=encoder, ensure_ascii=False)
        super(JsonResponse, self).__init__(content=data, **kwargs)


class JsonResponseError(JsonResponse):
    status_code = None

    def __init__(self, data, encoder=DjangoJSONEncoder, safe=True, **kwargs):

        self.status_code = data.get('code', 500)
        super(JsonResponseError, self).__init__(data, encoder, safe, **kwargs)

class JsonCORSResponse(JsonResponse):
    def __init__(self, data, encoder=DjangoJSONEncoder, safe=True, **kwargs):
        super(JsonCORSResponse, self).__init__(data, encoder, safe, **kwargs)
        self['Access-Control-Allow-Origin'] = '*'
        self['Access-Control-Allow-Credentials'] = 'true'

