from decimal import Decimal
from django.shortcuts import get_object_or_404
from ptsessions.models import PtSessions

def basket_contents(request):
    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})

    for session_id, session_data in basket.items():
        if isinstance(session_data, int) and session_data > 0:  # Ensure quantity is positive
            session = get_object_or_404(PtSessions, id=session_id)
            total += session_data * session.item_price
            product_count += session_data
            basket_items.append({
                'session_id': session_id,
                'quantity': session_data,
                'session': session,
                'price': session.item_price
            })
        elif isinstance(session_data, dict):
            product = get_object_or_404(PtSessions, id=session_id)
            for product_id, quantity in session_data.items():
                if quantity > 0:
                    total += quantity * product.price
                    product_count += quantity
                    basket_items.append({
                        'session_id': session_id,
                        'quantity': quantity,
                        'session': product,
                    })

    grand_total = total

    content = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
    }
    return content
