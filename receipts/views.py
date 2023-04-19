from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from receipts.models import Receipt


# Create your views here.
@login_required
def receipt_list(request):
    receipts = Receipt.objects.filter(purchaser=request.user)
    context = {"receipts": receipts}
    return render(request, "receipts/receipt_list.html", context)
