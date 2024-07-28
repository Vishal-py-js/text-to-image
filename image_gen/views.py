from django.http import JsonResponse
from .tasks import async_generator


prompts = ["A red flying dog", "A piano ninja", "A footballer kid"]

def your_view(request):
    arr = []
    for i ,item in enumerate(prompts):
        imgdata = async_generator(item)
        arr.append({"name": f"converted{i}.png", "image":imgdata})
   
    # creating images and saving it to the root folder
    for i, img in enumerate(arr):
        with open(img["name"], "wb") as f:
            f.write(img["image"])
    return JsonResponse({"data": "Success"})
