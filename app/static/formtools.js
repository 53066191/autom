function transformToJson(formData) {
    var res = {}
    for (var i in formData) {
        /*[{"name":"user","value":"hpc"},{"name":"pwd","value":"123"},{"name":"sex","value":"M"},{"name":"age","value":"100"},{"name":"phone","value":"13011112222"},{"name":"email","value":"xxx@xxx.com"}]
    */
        //下标为的i的name做为json对象的key，下标为的i的value做为json对象的value
        res[formData[i].name] = formData[i]['value'];
    }

    return JSON.stringify(res);
}


function getFormData(form_id) {
    var myform = $(form_id);
    var data = myform.serializeArray();
    var jsons = transformToJson(data);
    return jsons
}