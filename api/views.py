import stripe
from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect
from django.views import View
from django.views.generic import TemplateView

from .models import Item, Price


stripe.api_key = settings.STRIPE_SECRET_KEY


class BuyItemSessionView(View):
    def post(self, request, *args, **kwargs):
        price = Price.objects.get(id=self.kwargs["pk"])
        DOMAIN = "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': price.stripe_price_id,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=DOMAIN + '/success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=DOMAIN + '/cancel/',
        )
        return redirect(checkout_session.url)


class SuccessView(TemplateView):
    template_name = "success.html"

    def get(self, request):
        query = self.request.GET.get('session_id')
        context = {'session_id': query}
        return render(request, self.template_name, context)


class CancelView(TemplateView):
    template_name = "cancel.html"


class ItemDetailPageView(TemplateView):
    template_name = "item_detail.html"

    def get_context_data(self, item_id, **kwargs):
        product = Item.objects.get(id=item_id)
        prices = Price.objects.filter(product=product)
        context = super(ItemDetailPageView, self).get_context_data(**kwargs)
        context.update({
            "product": product,
            "prices": prices
        })
        return context






