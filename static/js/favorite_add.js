// var is_Authenticated = {{ user.is_authenticated|lower }};
var is_Authenticated = true;

function submitFavoriteForm(event) {
    event.preventDefault();
    var favoriteForm = document.getElementById('FavoriteForm');
    if (favoriteForm) {
        favoriteForm.submit();
    } else {
        console.error('FavoriteForm not found.');
        // 他に適切な処理を追加
    }
}

function addFavorite(itemId) {
    var formData = new FormData();
    formData.append('item_id', itemId);

    // Ajaxリクエスト
    $.ajax({
        type: 'POST',
        url: 'items/favorite_add/' + itemId + '/',
        data: formData,
        processData: false,
        contentType: false,
        success: function(response) {
            if (response.success) {
                console.log('お気に入り追加成功');
            } else {
                console.error('お気に入り追加失敗', response.errors);
            }
        },
        error: function() {
            console.error('通信エラー');
        }
    });
}

// お気に入り削除
function deleteFavorite(itemId) {
    // Ajaxリクエスト
    S.ajax({
        type: 'POST',
        url: '/favorite_delete/' + itemId + '/',  // URLは実際の設定に合わせて変更
        data: {},
        success: function(response) {
            if (response.success) {
                console.log('お気に入り削除成功');
            } else {
                console.error('お気に入り削除失敗', response.errors);
            }
        },
        error: function() {
            console.error('通信エラー');
        }
    });
}

function showLoginModal() {
    if (!is_Authenticated) {
        $('#loginModal').modal('show');
        return false;  
    }
    return true;  // ログインしている場合は通常の動作を続行
}

function addToFavorites(itemId, icon) {
    // お気に入り追加のロジックを実行（Ajaxなどを使用）
    // 成功した場合、アイコンの色を変更
    addFavorite(itemId);
    icon.classList.toggle('favorited');
}

// function addToCart(itemId, icon) {
//     // カート追加のロジックを実行（Ajaxなどを使用）
//     // 成功した場合、アイコンの色を変更
//     simulateAsyncRequest().then(() => {
//         icon.classList.toggle('added-to-cart');
//     });
// }

