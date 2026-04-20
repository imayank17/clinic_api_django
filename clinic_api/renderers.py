from rest_framework.renderers import JSONRenderer

class CustomRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        status_code = renderer_context['response'].status_code
        success = 200 <= status_code < 300
        
        response = {
            "success": success,
            "data": data if success else None,
            "error": data if not success else None
        }
        
        return super().render(response, accepted_media_type, renderer_context)
