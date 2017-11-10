/*
 * バリデーションの結果を画面に表示する
 * 単数レコード用
 * 引数:
 *      必須:Category ID
 *          Char
 *              新規の場合は、NEW
 *              新規以外は、ID
 *      必須:data
 *          Char
 *            入力項目名|バリデーション名|判定結果
 *            例
 *              入力項目:CATE_NM、LIST_NM
 *              検証内容:それぞれに値必須
 *              入力値  :CATE_NM="ABC",LIST_NM=Null
 *              結果    :CATE_NM|ISNULL|OK LIST_NM|ISNULL|NG
 *      必須:method
 *          Char
 *            新規の場合、POST
 *            更新の場合、PUT
 *            削除の場合、DELETE
 *      任意:bfrVal
 *          Char
 *            変更前項目名|変更前の値
 *      任意:aftVal        
 *          Char
 *            変更後項目名|変更後の値
 */
function validationResultDisplay(id, data, method, bfrVal ,aftVal,) {
    var data_arry = data.split(" ");  // 空白で分割
    var len = data_arry.length;
    var ngmsg = '';
    var ngcount = 0;
    $('input').removeClass("label-danger");
    for (var i = 1; i < len; i++){
        //alert(data_arry[i]);
        var report = data_arry[i].split("|");
        var item = report[0];           //項目名
        var valid = report[1];          //バリデーション名
        var result = report[2].trim();  //結果(OK/NG)
        //alert(item);
        //alert(valid);
        //alert(result);
        var msg_ele = '#' + item + '_' + valid + '_MSG';
        var lvl_ele = '#' + item + '_' + id;
        var lvl_cls = '###' + item + '_' + valid + '_LBL###';
        if (result == 'NG') {
            alert(lvl_ele);
            ngcount ++;
            $(msg_ele).addClass("show"); 
            $(msg_ele).removeClass("hidden"); 
            $(lvl_ele).removeClass(lvl_cls); 
            $(lvl_ele).addClass("label-danger"); 
            //alert(item + '_' + valid + '_' + result); 
        } else {
            $(msg_ele).addClass("hidden"); 
            $(msg_ele).removeClass("show"); 
        }
    }

    //var msgArrBfr = bfrVal.split("|");
    //var msgArrAFT = AFTVal.split("|");
    switch (method) {
        case "POST":
            //var inputNm = msgArrAft[0];
            //var inputVal = msgArrAft[1];
            //var msg = inputVal  + "を追加しました。"
            var msg = "バリデーションエラーの為、新規追加出来ませんでした。"
            break;
        case "PUT":
            //var inputNm = msgArrBfr[0];
            //var inputValBfr = msgArrBfr[1];
            //var inputValAFT = msgArrAfr[1];
            //var msg = inputNm + "を"  + inputValBfr + "から" + inputValAft + "に変更しました。"
            var msg = "バリデーションエラーの為、更新出来ませんでした。"
            break;
        case "DELET":
            //var inputNm = msgArrBfr[0];
            //var inputVal = msgArrBfr[1];
            //var msg = inputVal  + "削除しました。"
            var msg = "バリデーションエラーの為、削除出来ませんでした。"
            break;
        default:
            var msg = "バリデーションエラーです。"
    }
    alert(msg);
    return 'OK';
}



