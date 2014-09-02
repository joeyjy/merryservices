import os
import time
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def index(request):
    if request.method == 'POST':
        post_data = request.POST.copy()
        print post_data
        if post_data['clean_date'] and post_data['clean_time'] and post_data['clean_type']:
            if request.user.id:
                return HttpResponseRedirect(reverse('clean_needs'))
            else:
                return HttpResponseRedirect(reverse('clean_info'))
    os.environ['TZ'] = 'Asia/Shanghai'
    time.tzset()
    default_date = time.strftime('%d %b %Y')
    #default_time = time.strftime('%H:00')
    return render_to_response('home/index.html',
                                  RequestContext(request, locals()))

def clean_info(request):
    pass

    return render_to_response('home/info.html',
                                  RequestContext(request, locals()))

                                  
