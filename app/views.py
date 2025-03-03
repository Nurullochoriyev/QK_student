
from .models import *

from .utils import *

from django.shortcuts import render, redirect
from .forms import FanForm, StudentForm
from .models import Student


def index(request):
    data=Fan.objects.all()
    data1=Student.objects.all()
    return render(request,'index.html',{'db':data,'dc':data1})





def add_fan(request):
    if request.method == 'POST':
        form = FanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FanForm()
    return render(request, 'add_fan.html', {'form': form})

def add_student(request):
    qr_code = generate_qr_code("https://t.me/najottalim")
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('home')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form,'form1':qr_code})


import qrcode
from PIL import Image
from io import BytesIO
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def generate_pdf(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{student.familya}.pdf"'

    # 🟢 1️⃣ QR kod yaratish
    qr_data = f"https://t.me/najottalim/{student.id}"  # Student ID asosida link yaratamiz
    qr = qrcode.make(qr_data)  # QR kod yaratish (PIL.Image)

    # QR kodni xotiraga saqlash
    qr_io = BytesIO()
    qr.save(qr_io, format="PNG")  # PNG formatida saqlash
    qr_io.seek(0)  # Faylni boshiga qaytarish

    # 🟢 2️⃣ PDF yaratish va QR kodni joylash
    p = canvas.Canvas(response, pagesize=A4)

    # PIL.Image obyektini ochib, PDF ga joylash
    qr_image = Image.open(qr_io)  # PIL.Image obyektiga o‘tkazish
    qr_x, qr_y = 400, 700  # QR kod joylashuv koordinatalari
    p.drawInlineImage(qr_image, qr_x, qr_y, width=100, height=100)

    # Student ma’lumotlarini yozish
    fan_title = student.fan.title if student.fan else "Fan belgilanmagan"

    p.drawString(100, 810, f"Familya: {student.familya}")
    p.drawString(100, 790, f"Ism: {student.ismi}")
    p.drawString(100, 770, f"Otasining ismi: {student.otasini_ismi}")
    p.drawString(100, 750, f"Telefon raqami: {student.tel_raqami}")
    p.drawString(100, 730, f"Manzil: {student.adres}")
    p.drawString(100, 710, f"Fan: {fan_title}")

    p.showPage()
    p.save()

    return response

