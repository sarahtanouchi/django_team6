var isAuthenticated = true;


function addFavorite(itemId) {
    // アイテムIDを取得し、フォームデータを作成
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
    $.ajax({
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
    // ログインしていない場合はモーダルを表示
    if (!isAuthenticated) {
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

// 非同期リクエストを模倣する関数
function simulateAsyncRequest() {
    return new Promise(resolve => {
        // 仮の非同期処理（実際にはAjaxなどを使用する）
        setTimeout(resolve, 1000);
    });
}
