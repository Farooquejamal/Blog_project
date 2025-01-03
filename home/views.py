from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import BlogModel,Category,Comment
from .forms import PostForm,UpdateForm,CommentForm
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect
# Create your views here.

# def home(request):
#     return render(request,'home.html',{})

def LikeView(request,pk):
    post = get_object_or_404(BlogModel, pk=pk)
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article-detail',args = [str(pk)]))

class HomeView(ListView):
    model = BlogModel
    template_name = 'home.html'
    ordering = ['-updated_at']

    def get_context_data(self,*args,**kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView,self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context

def CategoryView(request,cats):
    category_name = cats.replace('-', ' ')
    category_posts = BlogModel.objects.filter(category__iexact=category_name)
    return render(request,'categories.html',{'cats':cats.title().replace('-',' '),'category_posts':category_posts})

def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request,'category_list.html',{'cat_menu_list':cat_menu_list})

class DetailView(DetailView):
    model = BlogModel
    template_name = 'article_details.html'

    def get_context_data(self,*args,**kwargs):
        cat_menu = Category.objects.all()
        context = super(DetailView,self).get_context_data(*args,**kwargs)

        stuff = get_object_or_404(BlogModel, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context['liked'] = liked
        return context

class AddPostView(CreateView):
    model = BlogModel
    form_class = PostForm
    template_name = "add_post.html"
    # fields = ['title','title_tag','content','slug','image']
    # def form_valid(self, form):
    #     form.instance.author = self.request.user  # Set the author to the current user
    #     return super().form_valid(form)

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "add_comment.html"
    # fields = '__all__'
    def form_valid(self,form):
        form.instance.post_id = self.kwargs['pk']
        response =  super().form_valid(form)
        return response
    success_url = reverse_lazy('home')

class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields ='__all__'

class UpdatePostView(UpdateView):
    model = BlogModel
    form_class = UpdateForm
    template_name = 'update_post.html'
    # fields = ['title','title_tag','content','image']

class DeletePostView(DeleteView):
    model = BlogModel
    template_name = 'delete.html'
    success_url = reverse_lazy('home')

