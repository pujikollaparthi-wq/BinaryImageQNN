"""BinaryImageQNN URL Configuration"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# IMPORT VIEWS
from BinaryImageQNN import views as mainView
from admins import views as adminViews
from users import views as userViews


urlpatterns = [

    # =========================
    # DJANGO DEFAULT ADMIN
    # =========================
    path('admin/', admin.site.urls),

    # =========================
    # MAIN PAGES
    # =========================
    path('', mainView.index, name="index"),
    path('index/', mainView.index, name="index"),

    path('AdminLogin/', mainView.AdminLogin, name="AdminLogin"),
    path('UserLogin/', mainView.UserLogin, name="UserLogin"),
    path('UserRegister/', mainView.UserRegister, name="UserRegister"),

    # =========================
    # ADMIN MODULE
    # =========================
    path('AdminLoginCheck/', adminViews.AdminLoginCheck, name="AdminLoginCheck"),
    path('AdminHome/', adminViews.AdminHome, name="AdminHome"),

    path('RegisterUsersView/', adminViews.RegisterUsersView, name="RegisterUsersView"),

    path('ActivaUsers/<int:id>/', adminViews.ActivaUsers, name="ActivaUsers"),
    path('DeleteUser/<int:id>/', adminViews.DeleteUser, name="DeleteUser"),

    # =========================
    # USER MODULE
    # =========================
    path('UserRegisterActions/', userViews.UserRegisterActions, name="UserRegisterActions"),
    path('UserLoginCheck/', userViews.UserLoginCheck, name="UserLoginCheck"),

    path('UserHome/', userViews.UserHome, name="UserHome"),
    path('UserViewDataset/', userViews.UserViewDataset, name="UserViewDataset"),

    # =========================
    # MNIST CANVAS
    # =========================
    path('UserTestCanvasMNIST/', userViews.UserTestCanvasMNIST, name="UserTestCanvasMNIST"),

    # =========================
    # QNN PREDICTION
    # =========================
    path('MnistTorchQNN/', userViews.MnistTorchQNN, name="MnistTorchQNN"),

    # =========================
    # EDA ANALYSIS
    # =========================
    path('eda_analysis/', userViews.eda_analysis, name="eda_analysis"),

    # =========================
    # USER LOGOUT
    # =========================
    path('UserLogout/', userViews.UserLogout, name="UserLogout"),

]


# =========================
# MEDIA FILES (FOR IMAGES / DATASET)
# =========================
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)