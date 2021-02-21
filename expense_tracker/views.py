from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone

from .models import Transaction


def index(request):
    transactions = Transaction.objects.all()
    incomes = [transaction.amount for transaction in transactions if transaction.type == 'income']
    expenses = [transaction.amount for transaction in transactions if transaction.type == 'expense']
    total_income = sum(incomes)
    total_expense = sum(expenses)
    remaining_balance = total_income - total_expense

    return render(request, 'expense_tracker/index.html', {'transactions': transactions[:5], 'total_income': total_income,
                                                          'total_expense': total_expense,'remaining_balance': remaining_balance})


def add_transaction(request):
    transaction = Transaction()
    transaction.name = request.POST['transaction_name']
    transaction.amount = float(request.POST['transaction_amount'])
    transaction.type = request.POST['transaction_type']
    transaction.date_added = timezone.now()
    transaction.save()

    return HttpResponseRedirect(reverse('expense_tracker:index'))
