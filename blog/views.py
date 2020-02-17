from django.shortcuts import render,redirect,get_object_or_404
from .models import Article,Comment
from django.http import Http404,HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from .forms import CommentForm

# Create your views here.
def leave_comment(request,article_id):
	if request.method == "POST":
		form = CommentForm()
		if form.is_valid():
			post = form.save(commit=False)
			post.date = timezone.now()
			post.save()
			return redirect('blog/details.html', pk=article_id)
	else:
		form = PostForm()
	return render(request, 'blog/details.html', {'form': form})


	# article = Article.objects.get(id=article_id)
 #    if request.method == "POST":
 #        form = CommentForm(request.POST)
 #        if form.is_valid():
 #        	article.comment_set.create(text=form.cleaned_data['text'],date= timezone.now())
 #            return render(request,'details',{'comments':Comment.objects.filter(article =article_id)})
 #    else:
 #        form = CommentForm()
 #    return render(request, 'details.html', {'form': form})

def blog(request):
	last_articles = Article.objects.order_by('-date')[:5]
	return render(request,'blog.html',context = {'articles':last_articles})


def detail(request, article_id):
	try:
		a = Article.objects.get(id =article_id)
	except:
		raise Http404('Not found')
	return render(request,'details.html',{"article":a})


def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request,user)
			messages.success(request,'You successfully registered!!!')
			return redirect('articles:blog')
		else:
			for err in form.error_messages:
				messages.error(request,f'{err}:{form.error_messages[err]}')
			return render(request,'register.html',{'form':form})

	form = UserCreationForm
	return render(request,'register.html',{'form':form})


def logout_request(request):
	logout(request)
	messages.success(request,'Bye!')
	return redirect('articles:blog')

	
def login_request(request):
	if request.method == 'POST':
		form = AuthenticationForm(request,request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username = username,password = password)
			if user is not None:
				login(request,user)
				messages.success(request,f'You are now logged in as {username}')
				return redirect('/')
			else:
				messages.error(request,f'Something went wrong')
		else:
			messages.error(request,f'Something went wrong')
	form = AuthenticationForm
	return render(request, 'login.html',{'form':form})
