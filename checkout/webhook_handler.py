from django.http import HttpResponse


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        print(f"[Stripe Webhook] Unhandled event: {event['type']}")
        return HttpResponse(
            content=f"Unhandled webhook received: {event['type']}",
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        print(f"[Stripe Webhook] PaymentIntent succeeded: {intent.get('id')}")
        # Here you would locate the order, update status, etc.
        return HttpResponse(
            content=f"Webhook received: {event['type']} - SUCCESS",
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        intent = event.data.object
        print(f"[Stripe Webhook] PaymentIntent failed: {intent.get('id')}")
        return HttpResponse(
            content=f"Webhook received: {event['type']} - FAILED",
            status=200)
