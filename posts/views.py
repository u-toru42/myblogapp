from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

def index(request):
    # return HttpResponse("Hello World! このページは投稿のインデックスです。")
    posts = Post.objects.order_by('-published') # published:降順
    return render(request, 'posts/index.html', {'posts': posts})
# URLからpost_idを取得し、ページに表示する。id番号を使い、テンプレートに遷移させる
def post_detail(request, post_id):
    # post_idを番号化してオブジェクトのデータを表示
    # 存在しないオブジェクトの場合404エラーを返す処理
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/post_detail.html', { 'post': post })
# Create your views here.