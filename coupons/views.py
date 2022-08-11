from django.shortcuts import redirect
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.db.models import F
from .models import Coupon
from orders.models import Order
from cart.cart import Cart
from .forms import CouponApplyForm
from django.contrib import messages


@require_POST
def coupon_apply(request):
    # current_user  = request.session.id
    now = timezone.now()
    form = CouponApplyForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        coupon = Coupon.objects.filter(code__iexact=code, valid_from__lte=now, valid_to__gte=now, active=True).exclude(max_value__lte=F('used')).first()
        if not coupon:
            messages.error(request, 'You can\'t use same coupon again, or coupon does not exist')
            return redirect('cart:cart_summary')
        try:
            coupon.used += 1
            coupon.save()
            request.session['coupon_id'] = coupon.id
        except Coupon.DoesNotExist:
                request.session['coupon_id'] = None
    return redirect('cart:cart_summary')