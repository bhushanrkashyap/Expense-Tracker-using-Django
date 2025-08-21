from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, redirect
from .models import *
from django.contrib import messages

def index(request):
    if request.method == "POST":
        description = request.POST.get('description')
        amount = request.POST.get('amount')

        current_balance, _ = Balance.objects.get_or_create(id=1)
        expense_type = "CREDIT"
        if float(amount) < 0:
            expense_type = "DEBIT"

        if float(amount) == 0:
            messages.success(request, "Amount cannot be zero")
            return redirect('/')

        tracking_history = TrackingHistory.objects.create(
            amount=float(amount),
            expense_type=expense_type,
            current_balance=current_balance,
            description=description
        )
        current_balance.current_balance += float(tracking_history.amount)
        current_balance.save()

        print(description, amount)
        return redirect('/')

    current_balance, _ = Balance.objects.get_or_create(id=1)

    income = 0.0
    expense = 0.0

    for tracking_history in TrackingHistory.objects.all():
        if tracking_history.expense_type == "CREDIT":
            income += float(tracking_history.amount)
        else:
            expense += float(tracking_history.amount)

    context = {
        'income': income,
        'expense': expense,
        'transactions': TrackingHistory.objects.all(),
        'current_balance': current_balance,
    }
    return render(request, 'index.html', context)
def delete_transaction(request, transaction_id):
    transaction = get_object_or_404(TrackingHistory, id=transaction_id)
    current_balance = transaction.current_balance
    if transaction.expense_type == 'CREDIT':
        current_balance.current_balance -= transaction.amount
    else:
        current_balance.current_balance -= transaction.amount

    current_balance.save()
    transaction.delete()
    return redirect('/')