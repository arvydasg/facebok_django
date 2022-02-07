from django.shortcuts import render
from main.models import groups
import time

def test(request):
    # first, we import models into this view.
    # from . models import <model name>
    # then, we create a variable that stores a function from db? Like so.
    all_groups = groups.objects.all().count()
    veganai_groups = groups.objects.filter(group_category='veganai').count()
    dovanos_groups = groups.objects.filter(group_category='dovanos').count()
    mamytes_groups = groups.objects.filter(group_category='mamytes').count()
    vilnius_groups = groups.objects.filter(group_category='vilnius').count()
    kaunas_groups = groups.objects.filter(group_category='kaunas').count()
    
    # then, we put that variable into context variable that can be used in test.html...
    context = {
        'all_groups': all_groups,
        'veganai_groups': veganai_groups,
        'dovanos_groups': dovanos_groups,
        'mamytes_groups': mamytes_groups,
        'vilnius_groups': vilnius_groups,
        'kaunas_groups': kaunas_groups,
    }
    
    items = groups.objects.filter(group_category='Mamytes')
    for item in items.values('group_name', 'group_link', 'group_category'):
        name = item['group_name']
        link = item['group_link']
        category = item['group_category']
        print(name)


    # is returned at the end. Context = context is the key.
    return render(request, 'main/test.html', context=context)
# when that is done, I can then go to html templateview and do {{ context variable }}
# and it prints out on the web! boom.
