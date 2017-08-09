from django.views.generic import View, TemplateView
from django.http import JsonResponse, HttpResponse






class PostlistView1(View):
    def get(self, request):
        name='공유'
        html=self.get_template_string().format(name=name)
        return HttpResponse(html)
    def get_template_string(self):    #이런 것은cbv 에서만 가능하다.
        return'''
             <h1>Askdjango</h1>
             <p>{name}</p>
             <p> 파이썬 열심히 공부해서 웹 개발을 할 수 있도록 하자!</p>
          '''

post_list1 = PostlistView1.as_view()


class PostlistView2(TemplateView):
    template_name='dojo/post_list.html'

    def get_context_data(self):
        context= super().get_context_data()
        context['name']= '공유'
        return context


post_list2=PostlistView2.as_view()

class PostlistView3(object):
    pass

class ExcelDownloadView(object):
    pass



