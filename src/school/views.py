from django.shortcuts import render

from school.models import Group, Student


# Create your views here.
def show_gr(request):
    group_dict = Group.objects.all()
    return render(request, 'gr_show.html', context={"gr": group_dict})


def stud_of_gr(request, grid):
    gr = Group.objects.get(id=grid)
    studs = Student.objects.filter(group_id=grid)
    return render(request, 'std_in_gr_show.html', context={"std": studs, "gr_name": gr.name})
