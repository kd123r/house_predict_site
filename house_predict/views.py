from django.shortcuts import render
from .forms import ModelForm, SquareFeetForm, BedroomsForm, BathroomsForm, NeighborhoodForm
import pickle

def predict_model(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print(request.POST)
        if request.POST.__contains__('neighborhood'):
            form = ModelForm(request.POST)
            if form.is_valid():
                squarefeet = form.cleaned_data['squarefeet']
                bedrooms = form.cleaned_data['bedrooms']
                bathrooms = form.cleaned_data['bathrooms']
                neighborhood = form.cleaned_data['neighborhood']
                model_features = []
                if neighborhood == 0:
                    model_features.append([squarefeet, bedrooms, bathrooms, 1, 0, 0])
                elif neighborhood == 1:
                    model_features.append([squarefeet, bedrooms, bathrooms, 0, 1, 0])
                else:
                    model_features.append([squarefeet, bedrooms, bathrooms, 0, 0, 1])
                loaded_model = pickle.load(
                    open("ml_model/house_predict_model.pkl", 'rb'))
                prediction = loaded_model.predict(model_features)[0]
                return render(request, 'home.html', {'form': form, 'prediction': prediction, 'show': True})
        elif request.POST.__contains__('bathrooms'):
            form = NeighborhoodForm(request.POST)
            if form.is_valid():
                return render(request, 'home.html', {'form': form})
        elif request.POST.__contains__('bedrooms'):
            form = BathroomsForm(request.POST)
            if form.is_valid():
                return render(request, 'home.html', {'form': form})
        elif request.POST.__contains__('squarefeet'):
            form = BedroomsForm(request.POST)
            if form.is_valid():
                return render(request, 'home.html', {'form': form})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = SquareFeetForm()

    return render(request, 'home.html', {'form': form})