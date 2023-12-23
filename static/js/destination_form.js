var selecterBox = document.getElementById('destination_form');

function formSwitch() {
    const check = document.getElementsByClassName('js-check')
    if (check[0].checked) {
        selecterBox.style.display = "none";
    } else if (check[1].checked) {
        selecterBox.style.display = "block";
    } else if (check[2].checked) {
        selecterBox.style.display = "block";
    } else {
        selecterBox.style.display = "none";
    }
}
window.addEventListener('load', formSwitch());

// function entryChange2(){
//     if(document.getElementById('changeSelect')){
//     id = document.getElementById('changeSelect').value;
//     }   
// }