
$('.spinner').each(function() {

    var el  = $(this);
    var add = $('.spinner-add');
    var sub = $('.spinner-sub');
    
    // substract
    // −ボタンを押した時のクリックイベント
    el.parent().on('click', '.spinner-sub', function() {
    // もし.spinnerのvalueが最小値よりも大きかったら
        if (el.val() > parseInt(el.attr('min'))) {
    // valueの値を-1する
            el.val(function(i, oldval) {
                return --oldval;
            });
        }
    // disabled
    // もし.spinnerのvalueが最小値と同じだったら
        if (el.val() == parseInt(el.attr('min'))) {
    // .spinnerの直前のspinner-subクラスにdisabledを付与する
            el.prev(sub).addClass('disabled');
        }
    // もし.spinnerのvalueが最大値より小さかったら
        if (el.val() < parseInt(el.attr('max'))) {
    // .spinnerの直後のspinner-addクラスのdisabledを外す
            el.next(add).removeClass('disabled');
        }
    });
    
    // increment
    //＋ボタンを押した時のクリックイベント
    el.parent().on('click', '.spinner-add', function() {
    // もし.spinnerのvalueが最大値よりも小さかったら
        if (el.val() < parseInt(el.attr('max'))) {
    // valueの値を+1する
            el.val(function(i, oldval) {
                return ++oldval;
            });
        }
    // disabled
    // もし.spinnerのvalueが最小値より大きかったら
        if (el.val() > parseInt(el.attr('min'))) {
    // .spinnerの直前のspinner-subクラスのdisabledを外す
            el.prev(sub).removeClass('disabled');
        }
    // もし.spinnerのvalueが最大値と同じだったら
        if (el.val() == parseInt(el.attr('max'))) {
    // .spinnerの直後のspinner-addクラスにdisabledを付与する
            el.next(add).addClass('disabled');
        }
    });
})