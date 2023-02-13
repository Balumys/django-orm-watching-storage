from datacenter.models import Visit
from django.shortcuts import render
from datacenter.models import format_duration


def storage_information_view(request):
    visits_to_vault = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visit in visits_to_vault:
        non_closed_visits.append(
            {
                'who_entered': visit.passcard,
                'entered_at': visit.entered_at,
                'duration': format_duration(visit.get_duration()),
            }
        )
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
