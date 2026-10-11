from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages

import json
import base64
import numpy as np
import io
from PIL import Image

from .models import UserRegistrationModel
from .utility.QNNPyTorchModel import predict_digit


# ================= USER REGISTER =================

def UserRegisterActions(request):

    if request.method == "POST":

        name = request.POST.get("name")
        loginid = request.POST.get("loginid")
        password = request.POST.get("password")
        mobile = request.POST.get("mobile")
        email = request.POST.get("email")
        locality = request.POST.get("locality")
        address = request.POST.get("address")
        city = request.POST.get("city")
        state = request.POST.get("state")

        if UserRegistrationModel.objects.filter(loginid=loginid).exists():

            return render(request, "UserRegister.html", {
                "msg": "Login ID already exists"
            })

        else:

            UserRegistrationModel.objects.create(
                name=name,
                loginid=loginid,
                password=password,
                mobile=mobile,
                email=email,
                locality=locality,
                address=address,
                city=city,
                state=state,
                status="activated"
            )

            return render(request, "UserLogin.html", {
                "msg": "Registered Successfully. Please Login."
            })

    return render(request, "UserRegister.html")


# ================= USER LOGIN =================

def UserLoginCheck(request):

    if request.method == "POST":

        loginid = request.POST.get("loginid")
        password = request.POST.get("password")

        try:

            user = UserRegistrationModel.objects.get(
                loginid=loginid,
                password=password
            )

            request.session["user"] = user.name

            messages.success(request, "Login Successful")
            return redirect("UserHome")

        except UserRegistrationModel.DoesNotExist:

            messages.error(request, "Invalid Login Details")
            return redirect("UserLogin")

    return render(request, "UserLogin.html")


# ================= USER LOGOUT =================

def UserLogout(request):

    if "user" in request.session:
        del request.session["user"]

    messages.success(request, "Logged out successfully")
    return redirect("index")


# ================= USER HOME =================

def UserHome(request):

    if "user" not in request.session:
        return redirect("UserLogin")

    return render(request, "users/UserHomePage.html")


# ================= VIEW DATASET =================

def UserViewDataset(request):

    if "user" not in request.session:
        return redirect("UserLogin")

    return render(request, "users/user_view_data.html")


# ================= CANVAS PAGE =================

def UserTestCanvasMNIST(request):

    if "user" not in request.session:
        return redirect("UserLogin")

    return render(request, "users/UserHomeCanvas.html")



def MnistTorchQNN(request):

    if request.method == "POST":

        try:

            data = json.loads(request.body)

            image_data = data.get("image")
            actual_digit = data.get("actual")

            actual_digit = int(actual_digit)

            # remove base64 header
            image_data = image_data.split(",")[1]

            image_bytes = base64.b64decode(image_data)

            # create PIL image
            image = Image.open(io.BytesIO(image_bytes)).convert("L")

            prediction = predict_digit(image)

            result = prediction == actual_digit

            return JsonResponse({
                "prediction": prediction,
                "result": result
            })

        except Exception as e:

            return JsonResponse({
                "prediction": -1,
                "result": str(e)
            })


# ================= EDA =================

def eda_analysis(request):

    if "user" not in request.session:
        return redirect("UserLogin")

    return render(request, "users/eda_analysis.html")