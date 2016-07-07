from django.shortcuts import render,redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm,PostForm2
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
me = User.objects.get(username='admin')
# Create your views here.
def post_list(request):
    posts = Post.objects.filter(\
        created_date__lte = timezone.now()
    )\
    .order_by('-created_date')
    #post_form = PostForm()
    post_form = PostForm2()
    return render(request, 'blog/post_list.html', locals())
	# locals() == {'posts':posts,'post_form':post_form}

@csrf_exempt
def add_record2(request):
	if request.POST:
		data = request.POST
		title = data['title']
		text = data['text']
		Post.objects.create(title=title, text=text, author=me)
		return redirect('/blog')

@csrf_exempt
def add_record(request):
	if request.POST:
		form = PostForm2(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = me
			post.save()
		return redirect('/blog')

def post_record(request,key):
	post = Post.objects.get(id = key)
	return render(request, 'blog/post_record.html', locals())