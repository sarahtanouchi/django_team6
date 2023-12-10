from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import SignupForm, LoginForm
 
class SignUp(generic.CreateView):
    form_class = SignupForm # 利用するフォームクラスを設定
    template_name = "accounts/sign_up.html"
 
    def get_success_url(self):
        # items:index のURL を逆引きして利用
        return reverse_lazy("items:index") 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
 
        # 以下で、 辞書データ context に値を追加
        context["title"] = "新規お客様情報登録"
        return context
        
    def signup_view(request):
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                # フォームが有効な場合は、確認画面にリダイレクトする
                request.session['signup_data'] = form.cleaned_data  # フォームの入力内容をセッションに保存
                return redirect('confirmation')  # 確認画面へリダイレクト
        else:
            form = SignupForm()
        return render(request, 'signup.html', {'form': form})

    def confirmation_view(request):
        signup_data = request.session.get('signup_data')  # セッションからフォームの入力内容を取得
        if not signup_data:
        # セッションにフォームの入力内容がない場合は新規登録画面にリダイレクトする
            return redirect('signup')

        # 確認画面でフォームの入力内容を表示
        return render(request, 'confirmation.html', {'signup_data': signup_data})
        
# ログイン
class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'accounts/login.html'
 
# ログアウト
class Logout(LogoutView):
    template_name = "accounts/logout.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "ログアウトしました"
        return context
 
# ユーザープロフィール
class Detail(LoginRequiredMixin, generic.TemplateView):
    template_name = "accounts/detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "プロフィール"
        return context
 
# ユーザープロフィールの更新
class Update(LoginRequiredMixin, generic.TemplateView):
    template_name = "accounts/update.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "プロフィール編集"
        return context
