from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from ptsessions.models import PtSessions


def basket_contents(request):

    basket_items = []
    total = 0
    session_count = 0
    basket = request.session.get('basket', {})

    for session_id, session_data in basket.items():
        if isinstance(session_data, int):
            session = get_object_or_404(PtSessions, id=id)
            total += session_data * PtSessions.item_price
            product_count += session_data
            basket_items.append({
                'session_id': session_id,
                'quantity': session_data,
                'session': session,
            })
        else:
            product = get_object_or_404(PtSessions, id=id)
            for quantity in session_data.items():
                total += quantity * product.price
                product_count += quantity
                basket_items.append({
                    'session_id': session_id,
                    'quantity': session_data,
                    'session': session,
                })

        grand_total = total

        content = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
    }
        return content