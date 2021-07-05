from django.shortcuts import render, redirect
from .models import Job, Category, Contact
from django.core.paginator import Paginator
from .form import ApplyForm, JobForm, ContactForm
from django.urls import reverse
from accounts.models import Profile

# Create your views here.
def job_list(request):
    job_list = Job.objects.all()
    paginator = Paginator(job_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'jobs':page_obj}
    return render(request, 'job/job_list.html', context)


def job_detail(request, slug):
    job_detail = Job.objects.get(slug=slug)
    number = Profile.objects.all()
    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_detail
            myform.save()
    else:
        form = ApplyForm()
        
    context = {'job':job_detail, 'form':form, 'number':number}
    return render(request, 'job/job_detail.html', context)

def add_job(request):
    if request.method == 'POST':
        form2 = JobForm(request.POST, request.FILES)
        if form2.is_valid():
            myform = form2.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect(reverse('jobs:job_list'))
    else:
        form2 = JobForm()
    return render(request, 'job/add_job.html', {'form2':form2})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../')
    else:
        form = ContactForm()
    return render(request, 'job/contact.html', {'form':form})
