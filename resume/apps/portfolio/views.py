from django.shortcuts import render, get_object_or_404
from .models import Portfolio, PortfolioCategories


def portfolio_detail(request, page_id=None, **kwargs):
    portfolio = get_object_or_404(Portfolio, id=page_id)
    try:
        prev = get_object_or_404(Portfolio, id=str(int(page_id) - 1))
    except:
        prev = None

    try:
        next = get_object_or_404(Portfolio, id=str(int(page_id) + 1))
    except:
        next = None

    payload = {
        'portfolio': portfolio,
        'next': next,
        'prev': prev
    }
    return render(request, 'portfolio.details.html', payload)
