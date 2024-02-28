from celery import shared_task

from vehicle.models import Car, Moto


@shared_task
def check_milage(pk, model):
    if model == 'Car':
        instance = Car.objects.filter(pk=pk).first()
    else:
        instance = Moto.objects.filter(pk=pk).first()

    if instance:
        previous_milage = -1
        for m in instance.milage.all():
            if previous_milage == -1:
                previous_milage = m.milage

            else:
                if previous_milage < m.milage:
                    print('неверный пробег')
                    break


def check_filter():
    filter_price = {'price__lte': 500}

    if Car.objects.filter(**filter_price).exists():
        print('Найдены автомобили с ценой до 500')
        # send_email(
        #     subject='Отчет по фильтру',
        #     message='Найдены автомобили с ценой до 500',
        #     from_email='mysite@example.com',
        #     recipient_list=['user@example.com']
        # )
