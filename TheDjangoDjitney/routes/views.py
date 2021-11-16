from django.shortcuts import render
from .models import Line, Station, Stop
from .forms import  StopForm, LineForm, StationForm
# Add your imports below:
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
class HomeView(TemplateView):
  template_name = "routes/home.html"

  def get_context_data(self):
    context = super().get_context_data()
    context["lines"] = Line.objects.all()
    context["stations"] = Station.objects.all()
    context["stops"] = Stop.objects.all()
    return context

class LineView(ListView):
  model = Line
  template_name = "routes/lines.html"

class CreateLineView(CreateView):
  model = Line
  form_class = LineForm
  template_name = "routes/add_line.html"

class UpdateLineView(UpdateView):
  model = Line
  form_class = LineForm
  template_name = "routes/update_line.html"

class DeleteLineView(DeleteView):
  model = Line
  success_url = "/lines"
  template_name = "routes/delete_line.html"
