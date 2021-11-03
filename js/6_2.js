let html = '';
let arg = 1;
let puq = `<tr data-week="3"><td>date_twice</td><td>2020-10-date_value</td>caipiaohao<td>total_value</td><td>result_value1</td><td>result_value2</td><td>result_value3</td><td>0</td><td></td></tr>`;
let arr_arg = [1, 8, 7, 3, 5, 7, 10, 2, 9, 4];
dt = function (val,page) {
    let caipiao = `<td><span class="rq1">arg1</span><span class="rq1">arg2</span><span class="rq1">arg3</span><span class="rq1">arg4</span><span class="rq1">arg5</span><span class="rq1">arg6</span><span class="rq1">arg7</span></td><td><span class="bq1">arg8</span></td>`;
    let arr = [5, 1, 7, 6, 3, 2, 4, 7];
    for (let c = 1; c <= 8; c++) {
        caipiao = caipiao.replace('arg' + c, (Math.floor(((arr_arg[arg] << 2) / 5 + c) * c / 3) + 1) + arr[page])
    }
    html += puq.replace('caipiaohao', caipiao).replace('date_twice', arg * page + 2020097).replace('date_value', '0' + page).replace('result_value3', val.value).replace('total_value', val.value * 24).replace('result_value2', val.value * 8).replace('result_value1', val.value * 15);
    arg += 1
};


get_data = function(data,page) {
    data = eval(data)
    for (let index = 0;index < 10;index ++){
        val = data[index];
        dt(val,page);
    }
    return html
}


