from django.views import generic


class HomePage(generic.TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(HomePage, self).get_context_data(**kwargs)
        context['home'] = 'active'
        return context

