


def handle_uploaded_file(f, name):
    with open(name + '.png', 'w') as destination:
        for chunk in f.chunks():
            destination.write(chunk)