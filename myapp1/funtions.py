def handle_uploaded_file(f, fr):
    if fr == 'seller':
        with open('myapp1/static/image/upload/seller/'+f.name, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
    else:
        with open('myapp1/static/image/upload/shop/'+f.name, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)