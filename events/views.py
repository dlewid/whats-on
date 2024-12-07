from django.shortcuts import render
from .models import Event, Review

# Create your views here.
from .forms import ReviewForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect


def index(request):
    event_list = Event.objects.all()
    context = {
        "events": event_list,
    }
    return render(request, 'events/index.html', context)


def reviews(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            print("form was saved")
            return redirect("events:reviews")
    else:
        form = ReviewForm()

    review_list = Review.objects.all()
    # This is done so the stars variable can be an iterable list
    reviews_with_stars = [
        {
            **review.__dict__,
            'star_range': range(review.stars),
            'no_star_range': range(5 - review.stars),
        }
        for review in review_list
    ]
    return render(request, "events/review.html", {"form": form, "reviews": reviews_with_stars})
