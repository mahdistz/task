from django.shortcuts import redirect
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from user.forms import LoginForm
from user.models import Users
from user.serializers import RegisterSerializer
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView


class Home(TemplateView):
    template_name = "home.html"


# Class based view that extends from the built-in login view to add remember me functionality
class Login(LoginView):
    form_class = LoginForm
    template_name = 'login.html'

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')
        if not remember_me:
            # set session expiry to 0 seconds.
            # So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)
            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True
        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(Login, self).form_valid(form)

    def get(self, request, *args, **kwargs):
        tokens = self.request.token
        return redirect('chart', {'tokens': tokens})


class UserRegistrationView(CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        status_code = status.HTTP_201_CREATED
        response = {
            'success': 'True',
            'status code': status_code,
            'message': 'User registered successfully',
        }

        return Response(response, status=status_code)


class UserDetailView(RetrieveUpdateAPIView):
    queryset = Users.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [IsAuthenticated]


class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return ["Chrome", "Firefox", "Internet Explore", "Safari", "Edge", "Opera", "other"]

    def get_data(self):
        """Return 1 datasets to plot."""
        return [[75, 44, 92, 11, 44, 95, 35], ]


line_chart = TemplateView.as_view(template_name='chart.html')
line_chart_json = LineChartJSONView.as_view()
