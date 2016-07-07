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
'''
def post_record(request,key):
    posts = Post.objects.filter(id__gte=key)[:2]
    post = posts[0]
    next_post = posts[1]
    return render(request, 'blog/post_record.html', locals())

# not that correct but works
def post_record(request,key):
    posts = Post.objects.filter(id__gte=key)
    post = posts[0]
    try:
        next_post = posts[1]
    except IndexError:
        next_post = post
    return render(request, 'blog/post_record.html', locals())
'''
'''
# correct but little slower
def post_record(request,key):
    posts = Post.objects.filter(id__gte=key)[:2]
    post = posts[0]
    post_max = Post.objects.order_by('id').last() 
    id_max = post_max.id
    if post.id == id_max:
        next_post = post
    else:
        next_post = posts[1]
    return render(request, 'blog/post_record.html', locals())
'''

# correct
def post_record(request,key):
    posts = Post.objects.filter(id__gte=key)[:2]
    if len(posts) == 1:
       post = posts[0]
       next_post = post
    else:
       post = posts[0]
       next_post = posts[1]
    return render(request, 'blog/post_record.html', locals())

@csrf_exempt
def delete_record(request,id):
    if request.method == 'POST':
    #if request.POST:
        Post.objects.filter(id = id).delete()
        return redirect('/blog')
    else:
        return render(request,'404.html')
