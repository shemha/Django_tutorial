# venv/lib/python3.8/site-packages/django/shortcuts.pyの'render'メソッド, 'redirect'メソッド, 'get_object_or_404'メソッド
from django.shortcuts import get_object_or_404, render, redirect  # 'redirect', 'get_object_or_404'追加
# venv/lib/python3.8/site-packages/django/contrib/auth/__init__.pyの'authenticate'メソッド, 'login'メソッド
from django.contrib.auth import authenticate, login
# app/forms.pyの'CustomUserCreationForm'クラス
from .forms import CustomUserCreationForm
# app/models.pyの'Product'クラス
from .models import Product
# venv/lib/python3.8/site-packages/django/contrib/auth/decorators.pyの'login_require'メソッド
from django.contrib.auth.decorators import login_required
# venv/lib/python3.8/site-packages/django/views/decorators/http.pyの'require_POST'変数
from django.views.decorators.http import require_POST
# venv/lib/python3.8/site-packages/django/contrib/messagesディレクトリ
from django.contrib import messages
# app/forms.pyの'AddToCartForm'クラス
from .forms import AddToCartForm
import json
import requests
# app/models.pyの'Sale'クラス
from .models import Sale
# app/forms.pyの'PurchaseForm'クラス
from .forms import PurchaseForm

# Create your views here.
# トップページ
def index(request):
    print(fetch_address('1000001'))
    products = Product.objects.all().order_by('-id')
    return render(request, 'app/index.html', {'products': products})


# サインアップページ
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            input_email = form.cleaned_data['email']
            input_password = form.cleaned_data['password1']
            new_user = authenticate(
                email=input_email,
                password=input_password,
            )
            if new_user is not None:
                login(request, new_user)
                return redirect('app:index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'app/signup.html', {'form': form})


# 商品詳細ページ
def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    # 「カートに追加する」ボタンが押された時
    if request.method == "POST":
        add_to_cart_form = AddToCartForm(request.POST)
        if add_to_cart_form.is_valid():
            num = add_to_cart_form.cleaned_data['num']
            # セッションに'cart'というキーが存在するかどうか(初めてカート追加するかどうか)で処理を分ける
            if 'cart' in request.session:
                # すでに対象商品がカートにあれば新しい個数を加算、なければ新しくキーを追加する
                if str(product_id) in request.session['cart']:
                    request.session['cart'][str(product_id)] += num
                else:
                    request.session['cart'][str(product_id)] = num
            else:
                # 初めてのカート追加の場合、新しく'cart'というキーをセッションに追加する
                request.session['cart'] = {str(product_id): num}
            messages.success(request, f"{product.name}を{num}個カートに⼊れました!")
            return redirect('app:detail', product_id=product_id)
    
    # request.methodがGETのとき(画⾯にアクセスされたとき)は空のフォームを表⽰する
    add_to_cart_form = AddToCartForm()
    context = {
        'product': product,
        'add_to_cart_form': add_to_cart_form,
    }
    return render(request, 'app/detail.html', context)


# 「「お気に⼊りする・お気に⼊りから外す」ボタン機能
@login_required
@require_POST
def toggle_fav_product_status(request):
    """お気に⼊り状態を切り替える関数"""

    product = get_object_or_404(Product, pk=request.POST["product_id"])
    user = request.user

    if product in user.fav_products.all():
        # productがユーザーのfav_productsに既に存在している場合(お気に⼊り済の場合)
        # → productをfav_productsから除外する(お気に⼊りを外す)
        user.fav_products.remove(product)
    else:
        # productがユーザーのfav_productsに存在しない場合(お気に⼊りしていない場合)
        # → productをfav_productsに追加する(お気に⼊り登録する)
        user.fav_products.add(product)
    return redirect('app:detail', product_id=product.id)


# お気に⼊り商品⼀覧
@login_required
def fav_products(request):
    user = request.user
    products = user.fav_products.all()
    return render(request, 'app/index.html', {'products': products})


# 商品を追加・削除機能
@login_required
@require_POST
def change_product_amount(request):

    # name="product_id"のフィールドの値を取得(どの商品を増減させるか)
    product_id = request.POST["product_id"]
    # セッションから"cart"情報を取得
    cart_session = request.session['cart']

    # セッションの更新
    if product_id in cart_session:
        # 1つ減らすボタンが押された時
        if "action_remove" in request.POST:
            cart_session[product_id] -= 1
        # 1つ増やすボタンが押された時
        if "action_add" in request.POST:
            cart_session[product_id] += 1
        # 商品個数が0以下になった場合は、カートから対象商品を削除
        if cart_session[product_id] <= 0:
            del cart_session[product_id]
    return redirect('app:cart')


def fetch_address(zip_code):
    """
    郵便番号検索APIを利⽤する関数
    引数に指定された郵便番号に対応する住所を返す
    住所取得に失敗した場合は空⽂字を返す
    """

    REQUEST_URL = f'http://zipcloud.ibsnet.co.jp/api/search?zipcode={zip_code}'
    response = requests.get(REQUEST_URL)
    response = json.loads(response.text)
    results, api_status = response['results'], response['status']
    
    address = ''
    # レスポンスステータスが200 かつ 'results'が存在する場合
    # → address変数に取得した住所を代⼊する
    if api_status == 200 and results is not None:
        result = results[0]
        address = result['address1'] + result['address2'] + result['address3']
    return address


@login_required
def cart(request):
    user = request.user

    # セッションから'cart'キーに対応する辞書を取得する。
    # セッションに'cart'キーが存在しない場合は{}(空の辞書)がcart変数に代⼊される。
    cart = request.session.get('cart', {})

    # cart_products → Productオブジェクトをキー、購⼊個数を値として持つ辞書
    # (初期値は空の辞書)
    cart_products = {}

    # total_price → カート内商品の合計⾦額を表す変数(初期値は0)
    total_price = 0

    # 合計⾦額の計算
    # cart_prodcutsとtotal_priceを更新する
    for product_id, num in cart.items():
        product = Product.objects.filter(id=product_id).first()
        if product is None:
            # productがNoneのとき(対象商品がデータベースから削除されている場合等)は画⾯に表⽰しない
            continue
        cart_products[product] = num
        total_price += product.price * num
    
    if request.method == 'POST':
        purchase_form = PurchaseForm(request.POST)
        
        if purchase_form.is_valid():
            
            # 住所検索ボタンが押された場合
            if 'search_address' in request.POST:
                zip_code = request.POST['zip_code']
                address = fetch_address(zip_code)
                # 住所が取得できなかった場合はメッセージを出してリダイレクト
                if not address:
                    messages.warning(request, "住所を取得できませんでした。")
                    return redirect('app:cart')
                # 住所が取得できたらフォームの値として⼊⼒する
                purchase_form = PurchaseForm(
                    initial={'zip_code': zip_code, 'address': address}
                )

            # 購⼊処理ボタンが押された場合
            if 'buy_product' in request.POST:
                # 住所が⼊⼒済みかを確認する。未⼊⼒の場合はリダイレクトする。
                if not purchase_form.cleaned_data['address']:
                    messages.warning(request, "住所の⼊⼒は必須です。")
                    return redirect('app:cart')
                # カートが空じゃないかを確認する。空の場合はリダイレクトする。
                if not cart:
                    messages.warning(request, "カートは空です。")
                    return redirect('app:cart')
                # 所持ポイントが⼗分にあるかを確認する。不⾜してる場合はリダイレクトする。
                if total_price > user.point:
                    messages.warning(request, "所持ポイントが⾜りません。")
                    return redirect('app:cart')

                # 各プロダクトのSale情報を保存(売上記録の登録)
                for product, num in cart_products.items():
                    sale = Sale(
                        product=product,
                        user=request.user,
                        amount=num,
                        price=product.price,
                        total_price=num * product.price,
                    )
                    sale.save()

                # 購⼊した分だけユーザーの保有ポイントを減らす。
                user.point -= total_price
                user.save()
                # セッションから'cart'を削除してカートを空にする。
                del request.session['cart']
                messages.success(request, "商品の購⼊が完了しました！")
                return redirect('app:cart')

    else:
        purchase_form = PurchaseForm()
    context = {
        'purchase_form': purchase_form,
        'cart_products': cart_products,
        'total_price': total_price,
    }
    return render(request, 'app/cart.html', context)


@login_required
def order_history(request):
    user = request.user
    sales = Sale.objects.filter(user=user).order_by('-created_at')
    return render(request, 'app/order_history.html', {'sales': sales})