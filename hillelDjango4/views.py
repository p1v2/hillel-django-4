from django.http import HttpResponse
from hillelDjango4.tasks import hello_world_task


def hello_world(request):
    # random_time = random() * 10  # 0-10 seconds
    #
    # sleep(random_time)
    name = request.GET.get('name', 'World')

    # Apply async in 3 seconds
    hello_world_task.delay(name)

    return HttpResponse('Hello, World!')
