from django.urls import path
from Applications.webblog.views import indexWebblog, seminarAWebblog, seminarBWebblog, seminarCWebblog, seminarDWebblog, tourismPhuket, researchSources, WebblogFQuestionPage, WebblogAnswerFromQuestionPage, WebblogFormPage, WebblogFormDetailPage, DashBoardPage, DashBoardPageCovid

urlpatterns = [
    path('', indexWebblog, name='indexWebblog'),
    path('seminarAWebblog/', seminarAWebblog, name='seminarAWebblog'),
    path('seminarBWebblog/', seminarBWebblog, name='seminarBWebblog'),
    path('seminarCWebblog/', seminarCWebblog, name='seminarCWebblog'),
    path('seminarDWebblog/', seminarDWebblog, name='seminarDWebblog'),
    path('tourismPhuket/', tourismPhuket, name='tourismPhuket'),
    path('researchSources/', researchSources, name='researchSources'),
    path('WebblogFQuestionPage/', WebblogFQuestionPage, name='WebblogFQuestionPage'),
    path('WebblogAnswerFromQuestionPage/', WebblogAnswerFromQuestionPage, name='WebblogAnswerFromQuestionPage'),   
    path('WebblogFormPage/', WebblogFormPage, name='WebblogFormPage'),
    path('WebblogFormDetailPage/', WebblogFormDetailPage, name='WebblogFormDetailPage'),
    path('DashBoardPage/', DashBoardPage, name='DashBoardPage'),
    path('DashBoardPageCovid/', DashBoardPageCovid, name='DashBoardPageCovid'),

]