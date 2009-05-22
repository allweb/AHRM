#####################################################################
# Project:    A*HRM
# Title:     Experience controller 
# Version:     0001
# Last-Modified:     2009-02-26 05:36:39  (Thu, 26 April 2009)        
# Author:     Sokha, Sin , Sanya, Mesa , Kanel (ALLWEB DEVELOPERS) 
# Status:     Active
# Type:     Process
# Created:     03-April-2009
# Post-History:     20-April-2009
######################################################################
from employees_controller import employee_tabs
from libs import *

@login_required
def experience_save(request,experience_id,process=""):
    data = initialize_view(request)
    if request.method == "POST" and request.POST.has_key('experience_save'):
        emp = Employee.objects.get(id = request.session['emp_id'])
        if experience_id !=0:
            experience = Experience.objects.get(id = experience_id)
        else:
            experience = Experience(employee = emp)
        form = forms.ExperienceForm(request.POST, instance = experience)
        if form.is_valid():
            form.save()
            process = ""
    else:
        if experience_id !=0:
            experience = Experience.objects.get(id = experience_id)
            form = forms.ExperienceForm(instance = experience)
        else:
            form = forms.ExperienceForm()
            
    experiences = Experience.objects.all()
    experiences = experiences.filter(employee=request.session['emp_id'])
    data['emp_tab'] = employee_tabs(request.session['emp_id'])        
    data['emp_id']=request.session['emp_id']
    data['tab_id']='experience'
    data['experience_id']=experience_id
    data['form']=form
    data['process']=process
    data['experience_list']=experiences
    data['curr_employee'] = Employee.objects.get(id=request.session['emp_id'])
    return render_to_response('employees/employee_main.html', data)    

def experience_edit(request,exp_id):
    return experience_save(request,exp_id,"edit")

def experience_new(request):
    return experience_save(request,0,"new")
  
@login_required
def experience_delete(request, exp_id):
    data = initialize_view(request)
    experience = Experience.objects.get(id=exp_id)
    experience.delete()
    return employee_experience(request)

