from django.views.generic import TemplateView
from lib.owmapi.owm import OWM


class IndexView(TemplateView):
    template_name = 'website/index.html'
    extra_context = {
        'erro_message': False,
        'lang': 'en',
        'city': 'Ribeirão Preto',
    }

    def get(self, request, *args, **kwargs):
        try:
            self.extra_context.update(
                lang=request.GET.get('lang') or self.extra_context.get('lang'),
                city=request.GET.get('city') or self.extra_context.get('city')
            )
            owm = OWM(appid='c0c4a4b4047b97ebc5948ac9c48c0559', language=self.extra_context.get('lang'))
            data = owm.forecast_at_place(self.extra_context.get('city'))
            self.extra_context.update(data=data)
        except Exception as e:
            self.extra_context.update(erro_message=f'{e}')
        return super().get(request, args, kwargs)
