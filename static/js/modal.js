function logoutAndShowModal() {
    // ログアウト処理
    window.location.href = logoutUrl;

    // ログアウト完了モーダルを表示
    $('#logoutModal').modal('show');
}

// ログイン状態をJavaScriptに渡す
var isAuthenticated = isUserAuthenticated;

function showLoginModal() {
    // ログインしていない場合はモーダルを表示
    if (!isAuthenticated) {
        $('#loginModal').modal('show');
        return false;  // リンクをクリックしてもページ遷移をしない
    }
    return true;  // ログインしている場合は通常の動作を続行
}


// ログイン状態をJavaScriptに渡す
// var isAuthenticated = {% if user.is_authenticated %}true{% else %}false{% endif %};
// // ログインモーダルを表示する関数
// function showLoginModal() {
//     // ログインしていない場合はモーダルを表示
//     if (!isAuthenticated) {
//         $('#loginModal').modal('show');
//         return false;  // リンクをクリックしてもページ遷移をしない
//     }
//     return true;
// }

// // ログアウト処理とログアウト完了モーダルを表示する関数
// function logoutAndShowModal() {
//     // ログアウト処理（この部分を適切に実装）
//     $.ajax({
//         url: "{% url 'accounts:logout' %}",
//         method: 'POST',
//         success: function(data) {
//             // ログアウト完了モーダルを表示
//             $('#logoutModal').modal('show');
//         },
//         error: function(error) {
//             console.error('ログアウトエラー:', error);
//         }
//     });
// }
