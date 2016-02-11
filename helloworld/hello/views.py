from django.views.generic.base import TemplateView

# Create your views here.


class Index(TemplateView):
    template_name = 'hello/index.html'

    def get_context_data(self, **kwrgs):
        context = super(Index, self).get_context_data()
        context['name'] = "Hello Mariano"
        return context
