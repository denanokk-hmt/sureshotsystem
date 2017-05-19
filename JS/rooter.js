
// CGIをを実行する
function doRootCGI(url)
{
    document.location.href = url;
}


// Submitする
// 使用例
// <input type="button" value="ただのボタン" onclick="return mySubmit('myForm', 'form.html', 'POST');">
function mySubmit(formName, url, method)
{
    var f = document.forms[formName];
    f.method = method; // method(GET or POST)を設定する
    f.action = url; // action(遷移先URL)を設定する
    f.submit(); // submit する
    return true;
}
