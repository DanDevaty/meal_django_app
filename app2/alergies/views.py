# views.py
from django.shortcuts import render, redirect
from .models import Allergy
from users.forms import ProfileForm
from django.contrib.auth.decorators import login_required
from users.models import CustomUser

@login_required
def edit_user_profile(request):
    user_profile = CustomUser.objects.get(user=request.user)
    allergy_choices = Allergy.ListOfAllergies

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()

        # Delete allergy
        if 'delete_allergy' in request.POST:
            allergy_id = request.POST.get('delete_allergy')
            user_profile.allergies.remove(allergy_id)

        # Add allergy
        elif 'add_allergy' in request.POST:
            name = request.POST.get('name', '').strip()
            custom = request.POST.get('addDifAllergies', '').strip()

            if name or custom:
                allergy, created = Allergy.objects.get_or_create(
                    name=name or custom,
                    defaults={'addDifAllergies': custom}
                )
                user_profile.allergies.add(allergy)

        return redirect('edit_user_profile')  # Replace with your actual URL name

    else:
        form = ProfileForm(instance=user_profile)

    return render(request, 'index.html', {
        'form': form,
        'user': request.user,
        'allergy_choices': allergy_choices,  # ✅ This is the list for the dropdown
    })
