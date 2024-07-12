from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt


current_status = "UNKNOWN"

def get_response(result, data):
    return JsonResponse({"result": result, "data": data})

@csrf_exempt
@require_POST
def login_view(request):
    global current_status
    if request.method == 'POST':
        current_status = "LOGIN"
        return get_response("0", current_status)
    return get_response("1", "發送命令失敗")

@csrf_exempt
@require_POST
def start_view(request):
    global current_status
    if request.method == 'POST':
        current_status = "START"
        return get_response("0", current_status)
    return get_response("1", "發送命令失敗")

@csrf_exempt
@require_POST
def stop_view(request):
    global current_status
    if request.method == 'POST':
        current_status = "STOP"
        return get_response("0", current_status)
    return get_response("1", "發送命令失敗")

@require_GET
def status_view(request):
    global current_status
    if request.method == 'GET':
        return get_response("0", current_status)
    return get_response("1", "發送命令失敗")
