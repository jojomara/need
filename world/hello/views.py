from django.shortcuts import render, redirect # type: ignore
from .forms import KYCForm

def kyc_form(request):
    if request.method == 'POST':
        form = KYCForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Only redirect if form is valid
    else:
        form = KYCForm()# but without passing any data to it

    return render(request, 'kyc/kyc_form.html', {'form': form})  # Ensure this is correctly indented under the else block

def success(request):
    return render(request, 'kyc/success.html')
