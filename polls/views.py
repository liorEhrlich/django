from django.http import HttpResponse,JsonResponse

list_a = ['blue','red','green']

def index(request):
    return HttpResponse("Welcome to colors app")

def list(request):
    return JsonResponse(list_a, safe=False)

def add(request):
    if request.GET.get('color') not in list_a:
        list_a.append(request.GET.get('color'))
        return JsonResponse({"msg": 'Added!!'},status=201)
    else:
        return JsonResponse({"msg": 'Already there....'},status=409)

def get(request):
    if request.GET.get('color') not in list_a:
        return HttpResponse("No such color",status=404)
    else:
        return HttpResponse(request.GET.get('color'),status=201)
