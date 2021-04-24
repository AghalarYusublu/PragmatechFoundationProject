import data


def DataSave(name, surname, salary):
    worker = {
        'ad': name,
        'soyad': surname,
        'maas': salary
    }
    data.Workers.append(worker)
