from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import BlogPost, Category
from apps.core.models import CompanyInfo

def blog_list(request, category_slug=None):
    if not category_slug:
        category_slug = request.GET.get('category')
    posts = BlogPost.objects.filter(is_published=True)
    current_category = None
    
    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        posts = posts.filter(category=current_category)
        
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    categories = Category.objects.all()
    
    context = {
        'posts': page_obj,
        'page_obj': page_obj,
        'categories': categories,
        'current_category': current_category,
        'page_title': 'Blog & Actualités',
        'company': CompanyInfo.get_instance(),
    }
    return render(request, 'blog/blog_list.html', context)

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, is_published=True)
    related_posts = BlogPost.objects.filter(category=post.category, is_published=True).exclude(id=post.id)[:3]
    
    context = {
        'post': post,
        'related_posts': related_posts,
        'page_title': post.title,
        'company': CompanyInfo.get_instance(),
    }
    return render(request, 'blog/blog_detail.html', context)
