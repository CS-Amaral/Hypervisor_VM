from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from app.controller.recoverVmsCmd import Get_vms
from app.controller.vboxmanager_commands import Change_vm

@app.route('/')
@app.route('/index')
def index():
    
    return render_template('index.html', title='Home')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    #get_vm = Get_vms()

    if form.validate_on_submit():
        setVM= Change_vm(form.so.data,form.cpu.data,form.memoria.data,form.ip.data)
        #print(form.so.data)
        #######k = get_vm.recoverVMS() ||| Login requested for user {}, remember_me={}
        setVM.clonarVm()
        if form.so.data == '0':
            soname = "Windows"
        else: 
            sosoname = "Linux"
        flash('Sua VM: ' + soname + ' foi clonada e esta pronta para ser executada')
        #flash('CPU: cpu{}, Memoria: memoria{}, IP: ip{}, SO: {} '.format(
        #    form.cpu.data, form.memoria.data, form.ip.data, form.so.data))
        return redirect('/index')
    
    return render_template('login.html', title='Sign In', form=form)