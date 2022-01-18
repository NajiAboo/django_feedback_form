from pyexpat import model
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ReviewForm
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView

from .models import Review
# Create your views here.


class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"
      
    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)
    
    # def post(self,request):
    #     form = ReviewForm(request.POST)
       
    #     if form.is_valid():
    #        form.save()
    #        return HttpResponseRedirect("/thank-you")
       
    #     return render(request,"reviews/review.html",{
    #         "form":form
    #     }) 


# def review(request):
    
#     if request.method == "POST":
#        form = ReviewForm(request.POST)
       
#        if form.is_valid():
#            #print(form.cleaned_data)        
#         #    review = Review(user_name=form.cleaned_data['user_name'], \
#         #        review_text=form.cleaned_data["review_text"], \
#         #         rating=form.cleaned_data['rating'])
           
#            #review.save()
#            form.save()
#            return HttpResponseRedirect("/thank-you")
       
#     else:
#         form = ReviewForm()
    
#     return render(request,"reviews/review.html",{
#             "form":form
#         })   
 
class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!!" 
        return context
    
class ReviewListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"  
    
    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__gt=0)
        return data
    
class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaed_review = self.object
        request = self.request
        
        fav_id = request.session.get("fav_review")        
        context["is_favorite"] = fav_id == str(loaed_review.id)
        return context

class FavoriteView(View):
    def post(self,request):
        review_id = request.POST["review_id"]
        print(review_id)
        fav_review = Review.objects.get(pk=review_id)
        request.session["fav_review"] = review_id
        return HttpResponseRedirect("/reviews/"+review_id)
        
def thank_you(request):
    return render(request, "reviews/thank_you.html")