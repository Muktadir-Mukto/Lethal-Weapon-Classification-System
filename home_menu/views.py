from django.shortcuts import render, redirect
# from .forms import UploadFile
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.core.files.storage import FileSystemStorage
from keras.preprocessing import image
import matplotlib.pyplot as plt
from skimage.io import imread
from skimage.transform import resize
from keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt
from django.contrib import messages

class index(TemplateView):
    template_name = 'index.html'


# def upload(request):
#     if request.method == 'POST':
#         # form = UploadFile(request.Post, request.FILES)
#         uploaded_file = request.FILES['image']
#         print(uploaded_file.name)
#         print(uploaded_file.size)
#     # return redirect(request, 'index.html')
#     return render(request, 'index.html')

def upload(request):
    context ={}

    # context1 = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['image']
        print(uploaded_file.name)
        print(uploaded_file.size)
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)





        categories = ['Grenade', 'Knife', 'Machine Guns', 'Pistol Hand Guns', 'RPG']

        img = imread("C:/Lethal-Weapon-Classification-System/Lethal-Weapon-Classification-System/media/"+name)
        img_resize = resize(img, (224, 224, 3))
        img = np.asarray(img_resize)
        # plt.imshow(img)
        # plt.show()
        img = np.expand_dims(img, axis=0)
        saved_model = load_model("C:/Lethal-Weapon-Classification-System/Lethal-Weapon-Classification-System/Static/CSE438_Model/model_vgg16.h5")
        # saved_model = load_model("../CSE438_Model/model_vgg16.h5")

        categories_predict = saved_model.predict(img)
        # context1['mes'] = categories[np.argmax(categories_predict[0])]

        mes = (categories[np.argmax(categories_predict[0])])
        print(mes)
        messages.success(request, mes)
        print("\n\n\n\n\n\n")
        print("\nThe predicted image is :", categories[np.argmax(categories_predict[0])])
        print("\n\n\n\n\n\n")
    return render(request, 'upload.html', context)