
        if request["type"] == "INVALID_METHOD":
            return self._response_invalid_method(request)
        if request["type"] == "UNSUPPORTED_MEDIA_TYPE":
            return self._response_unsupported_media_type(request)
        if request["type"] == "UNSUPPORTED_MEDIA_TYPE_FORMAT":
            return self._response_unsupported_media_type_format(request)
        if request["type"] == "UNSUPPORTED_MEDIA_TYPE_IMAGE":
            return self._response_unsupported_media_type_image(request)
        if request["type"] == "UN