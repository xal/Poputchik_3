from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from content.models import Page
from django.template.context import RequestContext
from django.contrib.auth.models import User
from forms import SignUpForm
from models import Profile
from django.contrib.auth.decorators import login_required


def login_user(request, redirect_page=None):
    page = get_object_or_404(Page, slug='login')
    state = None
    if request.POST:
        user = None
        try:
            password = request.POST.get('password')
            user = authenticate(username=request.POST.get('login'), password=password)
        except:
            pass
        if user is not None:
            login(request, user)
            if redirect_page:
                return redirect(redirect_page)
            return redirect('/')
        else:
            state = "Your username and/or password were incorrect."

    return render_to_response('account/login.html', {'page': page, 'state': state}, context_instance=RequestContext(request))


def sign_up(request):
    page = get_object_or_404(Page, slug='sign-up')
    state = None
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        if (form.cleaned_data['password'] == form.cleaned_data['password_check']):
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            try:
                user_name = User.objects.get(username=username) or None
                if user_name is not None:
                    state = 'User with that name already exists.'
                return render_to_response('account/signup.html', {'page': page, 'state': state, 'form': form}, context_instance=RequestContext(request))
            except:
                pass
            try:
                user_email = User.objects.get(email=email) or None
                if user_email is not None:
                    state = 'User with that email already exists.'
                return render_to_response('account/signup.html', {'page': page, 'state': state, 'form': form}, context_instance=RequestContext(request))
            except:
                pass
            user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password'])
            user.is_active = True
            user.save()
            profile = Profile(user=user)
            profile.email = form.cleaned_data['email']
            profile.coord_from = form.cleaned_data['coord_from']
            profile.coord_to = form.cleaned_data['coord_to']
            profile.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                if request.POST.get('to_cart'):
                    return redirect('/cart/')
                return redirect('/')
        else:
            state = "Password's don't match."
    return render_to_response('account/signup.html', {'page': page, 'state': state, 'form': form}, context_instance=RequestContext(request))


#@login_required
#def profile(request):
#    page = {'title': "Profile", 'slug': 'profile'}
#    form = None
#    state = None
#    if request.POST:
#        form = ProfileForm(request.POST or None)
#        if form.is_valid():
#            request.user.email = form.cleaned_data['email']
#            request.user.first_name = form.cleaned_data['first_name']
#            request.user.last_name = form.cleaned_data['last_name']
#            request.user.profile.billing_phone = form.cleaned_data['phone']
#            request.user.profile.billing_address_1 = form.cleaned_data['address_1']
#            request.user.profile.billing_address_2 = form.cleaned_data['address_2']
#            request.user.save()
#            request.user.profile.save()
#            state = 'Profile was changed.'
#    else:
#        try:
#            form = ProfileForm(initial={
#                'email': request.user.email,
#                'first_name': request.user.first_name,
#                'last_name': request.user.last_name,
#                'phone': request.user.profile.phone,
#                'address_1': request.user.profile.address_1,
#                'address_2': request.user.profile.address_2,
#            })
#        except:
#            pass
#    return render_to_response('account/profile.html', {'page': page, 'form': form, 'state': state,}, context_instance=RequestContext(request))
#
#
#@login_required
#def history(request):
#    page = {'title': "Profile", 'slug': 'history'}
#    orders = Order.objects.filter(user=request.user.profile)
#    return render_to_response('account/history.html', {'page': page, 'orders': orders, }, context_instance=RequestContext(request))
